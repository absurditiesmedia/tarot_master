import argparse
import json
from core.tarot import TarotDeck
from core.reading import TarotReading
from core.training import TarotTraining

def main():
    parser = argparse.ArgumentParser(description='Tarot Program')
    subparsers = parser.add_subparsers(dest='command')

    analyze_parser = subparsers.add_parser('analyze')
    analyze_parser.add_argument('--spread', required=True)
    analyze_parser.add_argument('--cards', nargs='+', required=True)
    analyze_parser.add_argument('--long', action='store_true')

    train_parser = subparsers.add_parser('train')
    train_parser.add_argument('--attribute', required=True)

    args = parser.parse_args()

    deck = TarotDeck('data/deck.json')

    if args.command == 'analyze':
        reading = TarotReading(deck, f'data/spreads/{args.spread}.json')
        try:
            reading._validate_cards(args.cards)
        except ValueError as e:
          print(e)
          return
        result = reading.analyze(args.cards, args.long)
        print(json.dumps(result, indent=2))           
    elif args.command == 'train':
        training = TarotTraining(deck)
        session_id = training.start_session()
        card_key, value = training.quiz(args.attribute)
        print(f"Session ID: {session_id}")
        print(f"Card: {card_key}, Value: {value}")

if __name__ == '__main__':
    main()

