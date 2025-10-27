#include <iostream>
using namespace std;

// Интерполирующий поиск предполагает, что массив равномерно распределён.
// Эффективнее бинарного поиска, если данные распределены равномерно.
int interpolationSearch(int arr[], int size, int key) {
    int low = 0;                     // Нижняя граница поиска
    int high = size - 1;             // Верхняя граница поиска

    while ((low <= high) && (key >= arr[low]) && (key <= arr[high])) {
        // Формула интерполяции для нахождения приблизительного положения ключа
        int pos = low + (((double)(high - low) / (arr[high] - arr[low])) * (key - arr[low]));

        // Если ключ найден, вернуть его индекс
        if (arr[pos] == key) {
            return pos;
        }

        // Если ключ меньше элемента в выбранной позиции, двигаться влево
        if (arr[pos] < key) {
            low = pos + 1;
        }
        // Иначе двигаться вправо
        else {
            high = pos - 1;
        }
    }

    // Если ключ не найден, возврат -1
    return -1;
}

// Простая демонстрационная функция для проверки работоспособности
int main() {
    int arr[] = {10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47}; // Отсортированный массив
    int size = sizeof(arr) / sizeof(arr[0]);  // Размер массива
    int key = 18;                            // Ключевое значение для поиска

    int index = interpolationSearch(arr, size, key);

    if (index != -1) {
        cout << "Элемент найден на позиции: " << index << endl;
    } else {
        cout << "Элемент не найден." << endl;
    }

    return 0;
}