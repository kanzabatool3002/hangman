#In this program we create hangman game.

keepgoing="y" #If the user inputs 'y' the loop repeats
# If the condition true, the loop starts executing
while (keepgoing == "y"):
    import random  #Shuffle a list
    def hangman():
        names=["pakistan","thailand","china","singapore","afghanistan","america","malaysia","mexico","nigeria","canada","panama","colombia","greece","zimbabwe"]
        word = random.choice(names)  #returns a random string from the list
        turns = 10  #Player gave incorrect answer 10 times
        guesses = ""
        entry=("abcdefghijklmnopqrstuvwxyz")
        #Player only enter these words
        print("chose alphabets from \na b c d e f g h i j k l m n o p q r s t u v w x y z")
        print("\t")
        while len(word)>0:
            words = ""
            missed = 0
 
            for char in word:
                if char in guesses:
                    words = words+char #if the alphabet in word is same the user entered it print the alphabet
                else:
                    words=words+"-" #if the alphabet is not same it print -
        #when the user guess the correct word, it print the word 
            if words == word: 
                print(words)
                print("You win :)")
                break

        #here we take guesses from the user
            print("guess the word", words)
            guess = input()
            print("\t")
            if guess in entry:
                if guess in guesses:
                    print("You already guess the alphabet",guesses) #if the player entered the same guess again we print this
                guesses = guesses+guess
            else:
                print("Please enter given alphabets")
                guess = input()
            if guess not in word: #if guess is not in the word it minus 1 from 10 turns
                turns =turns-1

                if turns == 9: 
                    print("9 attempts left")
                    print("------------")
                if turns == 8: # shows head 
                    print("8 attemptss left")
                    print("------------")
                    print("     O      ")
                if turns == 7: # shows head and torso
                    print("7 attempts left")
                    print("------------")
                    print("     O      ")
                    print("     |      ")
                if turns == 6: # shows head,torso and one leg
                    print("6 attempts left")
                    print("------------")
                    print("     O      ")
                    print("     |      ")
                    print("    /       ")
                if turns == 5: #shows head,torso and both legs
                    print("5 attempts left")
                    print("------------")
                    print("     O      ")
                    print("     |      ")
                    print("    / \     ")
                if turns == 4: #shows head,torso,both legs and one hand
                    print("4 attempts left")
                    print("------------")
                    print("    \O      ")
                    print("     |      ")
                    print("    / \     ")
                if turns == 3: #Shows head,torso,both legs and both hands
                    print("3 attempts left")
                    print("------------")
                    print("    \O/     ")
                    print("     |      ")
                    print("    / \     ")
                if turns == 2: #shows head,torso,both legs,both hands and roap
                    print("2 attempts left")
                    print("------------")
                    print("    \O/ |   ")
                    print("     |      ")
                    print("    / \     ")
                if turns == 1:
                    print("only 1 attempt left!!!") # shows the man hanged
                    print("-------------------")
                    print("        \O/_|      ")
                    print("         |         ")
                    print("        / \        ")
                if turns == 0:
                    print("Sorry,you ran out of tries. The word was " + word + ". Good luck for next time!")
                    break


    name=input("Enter your name: ")
    print("Welcome",name,"!")
    print("Play hangman with me!")
    print("Try to guess the name of countries in less than 10 attempts")
    hangman()
    keepgoing=input("Do you want to play again? press 'y' for yes")   

