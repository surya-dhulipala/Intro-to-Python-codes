number = [0,1,2,3,4,5]
square = [x **2 for x in number]
cube = [x **3 for x in number]

pattern = '{:>0}{:>10}{:>10}'
print(pattern.format("number","square", "cube"))

pattern = '{:>5}{:>10}{:>10}'

for i in number:
    print(pattern.format(i, i**2, i**3))

