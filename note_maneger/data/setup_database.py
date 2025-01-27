import sqlite3
from progekt.note_maneger.data.create_note_function import create_note
from datetime import datetime

from progekt.note_maneger.data.delete_note import delete_note

namebd = "notemulti"
all_info = []
create_table_notes = """
    CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    zametka_nomber INTEGER,
    username TEXT NOT NULL,
    content TEXT NOT NULL,
    status_zam TEXT NOT NULL,
    created_date TEXT NOT NULL,
    issue_date TEXT NOT NULL,
    title_all TEXT NOT NULL
    );
    """

def note_to_db(namebd):
    connection = sqlite3.connect(f"{namebd}.db")
    cursor = connection.cursor()
    cursor.execute(create_table_notes)
    connection.commit()
    rows = cursor.fetchall()

    if rows:
        print("Содержимое таблицы notes:")
        for row in rows:
            print(row)
    else:
        print("Таблица notes пуста.")

    connection.close()

#note_to_db(namebd)


#create_note(all_info)
def save_note_to_db(all_info,namebd):
    connection = sqlite3.connect(f"{namebd}.db")
    cursor = connection.cursor()
    cursor.execute(create_table_notes)
    for i in all_info:
        zametka_nomber = i["Заметка № "]
        username = i["имя"]
        content = i["описание"]
        status_zam = i["статус"][0]
        created_date = i["дата создания"].strftime("%Y-%m-%d %H:%M:%S")  # Преобразуем дату в строку
        issue_date = i["дедлайн"].strftime("%Y-%m-%d %H:%M:%S")  # Преобразуем дату в строку
        title_all = ", ".join(i["заголовок"])  # Объединяем заголовки в строку


        insert_query = """
        INSERT INTO notes (zametka_nomber, username, content, status_zam, created_date, issue_date, title_all)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(insert_query, (zametka_nomber, username, content, status_zam, created_date, issue_date, title_all))

    connection.commit()
    connection.close()

#save_note_to_db(all_info,namebd)

def load_notes_from_db(namebd):
    connection = sqlite3.connect(f"{namebd}.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM notes")
    rows = cursor.fetchall()
    # Вывод содержимого таблицы
    if rows:
        print("Содержимое таблицы notes:")
        for row in rows:
            print(row)
    else:
        print("Таблица notes пуста.")

    connection.close()

load_notes_from_db(namebd)


note_id = int(input("Ведите ID заметки :"))
print("1 - Имя")
print("2 - Описание")
print("3 - Статус")
print("4 - Дата создания")
print("5 - Дедлайн")
print("6 - Заголовок")
choice = int(input("Какой тип данных вы хотите изменить :"))

field_map = {
        1: "username",
        2: "content",
        3: "status_zam",
        4: "created_date",
        5: "issue_date",
        6: "title_all"
    }

    # Проверяем, выбрано ли корректное поле
if choice not in field_map:
    print("Некорректный выбор. Попробуйте снова.")

field_to_update = field_map[choice]
new_value = input(f"Введите новое значение для {field_to_update}: ")

# Если поле — дата, преобразуем в нужный формат
if field_to_update in ["created_date", "issue_date"]:
    try:
        new_value = datetime.strptime(new_value, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Некорректный формат даты. Используйте YYYY-MM-DD HH:MM:SS.")

# Обновляем запись в базе
print("Запись успешно обновлена!")

def update_note_in_db(note_id,field_to_update,new_value,namebd):
    connection = sqlite3.connect(f"{namebd}.db")
    cursor = connection.cursor()
    update_query = f"""
       UPDATE notes
       SET {field_to_update} = ?
       WHERE id = ?;
       """

    cursor.execute(update_query, (new_value, note_id))

    cursor.execute(create_table_notes)

    connection.commit()
    connection.close()

#update_note_in_db(note_id,field_to_update, new_value, namebd)


def delete_note_from_db(namebd):
    note_id = int(input("Ведите ID заметки которую надо удалить :"))
    connection = sqlite3.connect(f"{namebd}.db")
    cursor = connection.cursor()
    # SQL-запрос на удаление
    delete_query = "DELETE FROM notes WHERE id = ?;"
    cursor.execute(delete_query, (note_id,))

    # Сохраняем изменения
    connection.commit()


#delete_note_from_db(namebd)


def search_notes_by_keyword(namebd):
    keyword = input("Введите значение заголовка или описания: ")
    connection = sqlite3.connect(f"{namebd}.db")
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM notes
    WHERE title_all LIKE ? OR content LIKE ?;
    """, (f"%{keyword}%", f"%{keyword}%"))

    rows = cursor.fetchall()
    connection.close()

    return [{'id': row[0], 'username': row[1], 'title_all': row[2], 'content': row[3], 'status': row[4], 'created_date': row[5],
    'issue_date': row[6]} for row in rows]

#search_notes_by_keyword(namebd)


def filter_notes_by_status(namebd):
    print("1 - Новый")
    print("2 - Выполнено")
    print("3 - В процессе")
    print("4 - Отложено")
    choice_status = int(input("Ведите код статуса для поиска заметок :"))

    status_map = {
        1: "Новый",
        2: "Выполнено",
        3: "В процессе",
        4: "Отложено",
    }
    if choice_status not in status_map:
        print("Некорректный выбор. Попробуйте снова.")
    status = status_map[choice_status]
    connection = sqlite3.connect(f"{namebd}.db")
    cursor = connection.cursor()
    delete_query = "SELECT * FROM notes WHERE status_zam = ?;"
    cursor.execute(delete_query,(status,))
    rows = cursor.fetchall()
    connection.commit()

    return [{'id': row[0], 'username': row[1], 'title_all': row[2], 'content': row[3], 'status': row[4],'created_date': row[5],
    'issue_date': row[6]} for row in rows]

#filter_notes_by_status(namebd)