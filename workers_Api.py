import requests

class workersApi: 
    def __init__(self, url):
        self.url = url
        
    def create_company(self, name, description=""):
        company = {
            "name": name,
            "description": description
            }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company', json=company, headers=my_headers)
        return resp.json()

    def get_company(self, id):
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()

    def get_employee(self,id):
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json() 

    def get_employees_list(self,companyId):
        params = {'company': companyId}
        resp = requests.get(self.url + '/employee', params=params)
        return resp.json()

    def get_token(self, user = 'bloom', password = 'fire-fairy'):
        creds = {
           'username': user,
           'password': password
           }
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()['userToken'] 

    def create_employee(self, firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive):
        employee = {
            "firstName": firstName,
            "lastName": lastName,
            "middleName": middleName,
            "companyId": companyId,
            "email": email,
            "url": url,
            "phone": phone,
            "birthdate": birthdate,
            "isActive": isActive
            }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee', json=employee, headers=my_headers)
        return resp.json()

    def edit_employee(self, id, new_lastName, new_email, new_url, new_phone, new_isActive):
        employee = {
           "lastName": new_lastName,
           "email": new_email,
           "url":  new_url,
           "phone": new_phone,
           "isActive": new_isActive
           }
        my_headers = {"x-client-token": self.get_token()} 
        resp = requests.patch(self.url + '/employee/' + str(id), headers=my_headers, json=employee)
        return resp.json()

    def delete_employee(self, id):
        employee = {
           "id": id
           }
        my_headers = {"x-client-token": self.get_token()} 
        resp = requests.delete(self.url + f'/employee/{id}', headers=my_headers)
        return resp.json()


        