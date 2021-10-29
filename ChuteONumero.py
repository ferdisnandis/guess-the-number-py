#Chute o número - O bot escolherá um número e você terá que adivinhar!!
import random

secret_number = random.randrange(1, 100)

guess = int(input("Guess a number from 1 to 100: "))

print("Can I give some hint?")

while secret_number != guess:
    guess = int(input("Guess a number from 1 to 100: "))

    if(guess > secret_number):{
    print("Your guess is high! Please, try again")
} 
    elif(guess < secret_number):{
    print("Your guess is low! Please, try again")
}
    elif(guess == secret_number):{
    print("Congratulations! You got it right!")
}