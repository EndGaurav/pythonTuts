import emoji
print("Guess the number between 0 to 100 below :-")
print("You have only 6 number of guesses")
target = 18
guesses = 0

while guesses < 6:
    guesses = guesses + 1
    i = int(input("Enter the number: "))
    if i > target and i > 40:
        print("your guessing number is very high")
        continue

    elif i > target and i >= 20:
        print("This guess is bit high number")
        continue

    elif i < 18 and i > 10:
        print("very close")
        continue

    elif i < target and i < 10:
        print("Your guessing number is very low")
        continue

    elif i == target:
        print("🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
        print("Hurrrahhh you have guessed it right🎉🎊 and that number is:", i)
        print("you have gusessed it in", guesses)
        break


if i != target and guesses >= 6:
    print("-----------------------------------------------------------------------------------------------------")
    print("The number of chances get finished.")
    print("GAME OVER!")
    print("have a Better luck next time!👍")

