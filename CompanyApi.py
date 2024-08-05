import requests

class CompanyApi:
    """Класс предоставляет методы для работы с сервером приложения"""

    def __init__(self, url):
        self.url = url


    # API.Получить список компаний через API
    def get_company_list(self, params_to_add=None):
        resp = requests.get(self.url + '/company', params=params_to_add)
        return resp.json()

    # API.Получить токен авторизации для авторизации 
    def get_token(self, user='bloom', password='fire-fairy'):
        """
        Получить токен авторизации
        :params user(str): логин пользователя
        :params password(str): пароль пользователя

        :return: str: token
        """
        creds = {
            "username": user,
            "password": password
            }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]

    # API.Получить организацию по {id}
    def get_company(self, id):
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()

    # API.Создать новую организацию 
    def create_company(self, name, description=""):
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company', json=company, headers=my_headers)
        return resp.json()

    # API.Редактировать организацию id,name,descr
    def edit(self, new_id, new_name, new_descr):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        company = {
            "name": new_name,
            "description": new_descr
        }
        resp = requests.patch(self.url + '/company/' + str(new_id), headers=my_headers, json=company)
        return resp.json()

    # API.Удалить организацию по {id}
    def delete(self, id):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.get(self.url + '/company/delete/' + str(id), headers=my_headers)
        return resp.json()

    # API.(Де)активировать организацию {id} -> {isActive}")
    def set_active_state(self, id, isActive):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url + '/company/status/' + str(id), headers=my_headers, json={"isActive": isActive})
        return resp.json()

    # API.Получить список сотрудников в организации {companyId}")
    def get_empl_list(self,companyId):
        params = {'company': companyId}
        resp = requests.get(self.url + '/employee', params=params)
        return resp.json()
