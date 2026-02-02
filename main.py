import requests as consulta

#https://restcountries.com



name = input("Introduce el País en Ingles:")
response = consulta.get(f'https://restcountries.com/v3.1/name/{name}')
respuesta = response.json()

if response.status_code == 200:
    print("Nombre del pais: ",respuesta[0]['name'])
    print("Moneda: ", respuesta[0]['currencies'])
    print("Capital", respuesta[0]['capital'])
    print("Lenguas", respuesta[0]['languages'])

elif response.status_code >= 400:
    print(f"Error, no se encontró el país {name}, Código: {response.status_code}")