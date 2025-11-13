def get_project_data():
    """Функция для получения данных о проектах с консоли."""
    projects = []
    print("Введите данные о проектах (ресурс и прибыль).")
    print("Формат ввода: <ресурс> <прибыль> (например, 10 50)")
    print("Для завершения ввода введите 'стоп'.")

    while True:
        user_input = input("Введите данные о проекте: ").strip()
        if user_input.lower() == 'стоп':
            break

        try:
            resource, profit = map(int, user_input.split())
            if resource <= 0 or profit <= 0:
                print("Значения должны быть положительными. Попробуйте снова.")
                continue
            projects.append({"resource": resource, "profit": profit})
        except ValueError:
            print("Ошибка: введите два целых числа (ресурс и прибыль). Попробуйте снова.")

    return projects


def get_total_resources():
    """Функция для получения общего объёма ресурсов с консоли."""
    while True:
        try:
            total_resources = int(input("Введите общий объём ресурсов: "))
            if total_resources <= 0:
                print("Значение должно быть положительным. Попробуйте снова.")
                continue
            return total_resources
        except ValueError:
            print("Ошибка: введите целое число. Попробуйте снова.")


def greedy_algorithm(projects, total_resources):
    """Реализация жадного алгоритма для распределения ресурсов."""
    # Сортируем проекты по соотношению прибыль/ресурс (убывание)
    sorted_projects = sorted(projects, key=lambda x: x["profit"] / x["resource"], reverse=True)

    # Переменные для отслеживания выбранных проектов и оставшихся ресурсов
    selected_projects = []
    remaining_resources = total_resources
    total_profit = 0

    # Проходим по отсортированным проектам и выбираем те, которые помещаются в бюджет
    for project in sorted_projects:
        if project["resource"] <= remaining_resources:
            selected_projects.append(project)
            remaining_resources -= project["resource"]
            total_profit += project["profit"]

    return selected_projects, total_profit, remaining_resources


def print_results(selected_projects, total_profit, used_resources, remaining_resources):
    """Функция для вывода результатов."""
    print("\n" + "="*50)
    print("РЕЗУЛЬТАТЫ РАСПРЕДЕЛЕНИЯ РЕСУРСОВ")
    print("="*50)

    if selected_projects:
        print("Выбранные проекты:")
        for i, project in enumerate(selected_projects, 1):
            print(f"{i}. Ресурс: {project['resource']}, Прибыль: {project['profit']}")
    else:
        print("Ни один проект не может быть выбран с заданными ресурсами.")

    print(f"\nОбщая прибыль: {total_profit}")
    print(f"Использовано ресурсов: {used_resources}")
    print(f"Осталось ресурсов: {remaining_resources}")
    print("="*50)


def main():
    """Основная функция программы."""
    print("Жадный алгоритм для распределения ресурсов среди проектов")
    print("Цель: максимизация прибыли при ограниченном объёме ресурсов.\n")

    # Получение данных с консоли
    projects = get_project_data()
    if not projects:
        print("Не было введено ни одного проекта. Завершение работы.")
        return

    total_resources = get_total_resources()

    # Проверка на наличие проектов
    if not projects:
        print("Список проектов пуст. Завершение работы.")
        return

    # Запуск жадного алгоритма
    selected_projects, total_profit, remaining_resources = greedy_algorithm(projects, total_resources)
    used_resources = total_resources - remaining_resources

    # Вывод результатов
    print_results(selected_projects, total_profit, used_resources, remaining_resources)


if __name__ == "__main__":
    main()
