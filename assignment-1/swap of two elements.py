list = ['apple', 'banana', 'pineapple', 'watermelon', 'mango']
print("Original list: ",list)
index1 = 1
index2 = 2

list[index1], list[index2] = list[index2], list[index1]
print("Swapped list: ",list)
