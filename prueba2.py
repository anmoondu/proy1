import time
import streamlit as st
import random
import Funciones

st.set_page_config(
    page_title="ProyectoI: Científicos de sueños",
    page_icon="💤"
)


st.title('Mejora tu sueño')
st.write('# :blue[*en tan solo 2 minutos*]')
st.image('sueño3.jpg')
with st.sidebar:
     st.markdown('### Científicos de sueños')
     with st.expander('# :blue[**Quiénes somos**]'):
        st.write('''
             Científicos de sueños es un grupo de estudiantes del grado 
             en Ciencia de Datos por la Universidad Politécnica de Valencia, 
             que nace gracias a la asignatura de Proyecto I, y con el fin de realizar 
             un estudio de los hábitos diarios para comprobar si estos afectan a la 
             calidad o a la capacidad de dormir de cada individuo.
             ''')
     puntuacion = st.slider("_**¿Te ha gustado la\npágina:**_", 0, 10)
     if puntuacion > 7.5:
          st.write("_Muchas gracias, \nnos alegramos de que te guste_")
          #st.balloons()
     elif puntuacion > 5 and puntuacion < 7.5:
          st.write('_Gracias por la valoración_')
     elif puntuacion == 0:
          pass
     else:
          st.write("_Sentimos que no te haya gustado_")
     st.image('logo.png')


opciones_ocupacion = ["Trabajo", "Soy universitari@", "Estudio (FP, Bachiller, ESO...)", "Trabajo y Estudio", "Ninguna de las anteriores"]
opciones_genero = ["Masculino", "Femenino","Otro"]
opciones_estudios = ['No estudio actualmente', 'Ingenierías', 'Ciencias puras', 'Ciencias de la salud', 'Arquitectura', 'Ciencias sociales y jurídicas',
                     'Humanidades', 'Artes']
opciones_trabajo = ['No trabajo', 'Sanitario', 'Ocio', 'Empresarial', 'Científico', 'Ingenierías', 'Ciencias políticas y jurídicas', 'Creativo',
                    'Industrial','Digital','Docente', 'Seguridad','Agrícola','Financiero','Estético','Otros']
if opciones_trabajo == 'Científico':
     opciones_trabajo = 'Cientifico'
if opciones_trabajo == 'Ingenierías':
     opciones_trabajo = 'Ingenierias'
if opciones_trabajo == 'Otros':
     opciones_trabajo = 'Tareas domésticas/ cuidado/ transporte'
if opciones_trabajo == 'Agrícola':
     opciones_trabajo = 'Agricola y otros materiales'
if opciones_trabajo == 'Estético':
     opciones_trabajo = 'Estetico'
opciones_horario = ["Mañanas", "Tardes","Noche"]
opciones_trastorno = ["Ninguno", "Insomnio","Bruxismo","Apnea del sueño","Hipersomnia","Parálisis del sueño",
                      "Sonambulismo","Narcolepsia", 'Prefiero no contestar', 'Otro']
opciones_sino = ["Sí", "No"]
opciones_saludmental = ["Ninguna", "Trastorno de ansiedad","Depresión, trastorno bipolar y otros trastornos del estado de ánimo",
                        "Trastornos de la personalidad","Trastorno de estrés post-traumático"]
opciones_antesdormir= ["Veo la TV", "Leer","Uso pantallas (móvil, tablet...)","Me acuesto justo después de cenar","Otro"]
opciones_compania = ["Sí", "No","Ocasionalmente"]
genero = st.radio("**1. Sexo:**", opciones_genero)
edad = st.slider("**2. ¿Qué edad tienes?**", 10, 100,)
altura = st.slider("**3. ¿Cuánto mides? (m)**", 1.00, 2.50, )
peso = st.slider("**4. ¿Cuánto pesas? (kgs)**", 30, 150, )
IMC = peso/(altura**2)
st.info(f'El IMC que usaremos para los análisis es: {IMC:.2f}')
horas = st.slider("**5. ¿Cuántas horas duermes al día?:**", 0, 15)
if horas == 15:
     st.warning("⚠️ ¿Seguro que duermes 15 horas?")
ocupacion = st.radio("**6. ¿A qué te dedicas?:**", opciones_ocupacion)
estudio = st.multiselect("**7. ¿Cuál es la rama de tus estudios?:**", opciones_estudios)
trabajo = st.multiselect("**8. ¿En qué sector trabajas?:**", opciones_trabajo)
horario = st.multiselect("**9. ¿Cuál es tu horario de trabajo/estudio?:**", opciones_horario)
pantallas = st.slider("**10. ¿Cuántas horas pasas al día con pantallas?:**", 0, 24)
ejercicio = st.slider("**11. ¿Cuántos días a la semana haces ejercicio?:**", 0, 7)
pasos_diarios = st.number_input("**12. Pasos diarios:**", min_value=0, max_value=30000, step=1)
estres = st.slider("**13. ¿Cómo calificarías tu estrés diario¿:**", 0, 10)
trastorno_sueno = st.multiselect("**14. ¿Tienes algún trastorno del sueño?:**", opciones_trastorno)
despertarse = st.radio("**15. ¿Te despiertas durante la noche?:**", opciones_sino)
trastorno_saludmental = st.multiselect("**16. ¿Tienes algún problema de salud mental?:**", opciones_saludmental)
medicacion = st.radio("**17. ¿Tomas medicación para dormir?:**", opciones_sino)
antesdormir = st.multiselect("**18. ¿Qué haces antes de dormir?:**", opciones_antesdormir)
compania = st.radio("**19. ¿Duermes en compañía?:**", opciones_compania)
presion_arterial_diastolica = st.slider("**20. Presión arterial diastólica (la menor):**", 40, 150, )
presion_arterial_sistolica = st.slider("**21. Presión arterial sistólica (la mayor):**", 60, 200, )
pulsaciones = st.slider("**22. Pulsaciones (por minuto):**", 40, 150, )


def horass(horas):
     if horas < 7:
          n = 7-horas
          st.write('Te recomendamos dormir',n,'horas más')
     elif horas > 9:
          n1 = horas - 8
          st.write('Te recomendamos dormir', n1, 'horas menos')
     else:
          st.write('Duermes una cantidad de horas adecuada')
    
def pant(pantallas):
     if pantallas > 8:
          n = pantallas - 8
          st.write('Deberías reducir el tiempo de pantallas por lo menos', n, 'horas')
     else:
          pass
def sport(ejercicio):
     if ejercicio == 2:
          n = 3 - ejercicio
          st.write('Para mejorar la calidad haz',n, 'día más de deporte')
     elif ejercicio == 0 or ejercicio == 1:
          n = 3 - ejercicio
          st.write('Para mejorar la calidad haz',n, 'días más de deporte')
     else:
          pass

def pasos(pasos):
     if pasos < 10000:
          n = 10000 - pasos
          st.write('Para tener una mejor calidad del sueño deberías hacer 10000 pasos diarios, ', n, 'más de los actuales')

def estress(estres):
     if estres > 5 and estres <  8:
          st.write('Tienes un nivel de estrés medio, para mejorar la calidad incorpora hábitos que puedan disminuir el estrés')
     elif estres >= 8:
          st.write('Tienes un nivel de estrés alto, para mejorar la calidad incorpora hábitos que puedan disminuir el estrés')
     else:
          pass

def medicacionn(medica):
     if medica == 'Sí':
          st.write('Dado que tomas medicación, recomendamos la mejora de ciertos hábitos saludables para evitar esta toma')
     else:
          pass

btn_continuar = st.button('Analizar')
if btn_continuar:
    with st.spinner('Analizando...'):
        time.sleep(3)  # Simular una operación de carga
    #my_bar = st.progress(5)
    #for percent_complete in range(100):
     #   time.sleep(0.001)
      #  my_bar.progress(percent_complete + 1)

    st.title('Resultados')
    
    Pregunta = ["Género", "Edad", "Altura", "Peso", "Rama de estudios", 
           "Sector de trabajo", "Horario de trabajo/estudio", 
           "Horas de sueño", "Horas uso de pantallas", "Ejercicio", 
           "Estrés diario", "Trastornos del sueño", "Despertarse durante la noche",
           "Trastorno salud mental", "Medicación para dormir",
           "Antes de dormir", "Dormir en compañía", "IMC", 'Presión arterial diastolica', 'Presión arterial sistólica', 'Pulsaciones']

    Respuesta = [genero, edad, altura, peso, estudio, trabajo, 
           horario, horas, pantallas, ejercicio, estres, trastorno_sueno, despertarse, trastorno_saludmental, medicacion,
           antesdormir, compania, IMC, presion_arterial_diastolica, presion_arterial_sistolica, pulsaciones]

    X_user = Funciones.depurarDatos(Funciones.crearDF(Pregunta, Respuesta))

    y=Funciones.resultado(X_user)
    st.write('### :black[Tu calidad de sueño es: ]', y)

    st.write('### :black[Te recomendamos: ]')
    horass(horas)
    # st.write('Se recomienda dormir entre 7 y 9 horas, siendo mejor dormir 1h de más que de menos')
    pant(pantallas)
    # st.write('Se recomienda un uso de pantallas de menos de 8 horas diarias, siempre que estas sean necesarias por trabajo, en caso contrario recomendamos disminuirlas más')
    sport(ejercicio)
    pasos(pasos_diarios)
    estress(estres)
    medicacionn(medicacion)

    st.video('https://www.youtube.com/watch?v=viA1ZK5ud7A&ab_channel=S%C3%A9Curioso%E2%80%94TED-Ed')

