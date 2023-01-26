num = input("Enter an integer: ")
num = int(num)

sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num //= 10

print("The sum of the digits is", sum)
