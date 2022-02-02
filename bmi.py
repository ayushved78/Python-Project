
'''BMI Challenge'''
wt = float(input("Weight? "))
ht = float(input("Height? "))
y = round(wt,2)
print(y)
# x = (round(ht,2) ** 2)
x = ht ** 2
print(x)
bmi = y/x
bmr = round(bmi,1)

print(bmr)

if bmr < 18.5:
    print("underweight")
elif bmr > 18.5 and bmr < 25:
    print("normal")
elif bmr > 25 and bmr < 30:
    print("overweight")
elif bmr > 30 and bmr < 35:
    print("obese")
else:
    print("clinicall obese")