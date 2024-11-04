import random

# Sample questions
questions = [
    ("Would you rather be able to fly or be invisible?", "fly", "invisible"),
    ("Would you rather always have to tell the truth or always lie?", "truth", "lie"),
    ("Would you rather have the ability to read minds or teleport?", "read minds", "teleport"),
    ("Would you rather live in the ocean or in space?", "ocean", "space"),
]

def display_question(question):
    print(question[0])
    print(f"1: {question[1]}")
    print(f"2: {question[2]}")
    choice = input("Enter 1 or 2: ")
    return choice

def main():
    print("Welcome to the Would You Rather Game!")
    while True:
        question = random.choice(questions)
        choice = display_question(question)
        
        if choice == "1":
            print(f"You chose: {question[1]}")
        elif choice == "2":
            print(f"You chose: {question[2]}")
        else:
            print("Invalid choice. Please enter 1 or 2.")
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
