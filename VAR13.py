=== Жадный алгоритм для распределения ресурсов ===

Введите общий объем доступных ресурсов: 40
Введите количество проектов: 4

Введите данные для каждого проекта:

Проект 1:
  Требуемый ресурс: 10
  Прибыль от проекта: 50 

Проект 2:
  Требуемый ресурс: 15
  Прибыль от проекта: 80

Проект 3:
  Требуемый ресурс: 20
  Прибыль от проекта: 90

Проект 4:
  Требуемый ресурс: 8
  Прибыль от проекта: 40


def greedy_resource_allocation():
    """
    Жадный алгоритм для оптимального распределения ресурсов среди проектов
    """
    print("=== Жадный алгоритм для распределения ресурсов ===\n")
    
    # Ввод общего объема ресурсов
    while True:
        try:
            total_resources = float(input("Введите общий объем доступных ресурсов: "))
            if total_resources <= 0:
                print("Объем ресурсов должен быть положительным числом.")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите числовое значение.")
    
    # Ввод количества проектов
    while True:
        try:
            n = int(input("Введите количество проектов: "))
            if n <= 0:
                print("Количество проектов должно быть положительным числом.")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите целое число.")
    
    projects = []
    print("\nВведите данные для каждого проекта:")
    
    # Ввод данных о проектах
    for i in range(n):
        print(f"\nПроект {i+1}:")
        while True:
            try:
                resource = float(input("  Требуемый ресурс: "))
                if resource <= 0:
                    print("  Ресурс должен быть положительным числом.")
                    continue
                break
            except ValueError:
                print("  Пожалуйста, введите числовое значение.")
        
        while True:
            try:
                profit = float(input("  Прибыль от проекта: "))
                if profit < 0:
                    print("  Прибыль не может быть отрицательной.")
                    continue
                break
            except ValueError:
                print("  Пожалуйста, введите числовое значение.")
        
        # Вычисление эффективности (прибыль на единицу ресурса)
        efficiency = profit / resource if resource > 0 else 0
        projects.append({
            'index': i + 1,
            'resource': resource,
            'profit': profit,
            'efficiency': efficiency
        })
    
    # Сортировка проектов по убыванию эффективности (прибыль/ресурс)
    projects.sort(key=lambda x: x['efficiency'], reverse=True)
    
    # Распределение ресурсов жадным алгоритмом
    selected_projects = []
    used_resources = 0
    total_profit = 0
    
    for project in projects:
        if used_resources + project['resource'] <= total_resources:
            # Если проект полностью помещается в оставшиеся ресурсы
            selected_projects.append({
                'project': project['index'],
                'resource_used': project['resource'],
                'profit_gained': project['profit'],
                'fraction': 1.0
            })
            used_resources += project['resource']
            total_profit += project['profit']
        else:
            # Если проект не помещается полностью, можно добавить его частично
            remaining_resources = total_resources - used_resources
            if remaining_resources > 0:
                fraction = remaining_resources / project['resource']
                partial_profit = project['profit'] * fraction
                
                selected_projects.append({
                    'project': project['index'],
                    'resource_used': remaining_resources,
                    'profit_gained': partial_profit,
                    'fraction': fraction
                })
                used_resources += remaining_resources
                total_profit += partial_profit
            break
    
    # Вывод результатов
    print("\n" + "="*50)
    print("РЕЗУЛЬТАТЫ РАСПРЕДЕЛЕНИЯ РЕСУРСОВ")
    print("="*50)
    
    print(f"\nОбщий объем ресурсов: {total_resources}")
    print(f"Использовано ресурсов: {used_resources:.2f}")
    print(f"Общая прибыль: {total_profit:.2f}")
    
    print(f"\nВыбранные проекты (в порядке приоритета):")
    print("-" * 60)
    print(f"{'Проект':<10} {'Ресурсы':<12} {'Прибыль':<12} {'Доля':<10}")
    print("-" * 60)
    
    for item in selected_projects:
        fraction_percent = item['fraction'] * 100
        print(f"{item['project']:<10} {item['resource_used']:<12.2f} "
              f"{item['profit_gained']:<12.2f} {fraction_percent:<10.1f}%")
    
    # Вывод информации об эффективности проектов
    print(f"\nЭффективность проектов (прибыль/ресурс):")
    print("-" * 40)
    print(f"{'Проект':<10} {'Эффективность':<15}")
    print("-" * 40)
    for project in projects:
        print(f"{project['index']:<10} {project['efficiency']:<15.2f}")

def main():
    """
    Основная функция программы
    """
    try:
        greedy_resource_allocation()
        
        # Возможность повторного запуска
        while True:
            restart = input("\nХотите решить еще одну задачу? (да/нет): ").lower()
            if restart in ['да', 'д', 'yes', 'y']:
                greedy_resource_allocation()
            elif restart in ['нет', 'н', 'no', 'n']:
                print("Программа завершена.")
                break
            else:
                print("Пожалуйста, введите 'да' или 'нет'.")
                
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем.")
    except Exception as e:
        print(f"\nПроизошла ошибка: {e}")

# Пример использования
if __name__ == "__main__":
    main()



==================================================
РЕЗУЛЬТАТЫ РАСПРЕДЕЛЕНИЯ РЕСУРСОВ
==================================================

Общий объем ресурсов: 40.0
Использовано ресурсов: 40.00
Общая прибыль: 201.50

Выбранные проекты (в порядке приоритета):
------------------------------------------------------------
Проект     Ресурсы      Прибыль      Доля
------------------------------------------------------------
2          15.00        80.00        100.0     %
1          10.00        50.00        100.0     %
4          8.00         40.00        100.0     %
3          7.00         31.50        35.0      %

Эффективность проектов (прибыль/ресурс):
----------------------------------------
Проект     Эффективность
----------------------------------------
2          5.33
1          5.00
Проект     Эффективность
----------------------------------------
2          5.33
1          5.00
4          5.00
3          4.50

