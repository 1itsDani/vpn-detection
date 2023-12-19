import requests

API_KEY = 'API_HERE'  # Replace with your actual API key

def is_vpn(ip, api_key):
    try:
        url = f'https://vpnapi.io/api/{ip}?key={api_key}'
        response = requests.get(url)
        data = response.json()
        
        security_info = data.get('security', {})
        return security_info.get('vpn', False)
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

try:
    ip = input('Enter the IP address: ')

    if is_vpn(ip, API_KEY):
        print('This is a VPN IP')
    else:
        print('This is not a VPN IP')

except Exception as e:
    print(f"An error occurred: {e}")

input('Press Enter to exit')
