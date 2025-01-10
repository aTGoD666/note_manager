from datetime import datetime

issue_date = "21-12-24"  # - дата дэдлайна заметки для задания 2.2
d_format = "%d-%m-%y" # - формат дат 1
d_format2 = "%y-%m-%d" # - формат дат 2
# - ввод даты дэлдайна через цикл
issue_date = datetime.strptime(issue_date, d_format)
while True:
    try:
        created_date = datetime.strptime(input("Дата дэдлайна (дд-мм-гг): "), d_format)
        print("Дата успешно введена:", created_date.strftime(d_format))
        break
    except ValueError:
        print("Неверный формат даты. Попробуйте снова.")

    try:
        created_date = datetime.strptime(input("Дата дэдлайна (гг-мм-дд): "), d_format2)
        print("Дата успешно введена:", created_date.strftime(d_format2))
        break
    except ValueError:
        print("Неверный формат даты. Попробуйте снова.")


# - условие проверки даты

if created_date < datetime.now():
        print("Срок не вышел")
        defference = (created_date - datetime.now()).days
        defference = abs(defference)
        print(f"Осталось: {defference} д.")
elif created_date > datetime.now():
        print("Срок вышел")
        defference = (created_date - datetime.now()).days
        print(f"Срок просрочен на: {defference} д.")
else:
        print("Дэд лайн сегодня")


