#include <iostream>
#include <vector>
using namespace std;

// Алгоритм Merge Sort: сначала делим массив на части, потом сливаем отсортированные части вместе
void mergeSort(vector<int>& arr, int l, int r) {
    if(l >= r) return;                      // Базовый случай: массив длины 1 или меньше

    // Вычисление середины массива
    int m = l + (r-l)/2;                    // Предотвращаем переполнение целых чисел при вычислениях

    // Рекурсивно сортируем левую и правую части
    mergeSort(arr, l, m);                   // Сортируем левую половину
    mergeSort(arr, m+1, r);                 // Сортируем правую половину

    // Временные массивы для сохранения левой и правой частей
    vector<int> tempLeft(m-l+1), tempRight(r-m);

    // Копируем элементы в временные массивы
    for(int i=0; i<m-l+1; ++i) tempLeft[i] = arr[l+i];
    for(int i=0; i<r-m; ++i) tempRight[i] = arr[m+1+i];

    // Индексы для обхода трёх массивов
    int i = 0, j = 0, k = l;

    // Основной цикл для слияния отсортированных частей
    while(i < tempLeft.size() && j < tempRight.size()) {
        if(tempLeft[i] <= tempRight[j])
            arr[k++] = tempLeft[i++];       // Берём минимальный элемент из левой части
        else
            arr[k++] = tempRight[j++];     // Иначе берём минимальный элемент из правой части
    }

    // Добавляем остатки одной из частей, если они ещё есть
    while(i < tempLeft.size())
        arr[k++] = tempLeft[i++];
    while(j < tempRight.size())
        arr[k++] = tempRight[j++];
}

// Тестовая программа
int main() {
    vector<int> arr = {38, 27, 43, 3, 9, 82, 10};
    int size = arr.size();

    // Выполняем сортировку
    mergeSort(arr, 0, size-1);

    // Выводим отсортированный массив
    cout << "Отсортированный массив: ";
    for(int x : arr)
        cout << x << " ";
    cout << endl;

    return 0;
}