import json

class TarotDeck:
    def __init__(self, deck_file):
        with open(deck_file, 'r') as file:
            self.cards = json.load(file)

    def get_card(self, card_key):
        return self.cards.get(card_key, None)

