data = {}

def check_condition(type, value, value2=0, data = data):
    if type == "nisn":
        if not value.isnumeric() or not len(value) == 6:
            print("\nNISN does not match the format, NISN only has numbers with a length of 6 digits!!")
            return False
        else:
            return int(value)

    elif type == "name":
        if not all([x.isalpha() or x == ' ' for x in value]):
            print("\nNames are only allowed in letters")
            return False
        else:
            return True

    elif type == "lesson":
        if not value.isnumeric() or int(value) not in range(0,101):
            print("\nValue is only a number 0-100")
            return False
        else:
            return True

    elif type == "menu":
        i = input(value)
        if not i.isnumeric():
            print(f"\nEnter only numbers 1 to {value2}")
            return False
        elif not int(i) in range(1,value2+1):
            print(f"\nEnter the wrong menu, please select numbers 1 to {value2}")
            return False
        else:
            return int(i)

def text_menu(val):
    if val == "main_menu":
        return """
            ======= ACADEMIC SCORE =======
            1. SHOW REPORT
            2. CREATE DATA
            3. UPDATE DATA
            4. DELETE DATA
            5. EXIT
            ENTER OPTIONS (1-5): """

    elif val == "sm_read":
        return """
            ======= SUB MENU READ DATA =======
            1. READ ALL DATA
            2. SEARCH DATA
            3. EXIT
            ENTER OPTIONS (1-3): """
    
    elif val == "sm_create":
        return """
            ======= SUB MENU CREATE DATA =======
            1. INSERT DATA
            2. BACK TO MAIN MENU
            ENTER OPTIONS (1-2): """
    
    elif val == "sm_update":
        return """
            ======= SUB MENU UPDATE DATA =======
            1. UPDATE DATA
            2. BACK TO MAIN MENU
            ENTER OPTIONS (1-2): """
    
    elif val == "ssm_update":
        return """
            PLEASE SELECT THE DATA THAT WILL BE CHANGED
            1. NISN
            2. NAME
            3. IPA
            4. MATH
            5. BAHASA
            6. BACK TO SUB MENU
            ENTER OPTIONS (1-6): """
    
    elif val == "sm_delete":
        return """
            ======= SUB MENU READ DATA =======
            1. DELETE DATA
            2. EXIT
            ENTER OPTIONS (1-2): """

def menu1(data):
    while True:
        menu = check_condition("menu", text_menu("sm_read"), value2=3)

        if menu == 1:
            if not data:
                print("\nThere is no student data, please create data first")
            else:
                for nisn in data:
                    datas = data.get(nisn)
                    print(
                        f"""
                        ===============================
                        NISN : {nisn}
                        Name : {datas.get("name")}
                        IPA : {datas.get("ipa")}
                        Math : {datas.get("math")}
                        Bahasa : {datas.get("bahasa")}
                        Average : {datas.get("avg")}
                        ==============================="""
                    )

        elif menu == 2:
            if not data:
                print("\nThere is no student data, please create data first")
            else:
                nisn = input("\nInput NISN number to search for data: ")
                nisn = check_condition("nisn", nisn)
                if nisn in data:
                    read_single_data(nisn)
                else:
                    print("\nNISN number not found")

        elif menu == 3:
            break

def read_single_data(nisn, data = data):
    datas = data.get(nisn)
    print(
        f"""
        ==============================
        NISN : {nisn}
        Name : {datas.get("name")}
        IPA : {datas.get("ipa")}
        Math : {datas.get("math")}
        Bahasa : {datas.get("bahasa")}
        Average : {datas.get("avg")}
        =============================="""
    )



def menu2(data):
    while True:
        menu = check_condition("menu", text_menu("sm_create"), value2=2)
        if menu == 1:
            sub_menu2(data)
        elif menu == 2:
            break


def sub_menu2(data):
    while True:
        nisn = input("\nInput NISN: ")
        nisn = check_condition("nisn", nisn)

        if nisn in data:
            print("\nData already exists\n")
            break
        elif nisn:
            datas = {}
            while True:
                name = input("Input student name: ")
                if not check_condition("name", name):
                    continue
                ipa = input("Input the value of the science lesson: ")
                if not check_condition("lesson", ipa):
                    continue
                math = input("Input the value of the mathemathic lesson: ")
                if not check_condition("lesson", math):
                    continue
                bahasa = input("Input the value of the bahassa lesson: ")
                if not check_condition("lesson", bahasa):
                    continue
                
                datas = {
                    'name' : name.title(),
                    'ipa' : int(ipa),
                    'math' : int(math),
                    'bahasa' : int(bahasa),
                    'avg' : (int(ipa) + int(math) + int(bahasa)) / 3
                    }
                break
                
            
            while True:
                save = input("\nSave data?(y/n): ").lower()
                if save == 'y':
                    data[int(nisn)] = datas
                    print("\nData saved successfully!!!")
                    break
                elif save == 'n':
                    break
            break

def menu3(data):
    while True:
        menu = check_condition("menu", text_menu("sm_update"), value2=2)
        if menu == 1:
            sub_menu3(data)
        elif menu == 2:
            break

def sub_menu3(data):
    while True:
        nisn = input("\nInput NISN number of the data to be changed: ")
        nisn = check_condition("nisn", nisn)     
        if nisn in data:
            datas = data.get(nisn)
            while True:
                read_single_data(nisn)
                save = input("\nContinue editing data?(y/n): ").lower()

                if save == 'y':
                    while True:
                        menu = check_condition("menu", text_menu("ssm_update"), value2=6)
                        if menu == 1:
                            new_nisn = input("Input new NISN number: ")
                            if check_condition("nisn", new_nisn):
                                data[int(new_nisn)] = data.pop(nisn)
                                nisn = int(new_nisn)
                                print("\nData updated successfully")
                        elif menu == 2:
                            new_name = input("Input new Name: ")
                            if check_condition("name", new_name):
                                datas['name'] = new_name.title()
                                print("\nData updated successfully")
                        elif menu in range(3,6):
                            mapel = ["ipa", "math", "bahasa"]
                            new_value = input("Input new value: ")
                            if check_condition("lesson", new_value):
                                 datas[mapel[menu-3]] = int(new_value)
                                 datas['avg'] = (datas['ipa'] + datas['math'] + datas['bahasa'])/3
                                 print("\nData updated successfully")
                        elif menu == 6:
                            break                     
                elif save == 'n':
                    break

        else:
            print("\nThe data you are looking for does not exist")
        break

def menu4():
    while True:
        menu = check_condition("menu", text_menu("sm_delete"), value2=2)
        if menu == 1:
            sub_menu4()
        elif menu == 2:
            break

def sub_menu4(data = data):
    nisn = input("\nInput NISN number to be deleted: ")
    nisn = check_condition("nisn", nisn)
    if nisn in data:
        while True:
            read_single_data(nisn)
            delete = input("\nDo you want to continue to delete data?(y/n): ").lower()
            if delete == 'y':
                data.pop(nisn)
                break
            elif delete == 'n':
                break
    else:
        print("\nThe data you are looking for does not exist")

while True:
    option = check_condition("menu", text_menu("main_menu"), value2=5)

    if not option:
        continue
    elif option == 1:
        menu1(data)
    elif option == 2:
        menu2(data)
    elif option == 3:
       menu3(data)
    elif option == 4:
        menu4()
    elif option == 5:
        break
