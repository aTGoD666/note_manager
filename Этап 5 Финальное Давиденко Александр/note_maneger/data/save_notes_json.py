import json
#from note_maneger.data.save_notes_to_file import save_notes_to_file
from note_maneger.utils.data_format_json import data_format_json




def append_notes_json(all_info,filename): # - функция записи заметки в файл формата txt
    data_format_json(all_info)
    try:
        with open(filename,'w', encoding='utf-8') as file:
            print("Файл открыт!")
            j_file = json.dump(all_info,file , indent=4, ensure_ascii=False, default=data_format_json)
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


#append_notes_json(all_info,filename)  # - вызов функций для теста