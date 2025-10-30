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
