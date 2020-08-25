import json
import requests
import sys

query = input("Enter an IP or Domain name: ")
endpoint = f"http://ip-api.com/json/{query}"
if query == '':  #Conditia daca valoarea de la input lipseste
    print("Value error")
    sys.exit()   #Terminates the program immediatly
response = requests.get( endpoint )
data = json.loads( response.text )
status = data['status']
if status == 'fail':
    print("Value input non-exist\'s")
    sys.exit()
country = data['country']
city = data['city']
timezone = data['timezone']
lat = data['lat']
lon = data['lon']
ip = data['query']
value = -1
while value != 0:
    print( f"What information do you want to know?\n 1.Country and city > \n 2.Timezone > \n 3.Coordinates > \n 4.IP of domanin Name > \n 5.Exit ! ")
    value = int(input(""))
    if value == 1:
        print(f"The domain is located in {country} / {city}\n")
    if value == 2:
        print(f"The timezone is {timezone}\n")
    if value == 3:
        print(f"The coordinates > Lat: {lat} and Lon: {lon}\n")
    if value == 4:
        print(f"The IP of domain is {ip}\n")
    if value == 5:
        sys.exit()




