import requests as consulta

#https://restcountries.com

def obtener_datos_Pais(name):
    response = consulta.get(f'https://restcountries.com/v3.1/name/{name}')
    respuesta = response.json()


    