import json


def getDataFormJsonFile(_fileName):
    with open(_fileName, "r") as connect:
        return json.load(connect)


data = getDataFormJsonFile("db.json")


def start():
    xususiEmr = input("""
    Aşağıdakı Əmrlərdən Birini Secin:

    1.Tələbə kimi daxil olun
    2.Admin kimi daxil olun
    3.Programı dayandırmaq

Seciminizi Daxil edin:  """).strip()
    if xususiEmr.isnumeric() and 0 < int(xususiEmr) < 7:
        option = int(xususiEmr)

        if option == 1:
            def userLogin():
                finder = False
                print("daxil edin:")
                _email = input("Email: ")
                _password = input("Password: ")

                for db in data['students']:
                    if db['email'] == _email and db['password'] == _password:
                        finder = True

                        def userSearch():
                            searchInput = int(input("""
                        1. Öz məlumatlarının əldə olunması
                        2. Digər tələbələrin məlumatlarının əldə olunması
                            Secminizi Daxil edin:  
                            """))
                            if searchInput == 1:
                                print(
                                    f"ID: {db['id']} \nName: {db['name']} \nSurname: {db['surname']} \nEmail: {db['email']} \nPassword: {db['password']}")
                                userSearch()
                            if searchInput == 2:
                                for alldata in data['students']:
                                    print(
                                        f"ID: {alldata['id']} \nName: {alldata['name']} \nSurname: {alldata['surname']} \nEmail: {alldata['email']} \n")
                                userSearch()

                        userSearch()
                        break
                if finder == False:
                    print("Sehvdir")
                    userLogin()
            userLogin()
        if option == 2:
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
                            if xususiemr == 3:
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
            adminLogin()

        if option == 3:
            def programbitdi():
                print("Program muveffeqiyyətlə dayandırıldı")
                return

            programbitdi()
    else:
        print("Yalnız 1-6 arası bir seçim edə bilərsiniz!")
        start()


start()
