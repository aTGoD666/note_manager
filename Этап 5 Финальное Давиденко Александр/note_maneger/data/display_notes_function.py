from datetime import datetime



# Исходные данные
all_info = [{'Заметка № ': 1,
             'имя': 'паша',
             'описание': 'Нужно создать словарь для теста удаления',
             'статус': ['Новая'],
             'дата создания': datetime(2024, 12, 27, 0, 0),
             'дедлайн': datetime(2024, 12, 27, 0, 0),
             'заголовок': ['обучение коду', 'вводный урок', 'простой код']},
            {'Заметка № ': 2,
             'имя': 'вова',
             'описание': 'ор',
             'статус': ['Новая'],
             'дата создания': datetime(2024, 12, 26, 0, 0),
             'дедлайн': datetime(2024, 12, 27, 0, 0),
             'заголовок': ['вторая заметка', 'тот же', 'тот же']},
            {'Заметка № ': 3,
             'имя': 'коля',
             'описание': 'кака бубу',
             'статус': ['Новая'],
             'дата создания': datetime(2027, 12, 15, 0, 0),
             'дедлайн': datetime(2024, 12, 27, 0, 0),
             'заголовок': ['такая же', 'капуста', 'лук']}]

def display_notes(all_info):
    # Формат даты заметки
    d_format = "%d-%m-%y"
    # Возможные статусы заметок
    status_txt = ["Выполнено", "В процессе", "Отложено"]
    #all_info = [] - переменная для проверки кейса с пустым списком
    # Проверка, если список пуст
    if not all_info:
        print("Список заметок пуст!")
        return all_info # Завершаем выполнение функции

    # отображение списка заметок
    print("Добро пожаловать в 'Доску заметок'!")
    print("Вот все заметки!")
    for i in all_info:
        print("------------------------")
        for j, k in i.items():
            print(f"{j}: {k}")
