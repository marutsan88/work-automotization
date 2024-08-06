import requests

from CompanyApi import CompanyApi


class EmployeeApi:
    def __init__(self, url):
        self.url = url

    def add_employee(self, id, first_name, last_name, middle_name, company_id,
                     email, employee_url, phone, birthdate, is_active):
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

    def get_employee(self, employee_id):
        resp = requests.get(f'{self.url}/employee/{employee_id}')
        return resp.json()

    def get_employee_list(self, company_id):
        resp = requests.get(f'{self.url}/employee?company={company_id}')
        return resp.json()

    def patch_employee(self, employee_id, new_email, new_url,
                       new_is_active):
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