exp = range(32)
print(list(exp))
for i in exp:
    y = 2**i
    print("2 raised to the {}".format(i),"equals",y)
print()
ctemps = [-40, 0, 37, 100]
for f in ctemps:
    ftemp = ((9 * float(f)) / 5) + 32
    print("The temperature of {} C converts to {} F".format(f,ftemp))
print()

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   ']
clean_fruits =[fruit,fruit.lower().strip() for fruit in fruits]
print(fruits)
print(clean_fruits)

#truple_list = [(fruits,clean_fruits) for fruit in fruits]
truple_list = list(zip(fruits,clean_fruits))

print()
print(truple_list)

