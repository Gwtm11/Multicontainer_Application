from flask import session
import requests
import os


class UserClient:

    @staticmethod
    def get_user(api_key):
        headers = {
            'Authorization': api_key
        }

        response = requests.request(method="GET", url='http://'+os.getenv('USER_SERVICE') +'/api/user', headers=headers)
        if response.status_code == 401:
            return False

        user = response.json()
        return user
