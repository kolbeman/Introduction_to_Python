import sys
#print("Enter the temperature in Celsius")
#temp_in_f = input("Enter here:")
temp_in_c = sys.argv[1]
numb = float(temp_in_c)

print("You entered: ",numb,"degrees Celsius")
temp_in_f = ((9*numb)/5) + 32

print("The conversion is :",temp_in_f,"degrees Fahrenheit")

expected_answer = sys.argv[2]
real_answer = float(expected_answer)

print("This is the expected answer:", real_answer)
