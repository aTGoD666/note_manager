from datetime import datetime

def save_notes_to_file(): # - функция записи заметки в файл формата txt
    notes = open('notes.txt', 'w', encoding='utf-8') # - открытие файла для написания текста с деодирование под кирилицу

    all_info = []
    d_format = "%d-%m-%y"  # - формат дат заметки
    d_format2 = "%y-%m-%d"  # - формат дат 2
    status_zam = ["Новая"]  # - статус заметки
    status_txt = ["Выполнено", "В процессе", "Отложено"]  # - статусы
    zametka = "да"  # - значение для определения цикла
    zametka_nomber = 0  # - счетчик заметок
    out = False

    print("Вы можете добавить новую заметку!")

    while not out:
        if zametka in ["да"]:
            username = input("Имя: ")  # имя пользователя
            title = input("Заголовок темы: ")  # заголовок
            title2 = input("Заголовок урока: ")  # заголовок
            title3 = input("Заголовок задания: ")  # заголовок
            title_all = [title, title2, title3]  # заголовок
            print(F"Текущий статус заметки: {status_zam}")

            tvist = input("Изменить? (да/нет): ").lower()

            # - цикл для определения нужно ли менять статус

            while True:
                if tvist not in ["да", "нет"]:
                    print("Это неверное значение введите знаечение корректно")
                    tvist = input("Изменить? (да/нет): ").lower()
                    continue
                else:
                    if tvist == "нет":
                        print("Текущий статус остался")
                        print(status_zam)
                        break
                    else:

                        # - цикл для установки нового статуса
                        while True:
                            print("Выбирите новый статус заметки")
                            print(" 1 - Выполнено"
                                  " 2 - В процессе"
                                  " 3 - Отложено")
                            status_int = int(input("Висите код статуса: "))

                            if status_int in [1, 2, 3]:
                                print("Статус изменени на:")
                                print(status_txt[status_int - 1])
                                status_zam = [status_txt[status_int - 1]]
                                break
                        else:
                            print("Введен неверный код")
                        break

            content = input("Описание: ")  # описание заметки

            # дата создание заметки (формат дд-мм-гг и гг-мм-дд)

            while True:
                try:
                    created_date = datetime.strptime(input("Дата создания (дд-мм-гг): "), d_format)
                    print("Дата успешно введена:", created_date.strftime(d_format))
                    break
                except ValueError:
                    print("Неверный формат даты. Попробуйте снова.")

                try:
                    created_date = datetime.strptime(input("Дата создания (гг-мм-дд): "), d_format2)
                    print("Дата успешно введена:", created_date.strftime(d_format2))
                    break
                except ValueError:
                    print("Неверный формат даты. Попробуйте снова.")

            # дата истечения заметки (формат дд-мм-гг и гг-мм-дд)

            while True:
                try:
                    issue_date = datetime.strptime(input("Дата дэдлайна (дд-мм-гг): "), d_format)
                    print("Дата успешно введена:", issue_date.strftime(d_format))
                    break
                except ValueError:
                    print("Неверный формат даты. Попробуйте снова.")

                try:
                    issue_date = datetime.strptime(input("Дата дэдлайна (гг-мм-дд): "), d_format2)
                    print("Дата успешно введена:", issue_date.strftime(d_format2))
                    break
                except ValueError:
                    print("Неверный формат даты. Попробуйте снова.")

            zametka = input("Хотите добавить еще одну заметку? (Да/Нет): ").lower()

            while True:
                if zametka not in ["да", "нет"]:
                    print("Это неверное значение введите значение корректно")
                    zametka = input("Хотите добавить еще одну заметку? (Да/Нет): ").lower()
                    continue
                elif zametka == "да":
                    zametka_nomber = (zametka_nomber + 1)
                    print(F"Заметка № {zametka_nomber}")
                    print("Заметка успешно создана!!!")
                    all_infodick = {"Заметка № ": zametka_nomber,
                                    "имя": username,
                                    "описание": content,
                                    "статус": status_zam,
                                    "создание заметки": created_date,
                                    "дедлайн": issue_date,
                                    "заголовок": title_all}
                    all_info.append(all_infodick)
                    status_zam = ["Новая"]  # - перезаписываем переменную статуса на исходную
                    break
                else:
                    if zametka == "нет":
                        zametka_nomber = (zametka_nomber + 1)
                        print(F"Заметка № {zametka_nomber}")
                        print("Заметка успешно создана!!!")
                        all_infodick = {"Заметка № ": zametka_nomber,
                                        "имя": username,
                                        "описание": content,
                                        "статус": status_zam,
                                        "дата создания": created_date,
                                        "дедлайн": issue_date,
                                        "заголовок": title_all}
                        all_info.append(all_infodick)
                        status_zam = ["Новая"]  # - перезаписываем переменную статуса на исходную
                        out = True
                        break

    # - цикл для разложеиня заметки по ключам и написания заметки через строчку
    for idx, note in enumerate(all_info):
        for i, j in note.items():
            notes.write(f"{i}: {j}\n")
        if idx < len(all_info) - 1:
            notes.write("\n")


    # - закрытия файла txt
    notes.close()
    return all_info
# save_notes_to_file()  # - вызов функций для теста

