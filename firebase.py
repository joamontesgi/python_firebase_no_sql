import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import random
import json


base_datos_url = 'https://taller-clase-ef757-default-rtdb.firebaseio.com/'
cred = credentials.Certificate("taller-clase-ef757-firebase-adminsdk-ip06z-3e82da3827.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': base_datos_url
})

# Actualizar un documento de la colección 'resumen' por su identificador
def actualizar(id):
    referencia = db.reference('/resumen')
    referencia.child(id).update({
        'total_ventas': 1,
        'promedio': 1,
        'total_ordenes': 1
    })
    return "Se ha actualizado"

# Eliminar un documento de la colección 'resumen' por su identificador
def eliminar(id):
    referencia = db.reference('/resumen')
    referencia.child(id).delete()
    return "Se ha eliminado correctamente"
    
# Consultar datos de la colección 'resumen'
def leer():
    referencia = db.reference('/resumen')
    return referencia.get()

# Insertar 10 documentos en la colección 'resumen'
def insertarValores():
    referencia = db.reference('/resumen')
    for _ in range(10):
        datos = {
            'total_ventas': random.randint(1, 99),
            'promedio': random.randint(1, 99),
            'total_ordenes':random.randint(1, 99)
        }
        referencia.push(datos)
    return "Se han ingresado los datos"

# Guardar los datos de la colección 'resumen' en un archivo JSON
def guardarJson():
    referencia = db.reference('/resumen')
    datos = referencia.order_by_child('total_ordenes').get()
    with open('valores.json', 'w') as file:
        json.dump(datos, file, indent=4)
    return datos

# Insertar en la colección 'personas' 10 documentos.
def insertarPersonas():
    referencia = db.reference('/personas')
    for _ in range(10):
        datos = {
            'Nombre': random.choice(['A','B', 'C', 'D']),
            'Genero': random.choice(['Masculino','Femenino']),
            'Edad':   random.randint(10, 80)
        }
        referencia.push(datos)
    return "Se han ingresado los datos"

# Busca las personas que tengan el género definido
def buscarGenero(genero):
    referencia = db.reference('/personas')
    personas = referencia.order_by_child('Genero').equal_to(genero).get()
    return personas

# genero = "Masculino"
# print(buscarGenero(genero))
# print(insertarPersonas())
# print(guardarJson())
# print(insertarValores())