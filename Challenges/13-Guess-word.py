# Step 1

import random
list_of_words = ["apple", "orange", "snake"]
chosen_word = random.choice(list_of_words)
# print(f"The chosen word is '{chosen_word}'")

# Step 2

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    # display.append("*")
    display += "_"
print(display)

# Step 3
lives = 4
print(f"You have {lives} lives.")

while True:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already tried this letter {guess}.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life. You have {lives} left")

    print(display)

    if lives == 0:
        print("No more lives left. You have lost.")
        break
    if "_" not in display:
        print("Congrats! You won.")
        break
