# Tarot Master

At preent this is a command-line tarot program that can analyze tarot readings with plans to expand the functionality as described in the TODO list below and more.




## Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Place your tarot deck JSON file in the `data` directory as `deck.json`.

3. Place your spread descriptions JSON files in the `data/spreads` directory.

## Usage

### Analyze a Reading
```bash
python main.py analyze --spread=celtic-cross --cards "4w 3s 7p 2c 5w knight_w queen_c king_p ace_s 9c"
```

### Training Game [TODO]
python main.py train --attribute=short_meanings
```
[TODO]
-finish training game, including a sessionid to make this exposable as a webservice
-expose functionality as a webservice
-make demo front-end using javascript, possibility of an android app


