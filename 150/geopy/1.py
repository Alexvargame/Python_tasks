
from geopy.geocoders import Nominatim
from geopy import distance

geolocator = Nominatim(user_agent="geoapiExercises")
ladd1 ="27488 Stanford Avenue, North Dakota"
print("Location address:",ladd1)
location = geolocator.geocode(ladd1)
print("Street address, street name: ")
print(location.address)
ladd2 ="380 New York St, Redlands, CA 92373"
print("\nLocation address:",ladd2)
location = geolocator.geocode(ladd2)
print("Street address, street name: ")
print(location.address)


london = ("51.5074° N, 0.1278° W")
newyork = ("40.7128° N, 74.0060° W")
print("Distance between London and New York city (in km):")
print(distance.distance(london, newyork).km," kms")

geolocator = Nominatim(user_agent="geoapiExercises")
state1 ="Uttar Pradesh"
print("State Name:",state1)
location = geolocator.geocode(state1)
print("State Name/Country Name: ")
print(location.address)
state2 =" Illinois"
print("\nState Name:",state2)
location = geolocator.geocode(state2)
print("State Name/Country Name: ")
print(location.address)
state3 ="Normandy"
print("\nState Name:",state3)
location = geolocator.geocode(state3)
print("State Name/Country Name: ")
print(location.address) 
state4 ="Jerusalem District"
print("\nState Name:",state4)
location = geolocator.geocode(state4)
print("State Name/Country Name: ")
print(location.address)


geolocator = Nominatim(user_agent="geoapiExercises")
def city_state_country(coord):
    location = geolocator.reverse(coord, exactly_one=True)
    address = location.raw['address']
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    return city, state, country
print(city_state_country("50, 36.1"))


geolocator = Nominatim(user_agent="geoapiExercises")
lald ="47.470706, -99.704723"
print("Latitude and Longitude:",lald)
location = geolocator.geocode(lald)
print("Location address of the said Latitude and Longitude:")
print(location)
lald ="34.05728435, -117.194132331602"
print("\nLatitude and Longitude:",lald)
location = geolocator.geocode(lald)
print("Location address of the said Latitude and Longitude:")
print(location)
lald ="38.8976998, -77.0365534886228"
print("\nLatitude and Longitude:",lald)
location = geolocator.geocode(lald)
print("Location address of the said Latitude and Longitude:")
print(location)
lald ="55.7558° N, 37.6173° E"
print("\nLatitude and Longitude:",lald)
location = geolocator.geocode(lald)
print("Location address of the said Latitude and Longitude:")
print(location)
lald ="35.6762° N, 139.6503° E"
print("\nLatitude and Longitude:",lald)
location = geolocator.geocode(lald)
print("Location address of the said Latitude and Longitude:")
print(location)
lald ="41.9185° N, 45.4777° E"
print("\nLatitude and Longitude:",lald)
location = geolocator.geocode(lald)
print("Location address of the said Latitude and Longitude:")
print(location)
