if 5 > 2:
    print ('5 is indeed greater than 2')
else:
    print ('5 is not greater than 2')

def hi(name):
    print("Hi " + name + "!")

hi('Sonja')
hi('Laura')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')

for i in range(2,9):
    print(i)
