from view import *
from model import *

def main():
    while True:
        select = show_menu()
        if select == 1:
            all = get_all()
            show_all(all)
        elif select == 2:
            person = add_menu()
            add(person)
            show_result("Запись добавлена")
        elif select == 3:
            number = delete_menu()
            delete(number)
            show_result("Запись удалена")
        elif select == 4:
            show_result("Здоровья и процветания! До свидания!!!")
            break

def show_result(msg):
    print(msg)
    