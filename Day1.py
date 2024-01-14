# Create a program that swaps the values of two variables

val1 = input("enter first value : ")
val2 = input("enter second value : ")

print("before swap value 1 is {} value 2 is {}". format(val1, val2))

temp = val1
val1 = val2
val2 = temp

print("after swap value 1 is {} value 2 is {}". format(val1, val2))