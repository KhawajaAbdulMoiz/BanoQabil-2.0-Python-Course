# Name: KHAWAJA ABDUL MOIZ
# Roll No: 70288
# Email: khawajaahmedraza4@gmail.com

#Creating TIC_TAC_TOE_GAME

# Instructions for Playing Tic Tac Toe Game:

instructions = """
This will be our Tic Tac Toe Game Board:

 1 | 2 | 3 
---|---|---
 4 | 5 | 6 
---|---|---
 7 | 8 | 9 

*Instructions:
1. Insert the spot number(1-9) to put your sign
2. You must fill all 9 spots to get result
3. Player 1 will go first
"""

# Creating a game board with 9 empty spaces to represent available spots:

sign_dict = []
for i in range(9):
  sign_dict.append(' ')

# Function to display the current state of the game board:

def print_board(sign_dict):
  board = f"""

   {sign_dict[0]} | {sign_dict[1]} | {sign_dict[2]}
  ---|---|---
   {sign_dict[3]} | {sign_dict[4]} | {sign_dict[5]}
  ---|---|---
   {sign_dict[6]} | {sign_dict[7]} | {sign_dict[8]}
  """
  print(board)


# List to keep track of already chosen spots:
  
index_list = []

# Function to take input from players:

def take_input(player_name):
    while True:
        try:
            x = int(input(f'{player_name}: '))  # Attempt to convert input to an integer
            x -= 1  # Adjust input to match list index (0-8 instead of 1-9)
            if 0 <= x < 9 and x not in index_list:  # Check if input is valid and spot is not taken
                index_list.append(x)
                return x
            elif x in index_list:
                print('Spot blocked. Please choose another spot.')
            else:
                print('Please Enter a Number Between 1 to 9')
        except ValueError:
            print('Invalid input. Please Enter a Number.')


# Function to calculate game result
def result_calculation(sign_dict, player_one, player_two):
    
    # Check for winning combinations for player X
    if (sign_dict[0] == sign_dict[1] == sign_dict[2] == 'X' or
        sign_dict[1] == sign_dict[4] == sign_dict[7] == 'X' or
        sign_dict[0] == sign_dict[4] == sign_dict[8] == 'X' or
        sign_dict[2] == sign_dict[5] == sign_dict[8] == 'X' or
        sign_dict[3] == sign_dict[4] == sign_dict[5] == 'X' or
        sign_dict[2] == sign_dict[4] == sign_dict[6] == 'X' or
        sign_dict[6] == sign_dict[7] == sign_dict[8] == 'X' or
        sign_dict[0] == sign_dict[3] == sign_dict[6] == 'X'):
        print(f'Congratulations {player_one}. You WON.!!')  # Print winning message for Player X
        quit('Thanks for Joining')  # Quit the game

    # Check for winning combinations for player O
    elif (sign_dict[0] == sign_dict[1] == sign_dict[2] == 'O' or
          sign_dict[1] == sign_dict[4] == sign_dict[7] == 'O' or
          sign_dict[0] == sign_dict[4] == sign_dict[8] == 'O' or
          sign_dict[2] == sign_dict[5] == sign_dict[8] == 'O' or
          sign_dict[3] == sign_dict[4] == sign_dict[5] == 'O' or
          sign_dict[2] == sign_dict[4] == sign_dict[6] == 'O' or
          sign_dict[6] == sign_dict[7] == sign_dict[8] == 'O' or
          sign_dict[0] == sign_dict[3] == sign_dict[6] == 'O'):
        print(f'Congratulations {player_two}. You WON.!!')  # Print winning message for Player O
        quit('Thanks for Joining')  # Quit the game
    else:
        return  # If no winner, continue the game

# Main function to execute the game:
    
def main():
    message="|...WELCOME TO TIC TAC TOE...|\n"
    print(message.center(75))
    
    player_one = input("Enter Player 1 Name: ")  # Get Player One's Name
    player_two = input("Enter Player 2 Name: ")  # Get Player Two's Name
    print(f"Thanks for Joining {player_one} and {player_two}")
    print(instructions)  # Print Game Instructions
    print(f" {player_one}'s sign is - X")
    print(f" {player_two}'s sign is - O")
    input("Press Enter to Start the Game: ")
    print_board(sign_dict)  # Print initial game board
    for i in range(0, 9):  #Loop through 9 turns, corresponding to the 9 spots on the game board.
        if i % 2 == 0:  # Check whose turn it is based on the turn count
            index = take_input(player_one)  # Player one's turn
            sign_dict[index] = 'X'  # Update game board with player one's sign
        else:
            index = take_input(player_two)  # Player two's turn
            sign_dict[index] = 'O'  # Update game board with player two's sign
        print_board(sign_dict)  # Print updated game board        
        result=result_calculation(sign_dict, player_one, player_two)  # Check for game result after each turn
        if result:
            break    
    print("Its a Tie..!!")  # If all spots are filled and no winner, declare a tie   

# Calling the main function to start the game
main()
