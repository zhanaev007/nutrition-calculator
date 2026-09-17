import sys

def calculate_bmr(weight: float, height: float, age: int, gender: str) -> float:
    """Расчет базового метаболизма по формуле Миффлина-Сан Жеора."""
    if gender.lower() == 'm':
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def main():
    print("=== Калькулятор суточной нормы калорий и БЖУ ===")
    try:
        weight = float(input("Введите вес (кг): "))
        height = float(input("Введите рост (см): "))
        age = int(input("Введите возраст (лет): "))
        gender = input("Пол (m - мужской, f - женский): ").strip().lower()

        if gender not in ['m', 'f']:
            print("Ошибка: укажите 'm' или 'f'.")
            return

        bmr = calculate_bmr(weight, height, age, gender)
        
        # Средний коэффициент активности (1.375 — легкая нагрузка)
        norm_calories = bmr * 1.375
        
        # Расчет БЖУ (Белки: 30%, Жиры: 30%, Углеводы: 40%)
        protein = (norm_calories * 0.30) / 4
        fat = (norm_calories * 0.30) / 9
        carbs = (norm_calories * 0.40) / 4

        print("\n--- Результаты расчета ---")
        print(f"Базовый метаболизм (BMR): {bmr:.0f} ккал")
        print(f"Поддержание веса:         {norm_calories:.0f} ккал/день")
        print(f"• Белки:   {protein:.1f} г")
        print(f"• Жиры:    {fat:.1f} г")
        print(f"• Углеводы: {carbs:.1f} г")

    except ValueError:
        print("Ошибка ввода. Пожалуйста, используйте только числа.")

if __name__ == "__main__":
    main()
