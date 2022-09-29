number = 39890

first = number // 10000
second = number // 1000 % 10
third = number // 100 % 10
fourth = number // 10 % 10
fifth = number % 10

pattern = '{:>0}{:>3}{:>3}{:>3}{:>3}'

print(pattern.format(first,second, third, fourth, fifth))


