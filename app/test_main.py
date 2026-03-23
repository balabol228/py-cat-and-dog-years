import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    ("cat_age", "dog_age", "expected"),
    [
        (0, 0, [0, 0]),
        (1, 1, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (16, 16, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (30, 35, [3, 3]),
        (40, 50, [6, 8]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    result: list[int] = get_human_age(cat_age, dog_age)
    assert result == expected


def test_cat_edge_cases() -> None:
    assert get_human_age(14, 0)[0] == 0
    assert get_human_age(15, 0)[0] == 1
    assert get_human_age(24, 0)[0] == 2
    assert get_human_age(28, 0)[0] == 3


def test_dog_edge_cases() -> None:
    assert get_human_age(0, 14)[1] == 0
    assert get_human_age(0, 15)[1] == 1
    assert get_human_age(0, 24)[1] == 2
    assert get_human_age(0, 29)[1] == 3
