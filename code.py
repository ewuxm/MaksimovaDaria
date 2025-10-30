// блочная (корзинная) сортировка
def bucket_sort(arr):
    # Проверяем наличие элементов в списке
    if len(arr) == 0:
        return arr

    # Определение минимального и максимального значений списка
    min_val = min(arr)
    max_val = max(arr)
    
    # Количество баков
    num_buckets = len(arr)
    
    # Создаем пустые баки (списки)
    buckets = [[] for _ in range(num_buckets)]
    
    # Распределяем элементы по бакам
    for value in arr:
        index = int((value - min_val) / (max_val - min_val + 1) * (num_buckets - 1))
        buckets[index].append(value)
    
    # Сортируем каждый бак и собираем итоговый список
    sorted_arr = []
    for bucket in buckets:
        sorted_bucket = sorted(bucket)  # Используем встроенную сортировку каждого бака
        sorted_arr.extend(sorted_bucket)
    
    return sorted_arr
# Пример использования
if __name__ == "__main__":
    input_list = [89, 56, 34, 12, 78, 45]
    print("Исходный массив:", input_list)
    sorted_list = bucket_sort(input_list)
    print("Отсортированный массив:", sorted_list)
// Исходный массив: [89, 56, 34, 12, 78, 45]
// Отсортированный массив: [12, 34, 45, 56, 78, 89]



// Блинная сортировка
def flip(arr, k):
    """Перевернуть первые k элементов массива."""
    arr[:k+1] = arr[:k+1][::-1]

def find_max_index(arr, n):
    """Вернуть индекс максимального элемента среди первых n элементов массива."""
    max_idx = 0
    for i in range(n):
        if arr[i] > arr[max_idx]:
            max_idx = i
    return max_idx

def pancake_sort(arr):
    """Алгоритм блинной сортировки"""
    current_size = len(arr)
    
    while current_size > 1:
        # Найти максимальный элемент среди оставшихся
        max_idx = find_max_index(arr, current_size)
        
        # Если максимум находится не на последней позиции,
        # перевернем массив дважды:
        # сначала поднимаем наибольший элемент вверх,
        # потом ставим его на своё место
        if max_idx != current_size - 1:
            flip(arr, max_idx)   # Поднимаем самый большой элемент вверх
            flip(arr, current_size - 1)  # Ставим его на последнее место
            
        current_size -= 1  # Уменьшаем размер обрабатываемого массива
    
    return arr


# Тестирование алгоритма
arr = [3, 6, 2, 4, 5, 1]
print("Исходный массив:", arr)
sorted_arr = pancake_sort(arr)
print("Отсортированный массив:", sorted_arr)

// Исходный массив: [3, 6, 2, 4, 5, 1]
// Отсортированный массив: [1, 2, 3, 4, 5, 6]



// Сортировка бусинами (гравитационная)
import numpy as np

def bead_sort(arr):
    """
    Реализует сортировку бусинками (gravity sort).
    Вход: список целых положительных чисел
    Выход: отсортированный список
    """
    # Шаг 1: Создаем матрицу N x M, где строки соответствуют числам списка
    rows = len(arr)
    cols = max(arr)
    beads_matrix = np.zeros((rows, cols), dtype=int)

    # Заполняем матрицу "бусинками": первая строка имеет столько единиц, сколько первое число и т.п.
    for row in range(rows):
        beads_matrix[row, :arr[row]] = 1

    # Шаг 2: Применяем силу тяжести - каждый столбец опускается вниз
    for col in range(cols):
        column_sum = sum(beads_matrix[:,col])
        beads_matrix[:,col] = np.concatenate([np.ones(column_sum), np.zeros(rows-column_sum)])

    # Шаг 3: Преобразуем обратно в исходный вид
    result = []
    for row in range(rows):
        count = sum(beads_matrix[row,:])  # количество единичек соответствует числу
        result.append(count)

    return result


if __name__ == "__main__":
    input_list = [5, 3, 1, 8, 2, 7]
    print(f'Исходный массив: {input_list}')
    sorted_list = bead_sort(input_list)
    print(f'Отсортированный массив: {sorted_list}')

// Исходный массив: [5, 3, 1, 8, 2, 7]
// Отсортированный массив: [1, 2, 3, 5, 7, 8]


// Поиск скачками
import math

def jump_search(arr, target):
    """
    Выполняет поиск скачками (jump search) в отсортированном массиве.
    Возвращает индекс найденного элемента или -1, если элемент отсутствует.
    """
    length = len(arr)
    step = int(math.sqrt(length))  # Размер скачка
    prev = 0                       # Текущая позиция

    # Поиск подходящего блока, где элемент может находиться
    while arr[min(step, length)-1] < target:
        prev = step                # Переходим к следующему блоку
        step += int(math.sqrt(length))
        if prev >= length:         # Проверка выхода за пределы массива
            return -1

    # Линейный поиск внутри выбранного блока
    while arr[prev] < target:
        prev += 1                  # Двигаемся вперёд по одному элементу
        if prev == min(step, length):
            return -1              # Вышли за границы текущего блока

    # Нашли нужный элемент
    if arr[prev] == target:
        return prev
    else:
        return -1

# Пример использования
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
target_value = 13

result = jump_search(array, target_value)
if result != -1:
    print(f"Элемент {target_value} найден на позиции {result}.")
else:
    print(f"Элемент {target_value} не найден.")

// Элемент 13 найден на позиции 6.


// Экспоненциальный поиск
def binary_search(arr, left, right, target):
    """
    Стандартный бинарный поиск в пределах левого и правого индексов.
    """
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Элемент найден
        elif arr[mid] < target:
            left = mid + 1  # Продолжаем справа
        else:
            right = mid - 1  # Продолжаем слева
    return -1  # Элемент не найден

def exponential_search(arr, target):
    """
    Экспоненциальный поиск элемента в отсортированном массиве.
    Возвращает индекс элемента или -1, если элемент не найден.
    """
    if not arr or arr[0] > target or arr[-1] < target:
        return -1  # Массив пуст или целевой элемент вне границ массива

    # Первый этап: определяем подходящий диапазон
    bound = 1
    while bound < len(arr) and arr[bound] < target:
        bound *= 2  # Экспоненциально увеличиваем границу

    # Теперь выполняем бинарный поиск в найденном диапазоне
    left = bound // 2
    right = min(bound, len(arr) - 1)
    return binary_search(arr, left, right, target)

# Пример использования
data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
search_target = 13

index = exponential_search(data, search_target)
if index != -1:
    print(f"Элемент {search_target} найден на позиции {index}")
else:
    print(f"Элемент {search_target} не найден в массиве")


// Элемент 13 найден на позиции 6
