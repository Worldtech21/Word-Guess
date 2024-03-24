import random


words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig',\
          'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine',\
              'orange', 'papaya', 'quince', 'raspberry', 'strawberry',\
                  'tangerine', 'watermelon']
word = random.choice(words)

chances = 12
while chances >0:
    print("List of Words to guess from:")
    print(words)  
    guess = input("Enter your guess: ")
    if guess == word:
        print("Congratulations! You have guessed the word.")
        break
    else:
        chances -= 1
        print("Incorrect guess. You have", chances, "chances left.")
        if chances == 0:
            print("Sorry! You have run out of chances. The word was", word)
            break
