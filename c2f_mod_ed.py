import ANSWERS.temp_conv as tc

x = input("Enter temperature in F: ")
t1 = tc.f2c(x)
print("Temperature is {} C".format(t1))
print('-' * 60)
y = input("Enter temperature in C: ")
t2 = tc.c2f(y)
print("Temperature is {} F".format(t2))