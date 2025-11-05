#include <iostream>
#include <list>
using namespace std;

int main() {
    list<int> myList = {13, 23, 27, 75, 33, 14, 60};
    
    cout << "Исходный список: ";
    for (int num : myList) {
        cout << num << " ";
    }
    cout << endl;
    
    // Сортировка списка
    myList.sort();
    
    cout << "После сортировки: ";
    for (int num : myList) {
        cout << num << " ";
    }
    cout << endl;
    
    // Реверс списка
    myList.reverse();
    
    cout << "После реверса: ";
    for (int num : myList) {
        cout << num << " ";
    }
    cout << endl;
    
    return 0;
}
