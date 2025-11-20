#include <iostream>
#include <vector>
#include <random>
#include <algorithm>
#include <functional>

using namespace std;

// Функция для вычисления фитнесса (количество единиц)
int fitness(const vector<bool>& individual) {
    int count = 0;
    for (bool gene : individual) {
        if (gene) count++;
    }
    return count;
}

// Функция турнирного отбора
vector<bool> tournamentSelection(const vector<vector<bool>>& population, 
                                const vector<int>& fitnessValues, 
                                int tournamentSize) {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(0, population.size() - 1);
    
    vector<bool> bestIndividual;
    int bestFitness = -1;
    
    for (int i = 0; i < tournamentSize; i++) {
        int idx = dis(gen);
        if (fitnessValues[idx] > bestFitness) {
            bestFitness = fitnessValues[idx];
            bestIndividual = population[idx];
        }
    }
    
    return bestIndividual;
}

// Функция одноточечного кроссовера
pair<vector<bool>, vector<bool>> singlePointCrossover(const vector<bool>& parent1, 
                                                     const vector<bool>& parent2) {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, parent1.size() - 2);
    
    int crossoverPoint = dis(gen);
    
    vector<bool> child1, child2;
    
    // Первая часть от parent1, вторая от parent2
    for (int i = 0; i < crossoverPoint; i++) {
        child1.push_back(parent1[i]);
        child2.push_back(parent2[i]);
    }
    
    for (int i = crossoverPoint; i < parent1.size(); i++) {
        child1.push_back(parent2[i]);
        child2.push_back(parent1[i]);
    }
    
    return make_pair(child1, child2);
}

// Функция мутации
void mutate(vector<bool>& individual, double mutationRate) {
    random_device rd;
    mt19937 gen(rd());
    uniform_real_distribution<> dis(0.0, 1.0);
    
    for (int i = 0; i < individual.size(); i++) {
        if (dis(gen) < mutationRate) {
            individual[i] = !individual[i]; // Инвертируем бит
        }
    }
}

// Основная функция генетического алгоритма
vector<bool> geneticOnes(int popSize, int generations) {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(0, 1);
    
    // Инициализация случайной популяции
    vector<vector<bool>> population(popSize, vector<bool>(10));
    for (int i = 0; i < popSize; i++) {
        for (int j = 0; j < 10; j++) {
            population[i][j] = dis(gen);
        }
    }
    
    // Параметры алгоритма
    double mutationRate = 0.1;
    int tournamentSize = 3;
    
    vector<bool> bestIndividual;
    int bestFitness = -1;
    
    for (int gen = 0; gen < generations; gen++) {
        // Оценка фитнесса
        vector<int> fitnessValues(popSize);
        for (int i = 0; i < popSize; i++) {
            fitnessValues[i] = fitness(population[i]);
            
            // Обновляем лучшую особь
            if (fitnessValues[i] > bestFitness) {
                bestFitness = fitnessValues[i];
                bestIndividual = population[i];
            }
        }
        
        // Создание новой популяции
        vector<vector<bool>> newPopulation;
        
        // Элитизм - сохраняем лучшую особь
        newPopulation.push_back(bestIndividual);
        
        // Заполняем остальную часть популяции
        while (newPopulation.size() < popSize) {
            // Отбор родителей
            vector<bool> parent1 = tournamentSelection(population, fitnessValues, tournamentSize);
            vector<bool> parent2 = tournamentSelection(population, fitnessValues, tournamentSize);
            
            // Кроссовер
            auto children = singlePointCrossover(parent1, parent2);
            
            // Мутация
            mutate(children.first, mutationRate);
            mutate(children.second, mutationRate);
            
            // Добавляем детей в новую популяцию
            newPopulation.push_back(children.first);
            if (newPopulation.size() < popSize) {
                newPopulation.push_back(children.second);
            }
        }
        
        population = newPopulation;
        
        // Вывод информации о поколении
        if (gen % 10 == 0) {
            cout << "Поколение " << gen << ": лучший фитнесс = " << bestFitness << endl;
        }
        
        // Если нашли идеальное решение, можно остановиться
        if (bestFitness == 10) {
            cout << "Найдено идеальное решение на поколении " << gen << "!" << endl;
            break;
        }
    }
    
    return bestIndividual;
}

// Функция для вывода бинарной строки
void printBinaryString(const vector<bool>& binaryString) {
    for (bool bit : binaryString) {
        cout << (bit ? '1' : '0');
    }
    cout << endl;
}

int main() {
    int popSize, generations;
    
    cout << "=== Генетический алгоритм: поиск строки с максимальным количеством единиц ===" << endl;
    cout << "Введите размер популяции: ";
    cin >> popSize;
    
    cout << "Введите количество поколений: ";
    cin >> generations;
    
    cout << "\nЗапуск алгоритма..." << endl;
    
    vector<bool> result = geneticOnes(popSize, generations);
    
    cout << "\n=== РЕЗУЛЬТАТ ===" << endl;
    cout << "Лучшая найденная строка: ";
    printBinaryString(result);
    cout << "Количество единиц: " << fitness(result) << endl;
    cout << "Длина строки: " << result.size() << endl;
    
    return 0;
}
