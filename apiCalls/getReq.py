import requests
import json

# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# headers = {'content-type': 'application/json'}

resp=requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
status=resp.status_code
print("Response text: ", resp.text)

# extracting data in json format
print("Response json: ", resp.json())
print(status)

# requests.post('https://httpbin.org/post', json={'key1':'value1','key2':'value2'})
# requests.put('https://httpbin.org/put', data={'key':'value'})
# requests.delete('https://httpbin.org/delete')
# requests.head('https://httpbin.org/get')
# requests.patch('https://httpbin.org/patch', data={'key':'value'})
# requests.options('https://httpbin.org/get')
