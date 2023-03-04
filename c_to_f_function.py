def c2f(celsius):
    temp=float(celsius)
    fahrenheit = ((9 * temp) / 5) + 32
    return fahrenheit

temperatures = [-40, 0, 37, 100]

for temp in temperatures:
    in_temp = float(temp)
    out_temp = c2f(in_temp)
    print("The temperature {:.1f} C equals {:.1f} F".format(in_temp,out_temp))