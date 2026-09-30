num = int(input("enter a number a number between 1 to 10 : "))
if num>=1 and num <=10 :
 factorial = 1 
for i in range(1,num) :
    factorial = factorial * i
print(factorial)

