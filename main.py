#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

hard = 5
easy =10
number = random.randint(1, 100)
print(number)
difficulty_type = input("Choose difficulty. Type 'easy' or 'hard': ")
end_game = False
def not_call_attempts():
  print(f"You have {easy} attempts remaining to guess the number")
  
  
if difficulty_type == "easy":
  while end_game == False and easy>1:
    
    easy -=1
    guess = int(input("Make a guess:"))
    if guess > number or guess < number:
      
      not_call_attempts()
    
    if guess > number:
      print("Too high")
      print("Guess again")
    elif guess<number:
      print("Too low")
      print("Guess again")
    elif guess == number:
      print(f"You found the guess number is: {number}")
      end_game = True
    else:
      end_game = True
elif difficulty_type == "hard":
  while end_game == False and hard > 1:
    
    hard -= 1
    guess = int(input("Make a guess:"))
    if guess > number or guess < number:
      print(f"You have {hard} attempts remaining to guess the number")

    if guess > number:
      print("Too high")
      print("Guess again")
    elif guess<number:
      print("Too low")
      print("Guess again")

    elif guess == number:
      print(f"You found the guess number is: {number}")
      end_game == True
    else:
      end_game = True
else:
  end_game = True
      