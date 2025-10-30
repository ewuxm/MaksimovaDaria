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
