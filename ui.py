import os
from core import Game


def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_board(game):
    """Display the 15x15 board with row and column numbers."""
    print("\n   ", end="")
    for col in range(1, 16):
        print(f"{col:2d}", end=" ")
    print()

    for row in range(15):
        print(f"{row + 1:2d} ", end="")
        for col in range(15):
            cell = game.board[row][col]
            if cell is None:
                print(" . ", end="")
            else:
                print(f" {cell[0].upper()} ", end="")
        print()
    print()


def get_valid_coordinates():
    """Get valid row and column coordinates from user input."""
    while True:
        try:
            row_input = input("Enter row (1-15): ")
            col_input = input("Enter column (1-15): ")
            row = int(row_input)
            col = int(col_input)
            if 1 <= row <= 15 and 1 <= col <= 15:
                return row - 1, col - 1
            else:
                print("Error: Coordinates must be between 1 and 15. Try again.")
        except ValueError:
            print("Error: Please enter valid numbers for row and column.")


def display_turn(game):
    """Display whose turn it is."""
    print(f"\nCurrent turn: {game.current_player.capitalize()}")


def display_winner(game):
    """Display the winner or draw message."""
    if game.winner:
        print(f"\n{'='*40}")
        print(f"  {game.winner.capitalize()} wins!")
        print(f"{'='*40}")
    elif game.is_full():
        print("\n{'='*40}")
        print("  It's a draw!")
        print(f"{'='*40}")
    else:
        return False
    return True


def play_game():
    """Main game loop for console play."""
    game = Game()
    
    while not game.winner and not game.is_full():
        clear_screen()
        display_board(game)
        display_turn(game)
        
        row, col = get_valid_coordinates()
        
        if not game.make_move(row, col):
            print("\nInvalid move! That cell is already taken or out of bounds.")
            input("Press Enter to try again...")
            continue
    
    clear_screen()
    display_board(game)
    display_winner(game)


if __name__ == "__main__":
    play_game()
