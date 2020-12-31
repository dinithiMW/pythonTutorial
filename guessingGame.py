secret_number = 6
guessing_count = 3
count = 0

while count < guessing_count:
    guess = int(input("guess? "))
    count += 1
    if guess == secret_number:
        print("you won")
        break
else:
    print("sry You haven't another chanse")
