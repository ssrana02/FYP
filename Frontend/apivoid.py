import requests

api_key = 'c188212ff8aa99dfbe87964aa9293a603506bbc6'
url_to_check = 'https://example.com'

params = {
    'key': api_key,
    'url': url_to_check
}

url = 'https://endpoint/api/endpoint'
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    if data['blacklisted']:
        print('The URL is blacklisted.')
        print('Blacklist Reason:', data['blacklist_reason'])
    else:
        print('The URL is not blacklisted.')
else:
    print('Error:', response.status_code)
