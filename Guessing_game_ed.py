maxvalue = input('please enter a maximum ')
minvalue = input('please enter a minimum ')

while True:
    guess = (int(maxvalue) + int(minvalue))//2
    print("Is this your number ? ",guess)
    answer = input('please reply: ')

    if answer == 'y':
        print("I've got it!")
        print("The number is ",int(guess))
        break
    elif answer == 'h':
        print("Number is high")
        maxvalue = int(guess)
        continue
    elif answer == 'l':
        print("Number is low")
        minvalue = int(guess)
        continue
    else:
        print("Should not be here")
        break
