"""
Например, числовой корень числа 4851 — 9.
4851 → 4+8+5+1 = 18
18 → 1+8 = 9
"""

def split_digits(number):  
    digits = []
    while number > 0:  
        digit = number % 10  
        digits.append(digit)  
        number //= 10  
    ##return digits
    number = sum(digits)
    
    print(number)

split_digits(4851)

## Дальше не понимаю что использовать