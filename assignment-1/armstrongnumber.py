num = int(input("Enter a number :"))
numstr = str(num)
numdigits = len(numstr)
armstrongsum = 0
for digitchar in numstr :
    digit = int(digitchar)
    armstrongsum = armstrongsum + (digit ** numdigits)
    if armstrongsum == num :
        print(num,"is an Armstrong number!")
    else :
        print(num,"is NOT an armstrong number.")
