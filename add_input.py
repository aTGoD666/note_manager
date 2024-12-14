from datetime import datetime
username = input("Имя: ") # имя пользователя
title = input("Заголовок: ")  # заголовок
content = input("Описание: ") # описание заметки
status = input("Статус: ") # статус заметки
created_date = datetime.strptime(input("Дата: "), "%d-%m-%y") # дата создание заметки (формат дд-мм-гггг)
issue_date = datetime.strptime(input("Дата: "), "%d-%m-%y") # дата истечения заметки (формат дд-мм-гггг)
print(username)