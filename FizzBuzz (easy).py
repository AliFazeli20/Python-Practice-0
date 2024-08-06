# FizzBuzz program prints numbers from 1 to 100.
# For multiples of 3, it prints "Fizz" instead of the number.
# For multiples of 5, it prints "Buzz".
# For numbers that are multiples of both 3 and 5, it prints "FizzBuzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")  # Multiple of both 3 and 5
    elif i % 3 == 0:
        print("Fizz")  # Multiple of 3
    elif i % 5 == 0:
        print("Buzz")  # Multiple of 5
    else:
        print(i)  # Not a multiple of 3 or 5
