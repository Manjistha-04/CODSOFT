import random

def play_game():
    user_score = 0
    computer_score = 0

    
    print("\nWelcome to Rock-Paper-Scissors!")
    print("Game Rules:")
    print("- Rock beats Scissors")
    print("- Scissors beat Paper")
    print("- Paper beats Rock")
    
    while True:
        print("\n" + "="*40)
        print(f"Current Score - You: {user_score} | Computer: {computer_score}")
        print("="*40)
        
        
        while True:
            user_choice = input("\nChoose one: rock, paper, or scissors (or 'quit' to exit): ").lower()
            if user_choice in ['rock', 'paper', 'scissors', 'quit']:
                break
            print("Invalid choice. Please enter rock, paper, or scissors.")
        
        if user_choice == 'quit':
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("Congratulations! You won the game!")
            elif user_score < computer_score:
                print("Computer won the game. Better luck next time!")
            else:
                print("The game ended in a tie!")
            print("\nThanks for playing!")
            break
        
        
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"\nYour choice: {user_choice.capitalize()}")
        print(f"Computer's choice: {computer_choice.capitalize()}")
        
        if user_choice == computer_choice:
            print("\nIt's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print(f"\n{user_choice.capitalize()} beats {computer_choice}. You win!")
            user_score += 1
        else:
            print(f"\n{computer_choice.capitalize()} beats {user_choice}. Computer wins!")
            computer_score += 1
        
        
        while True:
            play_again = input("\nWould you like to play again? (yes/no): ").lower()
            if play_again in ['yes', 'no']:
                break
            print("Please enter 'yes' or 'no'.")
        
        if play_again == 'no':
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("Congratulations! You won the game!")
            elif user_score < computer_score:
                print("Computer won the game. Better luck next time!")
            else:
                print("The game ended in a tie!")
            print("\nThanks for playing!")
            break


play_game()