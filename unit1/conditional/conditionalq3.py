player1 = input()
player2 = input()

if player1 == player2:
    print("Tie Game.")

elif 'Rock' in player1:
    if 'Paper' in player2:
        print("Player 2 Wins.")
    else: # Player 2 input HAS to be scissors to pass through this condition
        print("Player 1 Wins.")

elif 'Paper' in player1:
    if 'Scissors' in player2:
        print("Player 2 Wins.")
    else: # Player 2 input HAS to be rock to pass through this condition
        print("Player 1 Wins.")

elif 'Scissors' in player1:
    if 'Rock' in player2:
        print("Player 2 Wins.")
    else: # Player 2 input HAS to be paper to pass through this condition
        print("Player 1 Wins.")