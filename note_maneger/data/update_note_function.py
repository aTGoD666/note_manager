from datetime import datetime



# Исходные данные
# all_info = [{'Заметка № ': 1,
#              'имя': 'паша',
#              'описание': 'Нужно создать словарь для теста удаления',
#              'статус': ['Новая'],
#              'дата создания': datetime(2024, 12, 27, 0, 0),
#              'дедлайн': datetime(2024, 12, 27, 0, 0),
#              'заголовок': ['обучение коду', 'вводный урок', 'простой код']},
#             {'Заметка № ': 2,
#              'имя': 'вова',
#              'описание': 'ор',
#              'статус': ['Новая'],
#              'дата создания': datetime(2024, 12, 26, 0, 0),
#              'дедлайн': datetime(2024, 12, 27, 0, 0),
#              'заголовок': ['вторая заметка', 'тот же', 'тот же']},
#             {'Заметка № ': 3,
#              'имя': 'коля',
#              'описание': 'кака бубу',
#              'статус': ['Новая'],
#              'дата создания': datetime(2027, 12, 15, 0, 0),
#              'дедлайн': datetime(2024, 12, 27, 0, 0),
#              'заголовок': ['такая же', 'капуста', 'лук']}]


def update_note(all_info):
    # Формат даты заметки
    d_format = "%d-%m-%y"
    # Возможные статусы заметок
    status_txt = ["Выполнено", "В процессе", "Отложено"]


    print("Вы можете изменить любую заметку.")
    print("Вот все заметки!")
    for i in all_info:
        print(i)
    # - общий цикл
    while True:
        try:
            print("Укажите номер заметки!")
            # - цикл для разложения списка
            zametka_nomer = int(input("Какую заметку вы хотите изменить: "))
            for i in all_info:
                if i["Заметка № "] == zametka_nomer:
                    print(f"Вы выбрали заметку № {zametka_nomer}")
                    for j, k in i.items():
                        if j != "Заметка № ":
                            print(f"{j}: {k}")

                    while True:
                        # - общий для введения типа данных
                        data_type = input("Какой тип данных вы хотите изменить?: ").lower()
                        if data_type == "Заметка №":
                            print("Изменение номера заметки запрещено. Введите другой тип данных.")
                            continue
                            # - проверка на даты и фиксация дат
                        if data_type in i:
                            if data_type in ["дата создания", "дедлайн"]:
                                try:
                                    new_value = input(f"Введите новое значение для '{data_type}' в формате DD-MM-YY: ")
                                    i[data_type] = datetime.strptime(new_value, d_format)
                                    print(f"{data_type} успешно обновлено!")
                                except ValueError:
                                    print("Некорректный формат даты. Попробуйте снова.")
                                    continue
                                # - проверка на заголовок и введения их
                            elif data_type == "заголовок":
                                try:
                                    zagolovok_nomer = int(input("Какой заголовок вы хотите изменить? (1, 2, 3): "))
                                    if 1 <= zagolovok_nomer <= len(i["заголовок"]):
                                        new_zagolovok = input("Введите новый заголовок: ")
                                        i["заголовок"][zagolovok_nomer - 1] = new_zagolovok
                                        print(f"Заголовок номер {zagolovok_nomer} успешно обновлен!")
                                    else:
                                        print("Некорректный номер заголовка.")
                                except ValueError:
                                    print("Введите корректный номер заголовка.")
                                    continue
                                # - проверка статуса и изменение статуса
                            elif data_type == "статус":
                                while True:
                                    print("Выберите новый статус заметки:")
                                    print(" 1 - Выполнено")
                                    print(" 2 - В процессе")
                                    print(" 3 - Отложено")
                                    try:
                                        status_int = int(input("Введите код статуса (1, 2, 3): "))
                                        if status_int in [1, 2, 3]:
                                            new_status = status_txt[status_int - 1]
                                            i[data_type] = [new_status]
                                            print(f"Статус изменен на: {new_status}")
                                            break
                                        else:
                                            print("Введен неверный код. Попробуйте снова.")
                                    except ValueError:
                                        print("Введите корректное число (1, 2 или 3).")
                                # - введение остальных значений
                            else:
                                new_value = input(f"Введите новое значение для '{data_type}': ")
                                i[data_type] = new_value
                                print(f"{data_type} успешно обновлено!")

                            print("Текущие данные после изменений:", i)
                            break
                        else:
                            print(f"Значение '{data_type}' не найдено. Введите тип данных правильно.")
                    break
            else:
                print("Заметка с таким номером не найдена! Введите номер заметки еще раз.")
        except ValueError:
            print("Введите корректное значение (Число).")

        return all_info
