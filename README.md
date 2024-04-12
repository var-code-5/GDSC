# Solitaire Card Game

This is a Python implementation of the classic Solitaire (also known as Klondike) card game. The game is played with a standard deck of 52 playing cards, with the objective of moving all the cards to the foundation piles.

## Features

- Fully functional Solitaire game with a command-line interface
- Supports moving cards between the stock, foundations, and piles
- Handles various game rules, such as card rank and suit requirements
- Provides feedback on invalid moves
- Allows the user to exit the game at any time

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

```
git clone https://github.com/your-username/solitaire-game.git
```

2. Navigate to the project directory:

```
cd solitaire-game
```

### Usage

1. Run the game:

```
python game_V.py
```

2. The game will start, and the initial game state will be displayed.

3. Follow the instructions provided in the "Legal Moves" section to interact with the game:
   - Press `0` to exit the game
   - Press `1` to display the legal moves
   - Press `2` to turn the stock
   - Press `3` to move a card from the stack to the foundation
   - Enter `1,[from pile],[number of elements],[to pile]` to move a pile of cards from one pile to another
   - Enter `2,[pile number]` to move a card from the stock to a pile
   - Enter `3,[pile number]` to move a card from a pile to the foundation

4. The game will continue until you have moved all the cards to the foundation piles or you choose to exit.

## Code Structure

The code consists of the following main components:

1. `game_V.py`:
   - `game` class: Manages the overall game state, including the deck, foundations, and piles.
   - `Card` class: Represents a single card with its value, suit, and rank.
   - `foundation` class: Represents a foundation pile.
   - `stock` class: Represents the stock pile.
   - `pile` class: Represents a single pile of cards.

2. `main` function:
   - Creates an instance of the `game` class and initializes the game.
   - Handles user input and executes the corresponding game actions.
   - Provides feedback on invalid moves and allows the user to exit the game.

## Dependencies

The game requires the following dependency:

- Python 3.x

## Future Improvements

- Implement a graphical user interface (GUI) for a more user-friendly experience
- Add support for multiple game modes or variations
- Implement undo/redo functionality for player actions
- Incorporate high scores and player progress tracking
