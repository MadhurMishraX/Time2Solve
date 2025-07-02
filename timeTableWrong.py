# Taking Total number of questions to do in a week
phy, chem, math = map(int, input("Enter the number of questions in each subject separated by spaces: ").split())
print("--------------------------------------------")
# Knowing the magnitude of difficulty
dp, dc, dm = map(float, input("Enter the difficulty of each subject separated by spaces: ").split())
print("--------------------------------------------")
# Knowing per day time
dayHours = list(map(float, input("Enter the total study time in hours you have for each day (7 values): ").split()))
print("*******************************************")
 
w1 = phy*dp
w2 = chem*dc  
w3 = math*dm
totalw = w1 + w2 + w3

netTime = sum(dayHours)*60

totalphy =  (w1/(totalw) * netTime)*60
totalchem = (w2/(totalw) * netTime)*60
totalmath = (w3/(totalw) * netTime)*60


tp = (totalphy/w1)*60
tc = (totalphy/w2)*60
tm = (totalphy/w3)*60

min_tp, sec_tp = divmod(tp, 60)
min_tc, sec_tc = divmod(tc, 60)
min_tm, sec_tm = divmod(tm, 60)

# qp, qc, qm = ()

print(f"Total time in the week: {dayHours}")
print('''                                                     ''')
print(f'''**************** Total time in ****************
      --------------------------------------------
      | Physics = {totalphy//60} hours {totalphy%60} minutes   |
      --------------------------------------------
      | Chemistry = {totalchem//60} hours {totalchem%60} minutes |
      --------------------------------------------
      | Math = {totalmath//60} hours {totalmath%60} minutes      |
                                                           ''')

print(f'''******* Ideal time to attempt per question in *******
      --------------------------------------------
      | Physics = {int(min_tp)} minutes {int(sec_tp)} seconds    |
      --------------------------------------------
      | Chemistry = {int(min_tc)} minutes {int(sec_tc)} seconds |
      --------------------------------------------
      | Math = {int(min_tm)} minutes {int(sec_tm)} seconds       |''')