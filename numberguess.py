from random import randint

number = (randint(0,100))

guess = raw_input("Guess a number between 0 and 100")
if guess == number:
    print "WITCH!!"
else:
	print "Nope, wrong guess."
