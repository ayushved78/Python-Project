# scs = input("Scores: ")
# sc = scs.split(",")
sc = [12,34,78,91,13,16,18]
for n in range(0,len(sc)):
    sc[n] = int(sc[n])

high = sc[0]
for i in range(0,len(sc)):
    if high < sc[i]:
        high = sc[i]

print(high)

'''FIZZ BUZZ CHALLENGE'''
n = int(input("Ranges till? "))
for i in range(1,n+1):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("BUZZ")
    elif i%3 == 0:
        print("FIZZ")
    else:
        print(i)