#!/usr/bin/env python

# A quiz game to learn python
import subprocess
import time
import random
# Title
subprocess.call(["figlet", "Trivia"])
print("\t  By Jake Leventhal\n\n")

def ask_question(q, a, first_q=False):
    ans = raw_input(q)
    if ans == a:
        print("You got it!\n")
    else:
        if first_q:
           print("Nope, sorry, the correct answer was %s!\n" % a) 
           print "OK, enough goofing off..\n"
        else:
            print("Nope, sorry!\n")
    time.sleep(2)
    subprocess.call("clear")

ask_question("Guess a numnber between 1-10\n", random.choice(range(1,11)), first_q=True)

ask_question("Who assassinated the arch duke of Austria-Hungary starting WW1?\n\ta.) Nicholas Stovenoff\n\tb.) Gavriel Princep\n\tc.) Mitch Handicunt\n\td.) Hitler\n", "b")

ask_question("In Greek Mythology, who created the horse?\n\ta.) Zeus\n\tb.) Perseus\n\tc.) Posiedon\n\td.) Hades\n", "c")
