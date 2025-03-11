import requests

uri = 'http://localhost:8080/iot/api/v1.0/things'

print(20 * '*' + ' GET all')
print(uri)

response = requests.get(uri)

print(20 * '*' + " Response:")
print(response.text)

input("it <enter> to continue...")
# ------------------------------------------------

print(20 * '*' + ' GET one')
print(uri + '/1')

response = requests.get(uri + '/1')

print(20 * '*' + " Response:")
print(response.text)

input("it <enter> to continue...")
# ------------------------------------------------

print(20 * '*' + ' POST')
print(uri)
data = {
    "local": "@lab. 163 / ISE /UAlg",
    "name": "Apollo",
    "sensors": [
        {
            "sensor_name": "temperature",
            "units": "numerical"
        },
        {
            "sensor_name": "humidity",
            "units": "percent"
        }
    ]
}
print("data:", data)

response = requests.post(uri, json=data)
print(20 * '*' + " Response:")
print(response.text)

input("it <enter> to continue...")
# ------------------------------------------------

print(20 * '*' + ' PUT')
print(uri + '/3')
print("data:", {"name": "Apollo X1"})
response = requests.put(uri + '/3',
                        json={"name": "Apollo X1"})

print(20 * '*' + " Response:")
print(response.text)

print(20 * '*' + ' GET  ALL (after put)')
response = requests.get(uri)
print(response.text)

input("it <enter> to continue...")
# ------------------------------------------------

print(20 * '*' + ' DELETE')
print(uri + '/3')
response = requests.delete(uri + '/3')
print(response.text)


print(20 * '*' + ' GET  ALL (after delete)')
response = requests.get(uri)
print(response.text)
