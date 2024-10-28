import random

word_list = ["abstract","emulate", "backend", "gateway", "integer", "segment","boolean", "compile", "override", "fragment", "inherit",
             "module", "trigger","storage", "pointer", "version", "operand", "operator", "parsing", "queue","process", "execute", "dynamic",
             "syntax", "package", "runtime", "upgrade","testing", "dataset"]
attempts = 5
chosen_word = random.choice(word_list)
display = ['_' for _ in chosen_word]
print(" ".join(display) + "\n")

game_over = False
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()

    if guessed_letter in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guessed_letter:
                display[position] = guessed_letter
    else:
        print("Letter not found!")
        attempts -= 1
        print(f"Attempts left: {attempts}")
        if attempts == 0:
            game_over = True
            print("You Failed!! The word was:", chosen_word)
    
    print(" ".join(display))

    if '_' not in display:
        game_over = True
        print("You Won!")
