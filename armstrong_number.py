def armstrong_number(number):
    exponent = len(str(number))
    digits = [int(digit) for digit in str(number)]
    supposed_armstrong_number = 0
    
    for i in digits:
        supposed_armstrong_number = supposed_armstrong_number + (i ** exponent)
    
    return supposed_armstrong_number == number