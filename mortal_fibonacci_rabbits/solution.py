class RabbitIncubator:
    YOUNG_INDEX = -1
    IMMORTALS_INDEX = 0

    def __init__(self, months: int, age: int):
        self._months = months
        self._birth_rates = self.get_birth_rates(age)

    def breed(self) -> int:
        """
        Calculate total count of rabbits after a given amount of months.
        """

        generations = self._create_generations(len(self._birth_rates))
        # print(f"generation {1}", generations)
        for i in range(self._months - 1):
            self._grow_generations(generations)
            generations[self.YOUNG_INDEX] = self._breed_young(generations)
            generations[self.IMMORTALS_INDEX] = 0
            # print(f"generation {i + 2}", generations)
        total = sum(generations)
        return total

    def _create_generations(self, generations_count: int) -> list:
        generations = generations_count * [0]
        generations[self.YOUNG_INDEX] = 1
        return generations

    def _grow_generations(self, generations: list) -> None:
        # immortals only accumulate
        generations[self.IMMORTALS_INDEX] += generations[1]

        # shift generations
        for i in range(1, len(generations) - 1):
            generations[i] = generations[i + 1]

        # youngest generation is gone
        generations[self.YOUNG_INDEX] = 0

    def _breed_young(self, generations: list) -> int:
        # calculate new young generation based on fertility of each generation
        young = 0
        for generation, birth_rate in zip(generations, self._birth_rates):
            young += generation * birth_rate
        return young

    @classmethod
    def get_birth_rates(cls, depth: int):
        rates = [1] * (depth + 1)
        rates[cls.YOUNG_INDEX] = 0
        rates[-2] = 0
        return rates
