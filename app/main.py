from typing import List


def get_human_age(cat_age: int, dog_age: int) -> List[int]:
    """
    Повертає приблизний "людський вік" кота та собаки на основі їхнього віку.

    Алгоритм для кота:
    - 0-14 років: 0 людських років
    - 15-23 років: +1 людський рік
    - 24-27 років: +2 людські роки
    - 28+ років: +3+ людські роки

    Алгоритм для собаки:
    - 0-14 років: 0 людських років
    - 15-23 років: +1 людський рік
    - 24-27 років: +2 людські роки
    - 28-29 років: +3 людські роки
    - далі +1 людський рік на кожні 5 років

    Параметри:
        cat_age (int): вік кота
        dog_age (int): вік собаки

    Повертає:
        List[int]: [людський вік кота, людський вік собаки]
    """

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Вік кота та собаки повинен бути цілим числом")

    # Захист від негативних чисел
    cat_age = max(0, cat_age)
    dog_age = max(0, dog_age)

    # --- Розрахунок для кота ---
    if cat_age < 15:
        human_cat = 0
    elif cat_age < 24:
        human_cat = 1
    elif cat_age < 28:
        human_cat = 2
    else:
        human_cat = 3 + (cat_age - 28) // 5

    # --- Розрахунок для собаки ---
    if dog_age < 15:
        human_dog = 0
    elif dog_age < 24:
        human_dog = 1
    elif dog_age < 28:
        human_dog = 2
    elif dog_age < 30:
        human_dog = 3
    else:
        # від 30 років +1 людський рік кожні 5 років
        human_dog = 3 + (dog_age - 30) // 5 + 1

    return [human_cat, human_dog]
