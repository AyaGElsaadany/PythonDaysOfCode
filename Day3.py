# Write a function to count the number of voewls in a given string

def count_voewls(str):
    count = 0
    voewl = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(str)-1):
        if str.lower()[i] in voewl:
            count += 1
    return count



print(count_voewls("ice CrEAm"))
