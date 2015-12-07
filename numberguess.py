from random import randint

guessesTaken = 0

number = (randint(0,100))

print "I'm thinking of a number between 0 and 100"

while guessesTaken < 6:
	print "Take a guess!"
	guess = raw_input()
	guess = int(guess)

	guessesTaken +=1

	if guess < number:
		print "Your guess is too low."

	elif guess > number:
		print "Your guess is too high."

	elif guess == number:
		break
if guess == number:
	guessesTaken = str(guessesTaken)
	print "Good job! You guessed my number in" + guessesTaken + " guesses!"

elif guess != number:
	number = str(number)
	print "Nope, the number I was thinking of was" + number 

