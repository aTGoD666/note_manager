

status_txt = ["Выполнено","В процессе","Отложено","Новая"] # - статусы

def status_ck(all_info,zametka_nomber):
    status_note = all_info[zametka_nomber - 1]["статус"][0]
    if status_note in status_txt:
        print("статус верный")
    else:
        print("Статус не корректен!")
