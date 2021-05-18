import requests
import json

# url = 'https://api.github.com/some/endpoint'
# url2="https://pokeapi.co/api/v2/pokemon/ditto"
# payload = {'some': 'data'}
# headers = {'content-type': 'application/json'}
url1="https://reqres.in/"
param={"page":2}
resp=requests.get(url1+"api/users?",params=param) #use "params" to use query parameters to url
status=resp.status_code
assert status==200,"Assertion failed"
print("Response text: ", resp.text)  #plain json response

# extracting data in json format
print("Response json: ", resp.json())  #json response captured in python dictionary/list
print(status)

payload={"name": "sumit","job": "QA"}
resp2=requests.post(url1+"api/users", json=payload, headers={'content-type':'application/json'},)
print(resp2.status_code)
print("resp2:", resp2.json())

patch_payload={"name": "morpheus", "job": "zion resident"}
resp3=requests.patch(url1+"api/users/2", json=patch_payload)
print(resp3.status_code)
print(resp3.json())
print("updated name: ", resp3.json()['name'])

resp4=requests.delete(url1+"api/users/2")
print(resp4.status_code)

# requests.post('https://httpbin.org/post', json={'key1':'value1','key2':'value2'})
# requests.put('https://httpbin.org/put', data={'key':'value'})
# requests.delete('https://httpbin.org/delete')
# requests.head('https://httpbin.org/get')
# requests.patch('https://httpbin.org/patch', data={'key':'value'})
# requests.options('https://httpbin.org/get')
