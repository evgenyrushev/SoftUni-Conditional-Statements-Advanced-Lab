city = input()
volume_sales = float(input())


con = True
comm = 0

if 0 <= volume_sales <= 500:
    if city == "Sofia":
        comm = volume_sales * 0.05
    elif city == "Varna":
        comm = volume_sales * 0.045
    elif city == "Plovdiv":
        comm = volume_sales * 0.055
    else:
        con = False
elif 500 < volume_sales <= 1000:
    if city == "Sofia":
        comm = volume_sales * 0.07
    elif city == "Varna":
        comm = volume_sales * 0.075
    elif city == "Plovdiv":
        comm = volume_sales * 0.08
    else:
        con = False

elif 1000 < volume_sales <= 10000:
    if city == "Sofia":
        comm = volume_sales * 0.08
    elif city == "Varna":
        comm = volume_sales * 0.10
    elif city == "Plovdiv":
        comm = volume_sales * 0.12
    else:
        con = False

elif volume_sales > 10000:
    if city == "Sofia":
        comm = volume_sales * 0.12
    elif city == "Varna":
        comm = volume_sales * 0.13
    elif city == "Plovdiv":
        comm = volume_sales * 0.145
    else:
        con = False
else:
    con = False

if con == False:
   print("error")
else:
   print(f"{comm:.2f}")
