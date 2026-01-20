import itertools

print("A\tB\tA and B\tA or B\tnot A")

print("-"*40)

for A, B in itertools.product([True, False], repeat=2):
    print(f"{A}\t{B}\t{A and B}\t{A or B}\t{not A}")