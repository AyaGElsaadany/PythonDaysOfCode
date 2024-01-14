# Write a program to find the sum of all elements in a list

in_list = input("enter nums : ").split()
float_in_list = [float(str) for str in in_list]

print(sum(float_in_list))
