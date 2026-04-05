class Marketplace:
    def __init__(self):
        self.listings = {}

    def create_listing(self, card_id, price):
        if card_id in self.listings:
            return 'Listing already exists.'
        self.listings[card_id] = price
        return f'Created listing for card {card_id} at price {price}'

    def get_listings(self):
        return self.listings

    def remove_listing(self, card_id):
        if card_id not in self.listings:
            return 'Listing not found.'
        del self.listings[card_id]
        return f'Removed listing for card {card_id}'

    def buy_card(self, card_id, user_balance):
        if card_id not in self.listings:
            return 'Listing not found.'
        price = self.listings[card_id]
        if user_balance < price:
            return 'Insufficient funds.'
        del self.listings[card_id]
        return f'Purchased card {card_id} for {price}'
