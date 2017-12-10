number = 23
running = True

while running:
    guess = int(input('Enter an integer'))

    if guess == number:
        print('Congratulation!')
        running = False;
    elif guess < number:
        print('No, low')
    else:
        print('high')

else:
    print('It\' over')
