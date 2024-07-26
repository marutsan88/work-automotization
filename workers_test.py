import requests
from workers_Api import workersApi

api = workersApi("https://x-clients-be.onrender.com")

def test_add_new_employee():
      #Создать новую компанию
    name = "SunWay"
    descr = "средства для загара"
    result = api.create_company(name, descr)
    new_id = result["id"]
    #Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    # получить список сотрудников 
    body = api.get_employees_list(companyId)
    len_before = len(body)
     # добавить нового сотрудника
    firstName = "Марина"
    lastName = "Карпова"
    middleName = "Алексеевна"
    company = companyId
    email = "sun-zagar777@mail.ru"
    url = "string"
    phone = "865423175266"
    birthdate = "2000-02-08"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании 
    body = api.get_employees_list(companyId)
    len_after = len(body)
    assert len_after - len_before == 1
    assert body[-1]["firstName"] == "Марина"
    assert body[-1]["lastName"] == "Карпова"
    assert body[-1]["middleName"] == "Алексеевна"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] == "865423175266"
    assert body[-1]["birthdate"] == "2000-02-08"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_get_employees_id():
    #Создать новую компанию
    name = "ООО Эктлетика Гид"
    descr = "Гид по городу Санкт-Петербург"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    #Обращаемся к компании по ID
    new_company = api.get_company(new_id)
    companyId = new_company['id']
    # получить список сотрудников новой компании до....
    body = api.get_employees_list(companyId)
    begin_list = len(body)
    # добавить нового сотрудника
    firstName = "Пётр"
    lastName = "Мидеев"
    middleName = "Сергеевич"
    company = companyId
    email = "midew346@mail.ru"
    url = "string"
    phone = "865837387609"
    birthdate = "1980-03-03"
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate,isActive=1)
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании 
    body = api.get_employees_list(companyId)
    after_list = len(body)
    assert after_list - begin_list == 1
    #Обращаемся к сотруднику по ID
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    assert body[-1]["firstName"] == "Пётр"
    assert body[-1]["lastName"] ==  "Мидеев"
    assert body[-1]["middleName"] == "Сергеевич"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] ==  "865837387609"
    assert body[-1]["birthdate"] == "1980-03-03"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_patch_employee():
    #Создать новую компанию
    name = "ИП Егоров"
    descr = "Ремонт грузовиков"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    #Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    # добавить нового сотрудника
    firstName = "Артём"
    lastName = "Егоров"
    middleName = "Артёмович"
    company = companyId
    email = "gruz-rem@mail.ru"
    url = "string"
    phone = "86564567877"
    birthdate = "2001-05-06"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании после....
    body = api.get_employees_list(companyId)
    #Обращаемся к сотруднику по ID
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    # Изменить информацию по сотруднику
    new_lastName = "Марков"
    new_email = "sana-x@mail.ru"
    new_url = "_Updated_"
    new_phone = "Updated"
    new_isActive = False
    edited = api.edit_employee(employee_id, new_lastName, new_email, new_url, new_phone, new_isActive)
    assert edited["email"] == "sana-x@mail.ru"
    assert edited["url"] == "_Updated_"
    assert edited["isActive"] == False

def test_delete_employee():
    #Создать новую компанию
    name = "ООО МТ эксклюзив"
    descr = "производство оконных рам"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    #Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    # добавить нового сотрудника
    firstName = "Ольга"
    lastName = "Перова"
    middleName = "Викторовна"
    company = companyId
    email = "perova-ol235@mail.ru"
    url = "string"
    phone = "865422377865"
    birthdate = "1980-05-06"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    # удалить сотрудника
    del_emp = api.delete_employee(emp_id)

    # Проверить, что сотрудник был удален
    assert del_emp is not None, "Сотрудник не был удален"
