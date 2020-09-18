from adminLog import adminLogin
from userLog import userLogin


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
            userLogin()
            start()
        if option == 2:
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
