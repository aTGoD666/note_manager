from datetime import datetime
from create_note_function import create_note
from display_notes_function import display_notes
from update_note_function import update_note
from delete_note import delete_note
from search_notes_function import search_notes

all_info = []
print("Добро пожаловать в 'Менеджер заметок!'")
print("---------------------------------------------")
print("1: Создать новую заметку")
print("2: Показать все заметки")
print("3: Обновить заметку")
print("4: Удалить заметку")
print("5: Найти заметки")
print("6: Выйти из программы.")
while True:
    print("---------------------------------------------")
    choice = int(input("Введите код действия!: "))
    if choice == 1:
        create_note(all_info) # функция создания заметки
        continue
    if choice == 2:
        display_notes(all_info) # функция отображение заметок
        continue
    if choice == 3:
        update_note(all_info) # функция обновления заметок
        continue
    if choice ==4:
        delete_note(all_info) # функция удаления заметок
        continue
    if choice == 5:
        search_notes(all_info) # функция нахождения заметок
        continue
    if choice == 6:
        print("Спасибо что использовали наш 'менеджер заметок!'")
        break
    else:
        print("Введен не корректный код действия")
    continue
