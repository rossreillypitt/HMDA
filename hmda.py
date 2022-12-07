import pandas as pd
import sys

#if len(sys.argv) == 1:
#    print("please enter a year")

#year = sys.argv[1]

flag = True
hmda_cols = []
ac_hmda = []
for year in range(2018, 2021):
    print(year)
    input_file_name = f'{year}_lar.txt'
    with open(input_file_name) as o:
        for line in o:
            while flag:
                hmda_cols.append(line.strip())
                hmda_cols = hmda_cols[0].split("|")
                flag = False
            if line[41:46] == '42003':
                ac_hmda.append(line.strip())
    
ac_hmda = [item.split("|") for item in ac_hmda]
ac_hmda_dF = pd.DataFrame(ac_hmda, columns=hmda_cols)
#    ac_hmda_dF.to_csv(f"PA_hmda_data_{year}.csv")

staging_list = []
desired_output_columns = ['activity_year', 'county_code', 'census_tract', 'derived_loan_product_type', 'derived_dwelling_category', 'derived_ethnicity', 'derived_race', 'derived_sex', 'action_taken', 'loan_purpose', 'loan_amount', 'hoepa_status', 'property_value', 'occupancy_type', 'income', 'debt_to_income_ratio']
for x in range(len(ac_hmda_dF)):
    if ac_hmda_dF.loc[x, 'loan_purpose'] == '1':
        if ac_hmda_dF.loc[x, 'derived_dwelling_category'] == 'Single Family (1-4 Units):Site-Built' or ac_hmda_dF.loc[x, 'derived_dwelling_category'] == 'Single Family (1-4 Units):Manufactured':
            if ac_hmda_dF.loc[x, 'action_taken'] == '1' or ac_hmda_dF.loc[x, 'action_taken'] == '3':
                if ac_hmda_dF.loc[x, 'occupancy_type'] == '1':
                    staging_list.append(ac_hmda_dF.loc[x, desired_output_columns])

output_dF = pd.DataFrame(staging_list)
output_dF.reset_index(drop=True, inplace=True)
print(output_dF)

output_dF.to_csv("ac_hmda_2018-2020.csv", index=False)
#the end for now