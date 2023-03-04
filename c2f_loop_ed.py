"""Program to convert Celsius to Fahrenheit"""

while True:

    temp_str = input("Enter Celsius temp or q to quit: ")

    if temp_str == 'q':
        break
    elif temp_str == '':
        continue
    else:
        try:
            celsius = float(temp_str)
        except ValueError as err:
            print("Value Error encountered !! \n",err)
        else:
            fahrenheit = ((9 * celsius) / 5) + 32
            print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))

