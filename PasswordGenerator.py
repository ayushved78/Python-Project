import random
letters = []
alpha = 'abcdefghijklmnopqrstuvwxyz'
# for i in range(0, 26):
#     letters.append(alpha)
#     alpha = chr(ord(alpha) + 1)
# # print(alpha)
for i in alpha:
    letters.append(i)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '$', '.']

password = []

nol = int(input("No of Letters: "))
non = int(input("Number of numbers: "))
nos = int(input("Number of Symbols: "))
for char in range(1, nol+1):
    password += random.choice(letters)
for char in range(1, non+1):
    password.append(random.choice(numbers))
for char in range(1, nos+1):
    password.append(random.choice(symbols))
# print(password)
random.shuffle(password)
# print(password)

psd = ""
for char in password:
    psd += char

print(psd)