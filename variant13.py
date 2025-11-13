projects = [
    {"resource": 10, "profit": 50},
    {"resource": 15, "profit": 80},
    {"resource": 20, "profit": 90},
    {"resource": 8, "profit": 40}
]
total_resources = 40

# Сортируем проекты по соотношению прибыль/ресурс (убывание)
# Это ключевой шаг жадного алгоритма — выбираем "наиболее выгодные" проекты
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

# Вывод результатов
print("Выбранные проекты:")
for i, project in enumerate(selected_projects, 1):
    print(f"{i}. Ресурс: {project['resource']}, Прибыль: {project['profit']}")

print(f"\nОбщая прибыль: {total_profit}")
print(f"Использовано ресурсов: {total_resources - remaining_resources}")
print(f"Осталось ресурсов: {remaining_resources}")
