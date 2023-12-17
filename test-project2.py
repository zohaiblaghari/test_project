num = int(input('Enter a number: '))
if num < 0:
    print("number is negatve.")
else:
    factorial = 1
    while num > 0:
        factorial*=num
        num -= 1
    print(f'the factorial is: {factorial}')
