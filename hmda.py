import pandas as pd

flag = True
hmda_cols = []
ac_hmda = []
with open("2021_lar.txt") as o:
    for line in o:
        while flag:
            hmda_cols.append(line.strip())
            hmda_cols = hmda_cols[0].split("|")
            flag = False
        if line[41:46] == '42003':
            ac_hmda.append(line.strip())
    ac_hmda = [item.split("|") for item in ac_hmda]

ac_hmda_dF = pd.DataFrame(ac_hmda, columns=hmda_cols)
ac_hmda_dF.to_csv("ac_hmda.csv", index=False)
#the end for now


