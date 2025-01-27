from datetime import datetime

d_format = "%d-%m-%y"  # - формат дат заметки
d_format2 = "%y-%m-%d"  # - формат дат 2

def valid_date(valid_date):
    try:
        datetime.strptime(valid_date, d_format)
        print("Дата корректна", valid_date.strftime(d_format))
    except ValueError:
        print(F"Неверный формат даты.{d_format}")
    try:
        datetime.strptime(valid_date, d_format2)
        print("Дата корректна", valid_date.strftime(d_format2))
    except ValueError:
        print(f"Неверный формат даты.{d_format2}")

    return valid_date