filename = 'test2.txt'
def append_notes_to_file(all_info,filename): # - функция записи заметки в файл формата txt
    try:
        with open(filename,'a', encoding='utf-8') as file:
            print("Файл открыт!")
            # - цикл для разложеиня заметки по ключам и написания заметки через строчку
            for idx, note in enumerate(all_info):
                for i, j in note.items():
                    file.write(f"{i}: {j}\n")
                if idx < len(all_info) - 1:
                    file.write("\n")
            print("Заметка успешно добавлена!")
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")
        try:
            with open(filename, 'a', encoding='utf-8') as file:
                print(f"Файл {filename} успещшно создан !")
        except PermissionError:
                print(f"У вас нет доступа к файлу {filename}.")
        except UnicodeDecodeError:
            print("Ошибка кодировки файла. Выберите другую кодировку!")
        except OSError as e:
            print(f"Ошибка файловой системы: {e}")


#append_notes_to_file(all_info,filename)  # - вызов функций для теста
