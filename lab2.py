# мультисписок (вложенный список) Таблица данных
data_table = [
    ['Имя', 'Возраст', 'Город'],
    ['Анна', 25, 'Москва'],
    ['Иван', 30, 'СПб'],
    ['Мария', 22, 'Казань']
]
print(data_table[0][0], data_table[1][0])

print("")

# реализация дека 
from collections import deque 
tasks = deque() 
# Добавляем задачи в очередь 
tasks.append("123") 
tasks.append("456") 
tasks.append("789") 
# Обработка задач в порядке FIFO 
print("сначала ввели", tasks.popleft(), "затем ввели", tasks.popleft())