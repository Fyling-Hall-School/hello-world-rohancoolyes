import random
def calculate_points(guesses):
   """Assign points based on the number of guesses taken."""
   if guesses == 1:
       return 100
   elif guesses <= 3:
       return 75
   elif guesses <= 5:
       return 50
   elif guesses <= 7:
       return 25
   else:
       return 10
def save_score(name, score):
   """Save player name and score to an external file."""
   with open("scores.txt", "a") as file:
       file.write(f"{name}: {score}\n")
def play_game():
   """Runs the number guessing game."""
   secret_number = random.randint(1, 100)
   guesses = 0
   print("Welcome to the Number Guessing Game!")
   name = input("Enter your name: ")
   while True:
       try:
           guess = int(input("Guess a number between 1 and 100: "))
           guesses += 1
           if guess < secret_number:
               print("Too low! Try again.")
           elif guess > secret_number:
               print("Too high! Try again.")
           else:
               print(f"Congratulations, {name}! You guessed the number in {guesses} tries.")
               points = calculate_points(guesses)
               print(f"You earned {points} points.")
               save_score(name, points)
               break
       except ValueError:
           print("Invalid input. Please enter a number.")
if __name__ == "__main__":
   play_game()