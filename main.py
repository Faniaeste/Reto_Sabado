import requests as consulta

#https://restcountries.com



name = input("Introduce el País en Ingles:")
response = consulta.get('https://restcountries.com/v3.1/name/{name}')
respuesta = response.json()
print("Nombre del pais: ",respuesta[0]['name'])
print("Moneda: ", respuesta[0]['currencies'])
print("Capital", respuesta[0]['capital'])
print("Lenguas", respuesta[0]['languages'])