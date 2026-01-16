import random 


# import the list of words 
word_bank = ["python", "java", "kotlin", "javascript", "hangman", "programming", "developer", "function", "variable", "loop"]

# make the random word selection function
word = random.choice(word_bank)

# initialize the guessed letters list and the number of attempts
guess_word = ["_"] * len(word)
attempts = 5 

# Game loop 

while attempts > 0: # ketika attempts masih lebih dari 0
    print("\nCurrent word: " + " ".join(guess_word))
    guess = input("Tebak deh :").lower()
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess: 
                guess_word[i] = guess
        print("Benar!")
    else:
        attempts -= 1 
        print(f"Salah! Kesempatan tersisa: {attempts}")
        
if "_" not in guess_word:
    print("\nSelamat! Kamu menebak kata: " + word) # perlu di edit 

else: 
    attempts == 0
    print("\nMaaf, kesempatanmu habis. Kata yang benar adalah: " + word)
            
    
# masih butuh edit, dimana harusnya kalau player udah bener udh finish aja. kecuali dia start lagi. 