import random
import os
import time  #for pausing the message before clearing the screen

#add a function to clear the screen
def clear_screen():
    if os.name == 'nt':  
        os.system('cls')
    else:
        os.system('clear') 

#declare the hangman figure parts
figure_parts = ["O","|","/","\\","/","\\"] #head, body, limbs

#declare the function to display figure parts
def display_hangman(wrong_guesses):
   

    #add the parts based on the wrong guesses
    head = figure_parts[0] if wrong_guesses > 0 else " "
    body = figure_parts[1] if wrong_guesses > 1 else " "
    left_arm = figure_parts[2] if wrong_guesses > 2 else " "
    right_arm = figure_parts[3] if wrong_guesses > 3 else " "
    left_leg = figure_parts[4] if wrong_guesses > 4 else " "
    right_leg = figure_parts[5] if wrong_guesses > 5 else " "
    
    arms = f"{left_arm}{right_arm}"
    legs = f"{left_leg}{right_leg}"

    lines = [
        " _______",
        " |     |",
        " |     {head}",
        " |    {arms}",
        " |     {body}",
        " |    {legs}",
        " |",
        " |________"
    ]
   
    #  loop to print ASCII figure
    for line in lines:
        print(line.format(head=head, arms=arms, body=body, legs=legs))

# add list of words to guess from
with open("words.txt", "r") as file:
    words = [line.strip() for line in file.readlines()]

# choose random word
word = random.choice(words)

lives = 5
wrong_guesses = 0
guessed = [] #to store guessed letters
word_display = ["_"] * len(word) #to make underscores for the length of the word


print ("Welcome dear player to the Word Guessing Game!")
print(f"The word has {len(word)} letters.")
print (f"You have {lives} lives. Use them well. Good luck!\n")
time.sleep(2)

#main loop of game 

while lives > 0 and "_" in word_display:
    clear_screen()
    display_hangman(wrong_guesses)
    print("\nWORD:" + " ".join(word_display)) #join elements into a single string using method with a space
    print("Guessed letters so far:",",".join(guessed) if guessed else "None")
    print(f"Your lives left: {lives}")
    print("Type 'hint' for a hint!\n")

    guess = input("Guess a letter from the word:").lower() #convert letter to lowercase

    if guess == "hint":
        print(f"Hint:The first letter is... '{word[0]}'")
        time.sleep(2)
        continue

    if len(guess) != 1 or not guess.isalpha(): #checks if the only letter entered is an alphabet
     print("Please enter a single letter!\n")
     time.sleep(2)
     continue

    if guess in guessed:
        print("You already guessed that letter.\n")
        time.sleep(2)
        continue

    guessed.append(guess) #add the new guess to the guessed words list

    if guess in word:
     print("Good guess player!\n")
     for i, letter in enumerate(word):
        if letter == guess:
            word_display[i]=guess
     time.sleep(2)
    else:
        lives -= 1
        wrong_guesses +=1
        print(f"Uh oh, Wrong guess! You lose a life. Your lives left: {lives}\n")
        time.sleep(2)

#update game display after the guess
clear_screen()
display_hangman(wrong_guesses)
print("\nWORD:" + " ".join(word_display)) #join elements into a single string using method with a space
print("Guessed letters so far:", ",".join(guessed) if guessed else "None")
print(f"Your lives left: {lives}")

#to show the final display:
clear_screen()
display_hangman(wrong_guesses)
#loop ends
if "_" not in word_display:
        print("\n CONGRATULATIONS! You guessed the word:", word)
else:
        print("\n UH OH! Game Over. The word was:", word)

