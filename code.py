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


//
