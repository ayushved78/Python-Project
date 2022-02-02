'''KMs to Miles'''
print("How man kms for the run?")
kms = input()
mi = float(kms) * 0.62
print(mi)

'''LEAP YEAR'''
# my solution -> X
'''
year = int(input("Year? "))
if year%4 == 0 and year%100 != 0 and year%400 != 0:
    print("Leap year")
else:
    print("Not a Leap Year")
'''
year = int(input("Year: "))
if year%4 == 0:
    if year%100 == 0:
        if year%400 ==0:
            print("Leap Year")
        else:
            print("Not Leap year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")