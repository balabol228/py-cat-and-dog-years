from app.main import get_human_age


def test_should_return_zeros_when_ages_are_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zeros_before_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_after_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_one_before_second_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_after_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_correct_ages_for_large_numbers() -> None:
    assert get_human_age(100, 100) == [21, 17]
