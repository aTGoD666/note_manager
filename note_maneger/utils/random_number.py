import random

used_ids = set()

# функция добавления уникального id
def random_num(all_infodick):
    global used_ids
    while True:
        id_note = random.randint(1,1000)
        if id_note not in used_ids:
            used_ids.add(id_note)
            id_dick = {'id заметки': id_note}
            all_infodick.update(id_dick)
            return all_infodick