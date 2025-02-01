#Magic8Ball.py
#Name: Jacob Oetken
#Date: 2/1/2025
#Assignment: Magic 8 Ball

#We will need random for this program, import to use this package.
import random

def main():
    print("Magic 8 Ball")
    
    #Prompt the user for their question
    question = input("Ask a yes/no question: ")

    # List of possible answers
    answers = ["Outlook hazy, look it up on Google.", "Yes, but only if you believe in unicorns.", "Signs point to pizza.", "404 - Future Not Found.", "The stars say maybe, but I'm just a ball.", "In your dreams... literally.", 
               "Unsure, ask your pet goldfish for advice.", "Without a doubt, if the moon is full.", "My sources say no, but what do they know?", "Don't count on it unless pigs start flying.", "As certain as finding socks in the laundry.", 
               "Very doubtful, like finding a needle in a haystack.", "Absolutely, just don't ask how.", "Cannot predict now, I'm on a lunch break.", "Sure, why not? Life is a mystery.", "Outlook sunny, but don't forget your umbrella.", 
               "Better not tell you now, it's a secret.", "You're making a major life decision based on what a plastic ball tells you to do? Jeez...", "Chances are as slim as a spaghetti noodle.", "Absolutely, positively, unequivocally, definitely maybe."]    
    # Select a random response
    r = random.randint(0, len(answers) - 1)  # Ensures a valid index

    response = answers[r]
    print("Magic 8 Ball says:", response)

if __name__ == '__main__':
  main()
