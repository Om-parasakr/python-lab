totalsum = 0
print("enter 10 numbers")
for i in range(1,11) :
    value = float(input(f"enter value[i] : "))
    totalsum += value
average = totalsum / 10
print(f"\nThe average of ten values is : {average}")
