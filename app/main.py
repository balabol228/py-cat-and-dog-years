def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    def cat(age: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // 4

    def dog(age: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        if age < 29:
            return 2
        return 3 + (age - 29) // 5

    return [cat(cat_age), dog(dog_age)]
