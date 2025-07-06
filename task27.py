def phonebook_menu(phonebook: dict[str, str]) -> None:
    while True:
        print("1: Kontakt qo'shish (`ism → telefon")
        print("2: Barcha kontaktlarni chiqarish")
        print("3: Ism bo‘yicha telefon qidirish")
        print("4. Output")
        tanlov = int(input("tanlov = "))
        if  1 <= tanlov <= 4:    
            
         if tanlov == 1 :
            name = input("ism kiriting : ")
            phone_number = input("phone_number : ")
            phonebook[name] = phone_number
            phonebook.update({name:phone_number})
            
         elif tanlov == 2 :
            if phonebook:
                print("kontaktlar ro'yxati")
                for name,phone_number in phonebook.items():
                    print(f"{name}:{phone_number}")
            else:
                print("phone_number mavjud emas")
                
         elif tanlov == 3:
            name_search = input("qidirayotgan ismingizni kiriting : ")
            if name_search in phonebook:
                print(f"{name_search} ning raqami = {phonebook[name]}")
            else:
                print("bunaqa ismdagi kontakt qo'shilmagan")
                
         elif tanlov == 4 :
                   print(' Dastur yakunlandi siz bn ishlaganimdan xursandman.') 
                   break
        else:
            print("Iltimos tanlovni qaytadan amalga oshiring")      
            
phonebook = {}

phonebook_menu(phonebook)
