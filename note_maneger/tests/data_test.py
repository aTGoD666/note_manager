from progekt.note_maneger.data.create_note_function import create_note
from progekt.note_maneger.data.display_notes_function import display_notes
from progekt.note_maneger.data.update_note_function import update_note
from progekt.note_maneger.data.delete_note import delete_note
from progekt.note_maneger.data.search_notes_function import search_notes
from progekt.note_maneger.data.append_notes_to_file import append_notes_to_file
from progekt.note_maneger.data.save_notes_to_file import save_notes_to_file
from progekt.note_maneger.data.save_notes_json import append_notes_json




all_info = []
filename = 'test2.txt'


print("Добро пожаловать в 'Менеджер заметок! TEST'")
print("---------------------------------------------")
print("1: Создать новую заметку")
print("2: Показать все заметки")
print("3: Обновить заметку")
print("4: Удалить заметку")
print("5: Найти заметки")
print("6: Записать заметки.")
print("7: Записать заметки заново.")
print("6: Записать заметки json.")
print("8: Выйти из программы.")
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
    if choice == 4:
        delete_note(all_info) # функция удаления заметок
        continue
    if choice == 5:
        search_notes(all_info) # функция нахождения заметок
        continue
    if choice == 6:
        append_notes_to_file(all_info,filename)
        continue
    if choice == 7:
        save_notes_to_file(all_info,filename)
        continue
    if choice == 8:
        filename = 'testj.txt'
        append_notes_json(all_info,filename)
        filename = 'test2.txt'
        continue
    if choice == 9:
        print("Спасибо что использовали наш менеджер заметок!")
        break
    else:
        print("Введен не корректный код действия")
    continue








print(all_info)