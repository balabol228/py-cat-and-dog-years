import pytest
from app.main import get_human_age

# ===============================
# Тести для кота та собаки
# ===============================

@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        # edge cases до 15 років
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        # edge 15-24
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        # edge 24+
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (30, 35, [3, 3]),
        (40, 50, [6, 8]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age(cat_age, dog_age, expected):
    """
    Перевірка нормальних кейсів.
    Кожен випадок тестує зміну результату від попереднього значення.
    """
    result = get_human_age(cat_age, dog_age)
    assert result == expected

# ===============================
# Тести для edge cases
# ===============================
@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-10, 0),  # негативний вік кота
        (0, -5),   # негативний вік собаки
        (1000, 1000), # дуже велике значення
    ]
)
def test_get_human_age_edge(cat_age, dog_age):
    """
    Перевірка функції на некласичні або екстремальні значення.
    """
    result = get_human_age(cat_age, dog_age)
    assert isinstance(result, list)
    assert len(result) == 2
    # Для негативних чисел очікуємо 0
    if cat_age < 0:
        assert result[0] == 0
    if dog_age < 0:
        assert result[1] == 0

# ===============================
# Тести на некоректний тип даних
# ===============================
@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("15", 10),  # рядок замість int
        (15, None),  # None замість int
        ([10], 10),  # список замість int
    ]
)
def test_get_human_age_type_error(cat_age, dog_age):
    """
    Функція повинна кидати TypeError при неправильному типі даних.
    """
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
