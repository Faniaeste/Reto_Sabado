import requests as consulta

#https://restcountries.com

response = consulta.get('https://restcountries.com/v3.1/name/spain')
respuesta = response.json()
print("Nombre del pais: ",respuesta[0]['name'])