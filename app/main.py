def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    def convert(age: int, step: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1

        human_years: int = 2
        human_years += (age - 25) // step + 1
        return human_years

    cat_human: int = convert(cat_age, 4)
    dog_human: int = convert(dog_age, 5)

    return [cat_human, dog_human]
