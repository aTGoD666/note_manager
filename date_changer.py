from datetime import datetime
username = "aT_God" # имя пользователя
title = "Старт"  # заголовок
content = "Первая" # описание заметки
status = "Новая" # статус заметки
created_date = "10-06-24" # дата создание заметки (формат дд-мм-гггг)
issue_date = "11-07-24" # дата истечения заметки (формат дд-мм-гггг)

# Код для отображения дат
temp_created_date = datetime.strptime(created_date, "%d-%m-%y") # форматируем дату создания
temp_issue_date = datetime.strptime(issue_date, "%d-%m-%y") # форматируем дату истечения
print(temp_issue_date.strftime("%d-%m"))
print(temp_created_date.strftime("%d-%m"))
