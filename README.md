# Rock, Paper, Scissors Game

This is a simple command-line Rock, Paper, Scissors game implemented in Python. The game allows you to play against the computer and keep track of the win/loss/tie statistics.

## Features

- Play a game of Rock, Paper, Scissors against the computer.
- View statistics of how many times you, the computer, or both have won.

## How to Run

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Gordon-Burns/rock-paper-scissors.git
    cd rock-paper-scissors
    ```

2. **Run the game**:

    ```bash
    python main.py
    ```

3. **Follow the on-screen prompts**:
   - Choose `1` to play the game.
   - Choose `2` to view the statistics.

## How It Works

- The game randomly chooses between "Rock", "Paper", or "Scissors" for the computer.
- The user makes their choice via input.
- The game then determines the outcome and stores the result in a `results.txt` file.
- The statistics option reads from this file to display the overall results.

## Dependencies

- Python 3.x
- No external libraries required

## Files

- `main.py`: The main script to run the game.
- `functions.py`: Contains the game logic and utility functions.
- `results.txt`: Automatically generated and used to store the results of the games.

## License

This project is licensed under the MIT License.
