rows = 10
for j in range(1, rows + 1):
    print("*" * j, " " * (rows + 1 - j),end = '') # # Part a : left sided triangle with inceasing *
    print("*" * (rows + 1 - j), end = '') # Part b: left sided triangle with decreasing *
    print(" " * (2*j), "*" * (rows + 1 - j), end = '') # # Part c: right sided triangle with decreasing *
    print(" " * (rows + 1 - j), "*" * j) # # Part d: right sided triangle with increasing *
