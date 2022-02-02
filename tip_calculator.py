'''DATA CONVERSION AND TIP CALCULATOR'''

print("Tip Calculator")
tb = float(input("What was the total bill? $"))
# tb_r = round(tb,2)
tip = int(input("Amount of tip? 10/12/15 "))
n = int(input("Total number of people? "))

total = round(tb/n,2) * ((100+tip)/100)
t_r = round(total,2)
print(f"Per Head: ${t_r}")