# Gacha Command

import random

class Gacha:
    def __init__(self, items):
        self.items = items

    def draw(self, number_of_draws=1):
        return random.sample(self.items, number_of_draws)

# Example usage:
# gacha = Gacha(['Item 1', 'Item 2', 'Item 3'])
# print(gacha.draw(2))
