try:
    with open('erors.txt', encoding='utf-8') as erors:
        print(erors.read())
except FileNotFoundError:
    print("Файл 'erors.txt' не найден! " )
    try:
        with open('erors.txt','w', encoding='utf-8') as erors:
            print("Файл 'erors.txt' успещшно создан !")
    except PermissionError:
        print("У вас нет доступа к файлу 'erors.txt'.")
    except UnicodeDecodeError:
        print("Ошибка кодировки файла. Выберите другую кодировку!")
    except OSError as e:
        print(f"Ошибка файловой системы: {e}")



erors.close()