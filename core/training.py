import random
import uuid

class TarotTraining:
    def __init__(self, deck):
        self.deck = deck

    def start_session(self):
        self.session_id = uuid.uuid4()
        self.correct = 0
        self.total = 0
        return self.session_id

    def quiz(self, attribute):
        card_key, card = random.choice(list(self.deck.cards.items()))
        value = card[attribute]
        return card_key, value

    def check_answer(self, card_key, response, attribute):
        card = self.deck.get_card(card_key)
        return response in card[attribute]

