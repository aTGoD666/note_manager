from datetime import datetime
username = input("Имя: ") # имя пользователя
title = input("Заголовок темы: ")  # заголовок
title2 = input("Заголовок урока: ")  # заголовок
title3 = input("Заголовок задания: ")  # заголовок
title_all = [title,title2,title3]  # заголовок
content = input("Описание: ") # описание заметки
status = input("Статус: ") # статус заметки
created_date = datetime.strptime(input("Дата: "), "%d-%m-%y") # дата создание заметки (формат дд-мм-гггг)
issue_date = datetime.strptime(input("Дата: "), "%d-%m-%y") # дата истечения заметки (формат дд-мм-гггг)
all_info = [username,
            title,
            title2,
            title3,
            content,
            status,
            created_date,
            issue_date,
            title_all]

print(all_info)