from datetime import datetime


def search_notes(all_info):  # - Функция поиска

    keyword = ""  # - Значение поиска
    status = ""  # - Значение поиска статуса

    # - Ввод значений
    keyword =  input("Введите значение для поиска!: ")
    status =  input("Введите статус для поиска!: ")

    # - Условие проверки статуса
    notes_with_status = [note for note in all_info if status in note['статус']]

    # - определение найденный заметки по статусу
    if not notes_with_status:
        print(f"В списке нет заметок со статусом '{status}'.")
    else:
        print("Заметки с указанным статусом:")

        # - отображение найденой заметки
        for note in notes_with_status:
            print("------------------------")
            for i, j in note.items():
                print(f"{i}: {j}")

    # - Проверка на пустое значение поля
    if not keyword.strip():
        print("Ключевое значение не указано. Поиск по ключевому слову пропущен.")
        return

    # - Условие проверки значения
    notes_with_keyword = [
        note for note in all_info
        if keyword in note.get('описание', '') or
           any(keyword in title for title in note.get('заголовок', [])) or
           keyword in note.get('имя', '')]

    # - определение найденный заметки по значению
    if not notes_with_keyword:
        print(f"В списке нет заметок со значением '{keyword}'.")
    else:
        print("Заметки с указанным значением:")

        # - отображение найденой заметки
        for note in notes_with_keyword:
            print("------------------------")
            for i, j in note.items():
                print(f"{i}: {j}")
    return all_info
