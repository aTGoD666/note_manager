from datetime import datetime
from check_deadline import  issue_date # - импорт даты дед лайна

status_zam = ["Новая"]  # - статус заметки
status_txt = ["Выполнено","В процессе","Отложено"] # - статусы
d_format = "%d-%m-%y" # - формат дат заметки


print("Текущий статус заметки")
print(status_zam)
tvist = input("Изменить? (да/нет): ").lower()

# - цикл для определения нужно ли менять статус

while True:
   if tvist not in ["да","нет"]:
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


                    if status_int in [1,2,3]:
                        print("Статус изменени на")
                        print(status_txt[status_int-1])
                        break
                else:
                    print("Введен неверный код")
                    print(status_txt[status_int])
                break
# - определение срока дедлайна
created_date = datetime.strptime(input("Дата: "), d_format)
issue_date = datetime.strptime(issue_date,d_format )

if created_date < issue_date:
    print("Срок не вышел")
elif created_date > issue_date:
    print("Срок вышел")
else:
    print("Срок сегодня")
