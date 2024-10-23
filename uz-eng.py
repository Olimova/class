lugat = {
    "salom": "hello",
    "kitob": "book",
    "maktab": "school",
    "work":"ish",
    "world":"dunyo",
    "good":"yaxshi",
    "bed":"yomon",
    "sleep":"uyqu",
    "kitchen":"oshxona",
    "morning":"ertalab",
    "day":"kun"
}
def qidirish(til, soz):
    if til == "uz":
        return lugat.get(soz, "So'z topilmadi.")
    elif til == "eng":
        for uzbekcha, inglizcha in lugat.items():
            if inglizcha == soz:
                return uzbekcha
        return "Bunday so'z lug'atda yoq."
    else:
        return "Noto'g'ri til kiritildi."

def yangi_soz(uzbekcha, inglizcha):
    if uzbekcha in lugat:
        return "Bu so'z allaqachon lug'atda mavjud."
    lugat[uzbekcha] = inglizcha
    return "So'z muvaffaqiyatli qo'shildi."

def ozgartirish(uzbekcha, yangi_inglizcha):
    if uzbekcha in lugat:
        lugat[uzbekcha] = yangi_inglizcha
        return "So'z muvaffaqiyatli o'zgartirildi."
    else:
        return "So'z lug'atda topilmadi."

def ochirish(uzbekcha):
    if uzbekcha in lugat:
        del lugat[uzbekcha]
        return "So'z muvaffaqiyatli o'chirildi."
    else:
        return "So'z lug'atda topilmadi."

def menyu():
    while True:
        print("\nLug'at dasturi")
        print("1. Qidirish (Uz->Eng yoki Eng->Uz)")
        print("2. Yangi so'z qo'shish")
        print("3. So'zni o'zgartirish")
        print("4. So'zni o'chirish")
        print("5. Dasturdan chiqish")

        tanlov = input("Tanlovingiz: ")

        if tanlov == "1":
            til = input("Qaysi tilda qidirish (uz/eng): ").lower()
            soz = input("So'z kiriting: ").lower()
            print(qidirish(til, soz))

        elif tanlov == "2":
            uzbekcha = input("O'zbekcha so'z kiriting: ").lower()
            inglizcha = input("Inglizcha tarjimasini kiriting: ").lower()
            print(yangi_soz(uzbekcha, inglizcha))

        elif tanlov == "3":
            uzbekcha = input("O'zgartirmoqchi bo'lgan O'zbekcha so'zni kiriting: ").lower()
            yangi_inglizcha = input("Yangi Inglizcha tarjimani kiriting: ").lower()
            print(ozgartirish(uzbekcha, yangi_inglizcha))

        elif tanlov == "4":
            uzbekcha = input("O'chirmoqchi bo'lgan O'zbekcha so'zni kiriting: ").lower()
            print(ochirish(uzbekcha))

        elif tanlov == "5":
            print("Dastur tugadi.")
            break

        else:
            print("Noto'g'ri tanlov, qayta urinib ko'ring.")

# Dastur ishga tushirilishi
if __name__ == "__main__":
    menyu()
