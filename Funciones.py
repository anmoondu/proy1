

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:26:45 2024

@author: User
"""

# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import MultiLabelBinarizer

def recodificar_siOno(str):
    if str == 'No':
        return 0
    else:
        return 1

def recodificar_genero(str):
    if str == 'Masculino':
        return 0
    if str == 'Femenino':
        return 1
    else:
        return 2

def str_a_lista(cadena):
    if not isinstance(cadena, list):
        palabras = cadena.split(',')
        palabras_limpio = list(palabra.strip() for palabra in palabras)
        return palabras_limpio
    else:
        return cadena

df_Tree = pd.read_csv('df_Tree.csv')

df_Tree = df_Tree.dropna()

X = df_Tree.drop(columns=['Calidad del sueño'])
y = df_Tree['Calidad del sueño']

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.218, random_state=42)

# Paso 3: Crear y entrenar el modelo
regressor = DecisionTreeRegressor(random_state=42, max_depth=4)
regressor.fit(X_train, y_train)
y_prue = regressor.predict(X_test)  # Cambiando X_Test por el dataset con los datos que ha puesto el usuario se devolverá la predicció

def resultado(X_user):
    y_pred = regressor.predict(X_user)
    return y_pred

def crearDF(variables, respuestas):  # respuestas será una lista con todas las respuestas
    df = pd.DataFrame({
        "Pregunta": variables,
        "Respuesta": respuestas
    })
    data = {row['Pregunta']: row['Respuesta'] for index, row in df.iterrows()}
    new_df = pd.DataFrame([data])
    return new_df

def depurarDatos(df):
    df['Despertarse durante la noche'] = df['Despertarse durante la noche'].map(recodificar_siOno)
    df['Medicación para dormir'] = df['Medicación para dormir'].map(recodificar_siOno)
    df['Género'] = df['Género'].map(recodificar_genero)
    
    variables_cualitativas = df.select_dtypes(include=['object'])
    df_sin_cualitativas = df.select_dtypes(include=['number'])
    df_cualitativas = df[variables_cualitativas.columns].copy()
    
    MLB = pd.DataFrame()
    for column in df_cualitativas:
        mlb = MultiLabelBinarizer()
        df_cualitativas[column] = df_cualitativas[column].map(str_a_lista)
        new_columns = [(column + ': ' + x) for x in mlb.fit(df_cualitativas[column]).classes_]
        new_data = pd.DataFrame(mlb.transform(df_cualitativas[column]), columns=new_columns)
        MLB = pd.concat([MLB, new_data], axis=1)
        
    df_User = pd.concat([df_sin_cualitativas, MLB], axis=1)
    df_arbol = pd.DataFrame(columns=X.columns)
    
    for column in df_arbol.columns:
        if column in df_User.columns:
            df_arbol[column] = df_User[column]
        else:
            df_arbol[column] = 0
            
    return df_arbol

Pregunta = ["Género", "Edad", "Altura", "Peso", "Rama de estudios", 
           "Sector de trabajo", "Horario de trabajo/estudio", 
           "Horas de sueño", "Horas uso de pantallas", "Ejercicio", 
           "Estrés diario", "Trastornos del sueño", "Despertarse durante la noche",
           "Trastorno salud mental", "Medicación para dormir",
           "Antes de dormir", "Dormir en compañía", "IMC"]

Respuesta = ["Femenino", 25, 175, 70, "Ingeniería", "Industrial", 
            "Mañanas", 1, 4, 3, 7, "Ninguno", "No", "Ninguno", "No",
            "Leer", "No", 22.9]

X_user = depurarDatos(crearDF(Pregunta, Respuesta))

print(X_user)
