#include <iostream>
using namespace std;

// Функция для построения бинарной кучи (heapify)
void heapify(int arr[], int n, int root) {
    int largest = root;      // Предполагаемый максимальный элемент (корень)
    int left_child = 2*root + 1;     // Левый потомок
    int right_child = 2*root + 2;    // Правый потомок

    // Проверяем, существует ли левый дочерний узел и больше ли он корня?
    if (left_child < n && arr[left_child] > arr[largest])
        largest = left_child;

    // Проверяем, существует ли правый дочерний узел и больше ли он текущего максимального?
    if (right_child < n && arr[right_child] > arr[largest])
        largest = right_child;

    // Меняем местами корень и наибольшего ребенка, если необходим перераспределение
    if (largest != root) {
        swap(arr[root], arr[largest]);
        // Рекурсивно восстанавливаем структуру кучи для нового поддерева
        heapify(arr, n, largest);
    }
}

// Главная функция для сортировки массива методом пирамидальной сортировки
void heapSort(int arr[], int n) {
    // Сначала строим максимальную кучу (max-heap)
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);  // Преобразуем дерево в max-heap начиная с нижних уровней

    // Один за другим извлекаем элементы из кучи и ставим их в конец массива
    for (int i=n-1; i>=0; i--) {
        // Переносим текущий корневой элемент (наибольший) в конец массива
        swap(arr[0], arr[i]);

        // Корректируем оставшуюся кучу, исключая последний элемент
        heapify(arr, i, 0);
    }
}

// Вспомогательная функция для вывода массива
void printArray(int arr[], int size) {
    for (int i=0; i<size; ++i)
        cout << arr[i] << " ";
    cout << endl;
}

// Тестовая программа
int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr)/sizeof(arr[0]);

    cout << "Исходный массив: ";
    printArray(arr, n);  // Добавил вывод исходного массива

    heapSort(arr, n);    // Добавил вызов функции сортировки

    cout << "Отсортированный массив: ";
    printArray(arr, n);  // Добавил вывод отсортированного массива

    return 0;  // Добавил возврат значения
}