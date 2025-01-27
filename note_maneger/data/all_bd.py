import sqlite3
from progekt.note_maneger.data.create_note_function import create_note


namebd = "notemulti"
all_info = []
create_note(all_info)




def bd(all_info,namebd):
    connection = sqlite3.connect(f"{namebd}.bd")
    cursor = connection.cursor()


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
    cursor.execute(create_table_notes)
    print(all_info)
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