# Taking Total number of questions to do in a week
phy, chem, math = map(int, input("Enter the number of questions in each subject separated by spaces: ").split())
print("--------------------------------------------")

# Knowing the magnitude of difficulty
dp, dc, dm = map(float, input("Enter the difficulty of each subject separated by spaces: ").split())
print("--------------------------------------------")

# Knowing per day time
s1, s2, s3, s4, s5, s6, s7 = map(float, input("Enter the total study time in hours you have for each day separated by spaces (Day1, Day2, Day3...): ").split())
print("*******************************************")

# Determining Workload
w1 = phy * dp
w2 = chem * dc
w3 = math * dm

# Total time in the week (in hours)
netTime = s1 + s2 + s3 + s4 + s5 + s6 + s7

# Total time per subject (in minutes)
totalphy = (w1 / (w1 + w2 + w3)) * netTime * 60
totalchem = (w2 / (w1 + w2 + w3)) * netTime * 60
totalmath = (w3 / (w1 + w2 + w3)) * netTime * 60

# Time per question (in seconds)
tp = (totalphy / w1) * 60
tc = (totalchem / w2) * 60
tm = (totalmath / w3) * 60

# Use divmod for conversions
phy_hr, phy_min = divmod(totalphy, 60)
chem_hr, chem_min = divmod(totalchem, 60)
math_hr, math_min = divmod(totalmath, 60)

tp_min, tp_sec = divmod(tp, 60)
tc_min, tc_sec = divmod(tc, 60)
tm_min, tm_sec = divmod(tm, 60)

# Final Output
print("\n============== 📊 Weekly Study Plan Breakdown ==============")
print(f"📘 Physics   : {int(phy_hr)} hr {int(phy_min)} min")
print(f"🧪 Chemistry : {int(chem_hr)} hr {int(chem_min)} min")
print(f"📐 Math      : {int(math_hr)} hr {int(math_min)} min\n")

print("----- ⏱ Average Time Per Question -----")
print(f"Physics   : {int(tp_min)} min {int(tp_sec)} sec")
print(f"Chemistry : {int(tc_min)} min {int(tc_sec)} sec")
print(f"Math      : {int(tm_min)} min {int(tm_sec)} sec")
print("=============================================================")
