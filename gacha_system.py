import random

class GachaSystem:
    def __init__(self, biases=[]):
        self.biases = biases
        self.cards = []  # List to hold available cards

    def add_card(self, card):
        """ Adds a card to the gacha system """
        self.cards.append(card)

    def pull_card(self):
        """ Simulates pulling a card from the gacha system """
        if not self.cards:
            raise Exception("No cards available")
        # Simulate gacha roll
        card = random.choice(self.cards)
        return card

    def pack_pull(self, pack_size=10):
        """ Simulates pulling a pack of cards """
        return [self.pull_card() for _ in range(pack_size)]

    def recycle_cards(self, cards):
        """ Recycles cards and potentially obtain rewards """
        return [card for card in cards if card not in self.biases]  # Example of recycling efforts

    def check_bias(self, pulled_card):
        """ Checks if the pulled card matches any bias """
        return pulled_card in self.biases

# Example of usage
if __name__ == '__main__':
    gacha = GachaSystem(biases=['Bias1', 'Bias2'])
    gacha.add_card('Card1')
    gacha.add_card('Card2') 
    gacha.add_card('Bias1')
    pulled_card = gacha.pull_card()  
    print(f'Pulled Card: {pulled_card}')
    if gacha.check_bias(pulled_card):
        print('Congrats on pulling your bias!')
    else:
        print('No bias this time.')
