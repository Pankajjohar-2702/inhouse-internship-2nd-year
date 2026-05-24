import random

choice=["rock","paper","scissor"]

user_score = 0
computer_score = 0

print("Welcome to the Rock, Paper, Scissors Game!")
while True:
    user_choice = input("Enter your choice (rock, paper, scissor) or 'exit' to quit: ").lower()
    
    if user_choice == 'exit':
        print("Thanks for playing! Goodbye!")
        break
    
    if user_choice not in choice:
        print("Invalid choice. Please try again.")
        continue
    
    computer_choice = random.choice(choice)
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissor") or\
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    print(f"score -> you: {user_score}, computer: {computer_score}")
    
    if user_score == 3:
        print("Congratulations! You won the game!")
        break
    elif computer_score == 3:
        print("Computer won the game! Better luck next time!")
        break
