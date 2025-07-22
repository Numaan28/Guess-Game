import random
print("🎯 Welcome to the Number Guessing Game!")
print("📜 Rules:")
print("1. I have selected a number between 1 and 100.")
print("2. Your job is to guess the correct number.")
print("3. After each guess, I’ll tell you whether the number is HIGHER or LOWER than your guess.")
print("4. Keep guessing until you get it right!")
print("🔢 Let's begin!\n")
n = random.randint(1, 100)
a = -1
guesses = 0
while(a != n):
    guesses +=1
    a = int(input("enter a number: "))
    if(a >n):
           print("its LOWER than you predicted")
    elif(a <n):
        print("its HIGHER than you predicted")
    else:
        print(f"🎉 You guessed it right! The number was {n}.")
        print(f"You guessed it in {guesses} attempts.")    
        

           