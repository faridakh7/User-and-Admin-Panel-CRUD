import json


def getDataFormJsonFile(_fileName):
    with open(_fileName, "r") as connect:
        return json.load(connect)

data = getDataFormJsonFile("db.json")


def userLogin():
    finder=False
    print("daxil edin:")
    _email= input("Email: ")
    _password= input("Password: ")

    for db in data['students']:
        if db['email']==_email and db['password']==_password:
            finder=True
            def userSearch():
                searchInput=int(input("""
            1. Öz məlumatlarının əldə olunması
            2. Digər tələbələrin məlumatlarının əldə olunması
                Secminizi Daxil edin:  
                """))
                if searchInput==1:
                    print(f"ID: {db['id']} \nName: {db['name']} \nSurname: {db['surname']} \nEmail: {db['email']} \nPassword: {db['password']}")
                    userSearch()
                if searchInput==2:
                    for alldata in data['students']:
                        print(f"ID: {alldata['id']} \nName: {alldata['name']} \nSurname: {alldata['surname']} \nEmail: {alldata['email']} \n")
                    userSearch()

            userSearch()
            break
    if finder==False:
        print("Sehvdir")
        userLogin()


