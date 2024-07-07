import json

class TarotReading:
    def __init__(self, deck, spread_file):
        self.deck = deck
        self.spread_file=spread_file
        with open(spread_file, 'r') as file:
            self.spread = json.load(file)
            

    def analyze(self, cards, long_format=False):
        reading = []
        for pos, card_key in zip(self.spread, cards):
            card = self.deck.get_card(card_key)
            pos['card'] = {
                'name': card['name'],
                'short_meanings': card['short_meanings']
            }
            
            if long_format:
                pos['card'].update(card)
            reading.append(pos)
        return reading
        
    def _validate_cards(self, cards):
        
        if len(cards) != len(self.spread):
            raise ValueError(f"Expected {len(self.spread)} cards for the '{self.spread_file}' spread, but got {len(cards)}.")
        for card in cards:
            if self.deck.get_card(card) is None:
                raise ValueError(f"Invalid card key: {card}")
        seen_cards = set()
        for card in cards:
            if self.deck.get_card(card) is None:
                raise ValueError(f"Invalid card key: {card}")
            if card in seen_cards:
                raise ValueError(f"Duplicate card key: {card}")
            seen_cards.add(card)                
                
