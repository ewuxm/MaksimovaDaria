#include <iostream>
#include <vector>
#include <string>
#include <deque>  
using namespace std;

int main() {
    // Мультисписок (вложенный вектор) - таблица данных
    vector<vector<string>> data_table = {  
        {"Имя", "Возраст", "Город"},      
        {"Анна", "25", "Москва"},
        {"Иван", "30", "СПб"},
        {"Мария", "22", "Казань"}
    };
    
    cout << data_table[0][0] << " " << data_table[1][0] << endl;

    // Реализация дека
    deque<string> tasks;

    tasks.push_back("123");
    tasks.push_back("456");
    tasks.push_back("789");

    cout << "сначала ввели " << tasks.front() << ", затем ввели ";
    tasks.pop_front();
    cout << tasks.front() << endl;
    return 0;
}