import requests
from bs4 import BeautifulSoup

def login_to_portal(session, username, password, portal_url):
    try:
        response = session.get(portal_url)
        response.raise_for_status()  # Check if the request was successful
        print("HTML content:", response.text)  # Add this line to print HTML content to console

        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_input = soup.find('input', {'name': 'csrf_token'})

        if csrf_input:
            csrf_token = csrf_input['value']
            # rest of the function...
            return True
        else:
            print("CSRF token not found in HTML.")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Error during login: {e}")
        return False
