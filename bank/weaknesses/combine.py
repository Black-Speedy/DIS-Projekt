

#open .csv files

lines1 = open("C:/Users/boask/Desktop/UIS_Prototype-master/bank/weaknesses/type-immunity-data.csv", 'r')
lines2 = open("C:/Users/boask/Desktop/UIS_Prototype-master/bank/weaknesses/type-weakness-data.csv", 'r')
lines3 = open("C:/Users/boask/Desktop/UIS_Prototype-master/bank/weaknesses/type-resistance-data.csv", 'r')

output = []


for i in lines1:
    j = i.strip() + ",immunity"
    output.append(j)

for i in lines2:
    j = i.strip() + ",weakness"
    output.append(j)

for i in lines3:
    j = i.strip() + ",resistance"
    output.append(j)

for i in output:
    print(i)