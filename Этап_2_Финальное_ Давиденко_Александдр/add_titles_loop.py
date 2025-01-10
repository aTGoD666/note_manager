title_all = [] # - Массив заголовков
idei_all = [] # - Массив идей
task_all = [] # - Массив задач

print("Запиши один или несколько заголовков")

# - цикл что бы задать заголовки

title = input("Заголовок: ")
while title not in ['', 'стоп']:
    title_all.append(title)
    title = input("Заголовок: ")
    if title in title_all:
        title_all.pop(-1)
        print("Значение есть")

# - цикл что бы задать идей

print("Запиши одну или несколько идей")

idei = input("Идея: ")
while idei not in ['', 'стоп']:
    idei_all.append(idei)
    idei = input("Идея: ")
    if idei in idei_all:
        idei_all.pop(-1)
        print("Значение есть")

# - цикл что бы задать задачи

print("Запиши одну или несколько задач")

task = input("Задача: ")
while task not in ['', 'стоп']:
    task_all.append(task)
    task = input("Задача: ")
    if task in task_all:
        task_all.pop(-1)
        print("Значение есть")

# - вывод всех списков

print("Все заголовки")
print(title_all)
print("Все идей")
print(idei_all)
print("Все задачи")
print(task_all)