# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа - пустая строка)

people = {
    1: {"name": "alex", "surname": "smirnov", "phone_number": "2443234", "e-mail": "dfdfdfd@mail.com"},
    2: {"name": "sergei", "surname": "ivanov", "phone_number": "3434322", "e-mail": ""},
    3: {"name": "elena", "surname": "kazakova", "phone_number": "434343433", "": "ssdsfdf@mail.com"}
}

def dict_of_dicts(people):
    users_without_email = []
    for user_id, user_data in people.items():
        if "e-mail" not in user_data or user_data["e-mail"] == "":
            users_without_email.append(user_data["name"])
    return users_without_email


result = dict_of_dicts(people)
print("Users without e-mail!")
for name in result:
    print(name)
