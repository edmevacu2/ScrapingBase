import requests

# Haciendo la solicitud
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# Se muestra el estado de la solicitud
# para solicitudes exitosas el codigo es 200
print(r)

# imprime el contenido de la solicitud
print(r.content)
