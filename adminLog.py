import json


def getDataFormJsonFile(_fileName):
    with open(_fileName, "r") as connect:
        return json.load(connect)


data = getDataFormJsonFile("db.json")


def adminLogin():
    finder = False
    print("daxil edin:")
    _email = input("Email: ")
    _password = input("Password: ")

    for db in data['admins']:
        if db['email'] == _email and db['password'] == _password:
            finder = True

            def emr():
                xususiemr = int(input("""
                       1. Tələbə əlavə etmək
                       2. Tələbə məlumatlarının dəyişdirilməsi
                       3. Tələbə databasedən silinməsi
                           Secminizi Daxil edin:  
                           """))
                if xususiemr == 1:
                    def addNewData():
                        _id = int(input("ID daxil edin: "))
                        _name = input("Ad daxil edin: ")
                        _surname = input("Soyad daxil edin: ")
                        _email = input("Email daxil edin: ")
                        _password = input("Password daxil edin: ")


                        new_students = {
                            "id": _id,
                            "name": _name,
                            "surname": _surname,
                            "email": _email,
                            "password": _password

                        }
                        data['students'].append(new_students)
                        with open("db.json", "w") as connect:
                            json.dump(data, connect)
                            print("Qeyd etdiyiniz parametrlər databaseyə daxil əlavə olundu!")
                    addNewData()
                if xususiemr == 2:
                    def updateDataFromId():
                        _id = int(input("ID daxil edin: "))
                        _name = input("Ad daxil edin: ")
                        _surname = input("Soyad daxil edin: ")
                        _email = input("Email daxil edin: ")
                        _password = input("Password daxil edin: ")

                        for stu in data['students']:
                            if stu['id'] == _id:
                                stu['name'] = _name
                                stu['surname'] = _surname
                                stu['email'] = _email
                                stu['password'] = _password

                        with open("db.json", "w") as connect:
                            json.dump(data, connect)
                            print(f"ID-si {_id} olan datanın məlumatları müvəffəqiyyətlə yeniləndi!")
                    updateDataFromId()
                if xususiemr ==3:
                    def delProductbyName():
                        _id = int(input("ID daxil edin: "))
                        finder = False
                        for stu in data['students']:
                            if stu['id'] == _id:
                                data['students'].pop(data['students'].index(stu))
                                finder = True
                                print(f"{_id} -Nömrəli ID databaseden silindi")
                                break
                        with open("db.json", "w") as connect:
                            json.dump(data, connect)
                        if finder == False:
                            print(f"{_id} -Nömrəli ID tapılmadi")
                            delProductbyName()
                    delProductbyName()
            emr()
            break
    if finder == False:
        print("Sehvdir")
        adminLogin()

