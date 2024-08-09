import allure
import requests

from CompanyApi import CompanyApi


class EmployeeApi:
    def __init__(self, url: str) -> None:
        self.url = url

    @allure.step('Add new employee by API')
    def add_employee(self, id: int, first_name: str, last_name: str,
                     middle_name: str, company_id: int,
                     email: str, employee_url: str, phone: str,
                     birthdate: str, is_active: bool) -> dict:
        '''
        Add new employee
        '''
        company_api = CompanyApi(self.url)
        token = company_api.get_token("flora", "nature-fairy")
        my_headers = {}
        my_headers["x-client-token"] = token
        body = {
            "id": id,
            "firstName": first_name,
            "lastName": last_name,
            "middleName": middle_name,
            "companyId": company_id,
            "email": email,
            "url": employee_url,
            "phone": phone,
            "birthdate": birthdate,
            "isActive": is_active
        }
        resp = requests.post(f'{self.url}/employee', json=body,
                             headers=my_headers)
        return resp.json()

    @allure.step('Get employee by id by API')
    def get_employee(self, employee_id: int) -> dict:
        '''
        Get employee by id
        '''
        resp = requests.get(f'{self.url}/employee/{employee_id}')
        return resp.json()

    @allure.step('Get employees list by API')
    def get_employee_list(self, company_id: int) -> dict:
        '''
        Get company's employees list
        '''
        resp = requests.get(f'{self.url}/employee?company={company_id}')
        return resp.json()

    @allure.step('Patch employee by API')
    def patch_employee(self, employee_id: int, new_email: str, new_url: str,
                       new_is_active: bool) -> dict:
        '''
        Patch employee
        '''
        company_api = CompanyApi(self.url)
        token = company_api.get_token("flora", "nature-fairy")
        my_headers = {}
        my_headers["x-client-token"] = token
        body = {
            "email": new_email,
            "url": new_url,
            "isActive": new_is_active
        }
        resp = requests.patch(f'{self.url}/employee/{employee_id}', json=body,
                              headers=my_headers)
        return resp.json()