import allure
import requests


class CompanyApi:
    def __init__(self, url: str) -> None:
        self.url = url

    @allure.step('Get authorization token by API')
    def get_token(self, user: str = "flora",
                  password: str = "nature-fairy") -> str:
        '''
        Get authorization token
        '''
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(f'{self.url}/auth/login', json=creds)
        token = resp.json()["userToken"]
        return token