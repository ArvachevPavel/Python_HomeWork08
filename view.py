def show_menu():
    print(f"Выберите действие: \n 1 - показать всех сотрудников"
          "\n 2 - добавить сотрудника"
          "\n 3 - удалить сотрудника"
          "\n 4 - Выход")
    select = int(input())
    return select

def add_menu():
    print (f"Введите фамилию, имя и номер телефона через пробел")
    person = input().split()
    return person

def delete_menu():
    print(f"Введите номер записи для её удаления")
    delete = int(input())
    return delete

def show_all(all):
    print("№\tФамилия\tИмя\tТелефон")
    for i, p in enumerate(all):
        print(i,*p, sep = "\t")
