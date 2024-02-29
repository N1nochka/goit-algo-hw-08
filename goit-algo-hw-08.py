import heapq

def minimize_cable_costs(cables):
    # Крок 1: Ініціалізація купи
    heapq.heapify(cables)
    
    # Ініціалізація змінної для збереження загальних витрат
    total_cost = 0
    
    # Поки в купі є більше одного кабелю
    while len(cables) > 1:
        # Крок 2: Вилучення двох найдовших кабелів
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)
        
        # Крок 3: Об'єднання кабелів та обчислення витрат
        new_cable = cable1 + cable2
        
        # Додавання витрат до загальних витрат
        total_cost += new_cable
        
        # Додавання нового кабелю до купи
        heapq.heappush(cables, new_cable)

    # Повернення мінімальних загальних витрат
    return total_cost

# Приклад використання
cables = [4, 6, 8, 10]  # Припустимо, що це список довжин кабелів
min_cost = minimize_cable_costs(cables)
print("Мінімальні загальні витрати:", min_cost)