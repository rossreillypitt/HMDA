import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

with open('ac_hmda_2018-2021.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

census_tracts = set()
for row in rows:
    census_tracts.add(row['census_tract'])

''' 
by year, then by tract

fields_to_use = ['derived_race', 'income', 'loan_amount', 'derived_sex'] #derived_loan_product_type', 'derived_dwelling_category'
xs_dict_by_year = {}
ys_dict_by_year = {}
census_tracts_list = list(census_tracts)
census_tracts_list = sorted(census_tracts_list)
for year in range(2018,2022):
    vs_dict = {}
    us_dict = {}
    for tract in (census_tracts_list):
        us = []
        vs = []
        for row in rows:
            if int(row['activity_year']) == year:
                if row['census_tract'] == tract:
                    values = []
                    for field in fields_to_use:
                        if field == 'income':
                            if row[field] == "NA":
                                pass
                            else:
                                values.append(int(row[field]))
                        if field == 'derived_race':
                            if row[field] == 'White':
                                values.append(0)
                            elif row[field] == 'Black or African American':
                                values.append(1)
                        elif field == 'derived_sex':
                            if row[field] == 'Female':
                                values.append(0)
                            elif row[field] == 'Male':
                                values.append(1)
                        elif field == 'loan_amount':
                            values.append(int(row[field]))
                    if len(values) == len(fields_to_use):
                        us.append(values)
                        field = 'action_taken'
                        if row[field] == '3':
                            vs.append(0)
                        elif row[field] == '1':
                            vs.append(1)
                    vs_dict[row['census_tract']] = np.array(vs)
                    us_dict[row['census_tract']] = np.array(us)
    xs_dict_by_year[year] = us_dict
    ys_dict_by_year[year] = vs_dict
'''

'''the above one might be suspect'''

fields_to_use = ['derived_race', 'income', 'loan_amount', 'derived_sex'] #derived_loan_product_type', 'derived_dwelling_category'
xs_dict_by_year = {}
ys_dict_by_year = {}
census_tracts_list = list(census_tracts)
census_tracts_list = sorted(census_tracts_list)
for year in range(2018,2022):
    vs_dict = {}
    us_dict = {}
    for tract in (census_tracts_list):
        us = []
        vs = []
        for row in rows:
            if int(row['activity_year']) == year:
                if row['census_tract'] == tract:
                    values = []
                    for field in fields_to_use:
                        if field == 'income':
                            if row[field] == "NA":
                                pass
                            else:
                                values.append(int(row[field]))
                        if field == 'derived_race':
                            if row[field] == 'White':
                                values.append(0)
                            elif row[field] == 'Black or African American':
                                values.append(1)
                        elif field == 'derived_sex':
                            if row[field] == 'Female':
                                values.append(0)
                            elif row[field] == 'Male':
                                values.append(1)
                        elif field == 'loan_amount':
                            values.append(int(row[field]))
                    if len(values) == len(fields_to_use):
                        us.append(values)
                        field = 'action_taken'
                        if row[field] == '3':
                            vs.append(0)
                        elif row[field] == '1':
                            vs.append(1)
                    vs_dict[row['census_tract']] = np.array(vs)
                    us_dict[row['census_tract']] = np.array(us)
    xs_dict_by_year[year] = us_dict
    ys_dict_by_year[year] = vs_dict

fields_to_use = ['derived_race', 'income', 'loan_amount', 'derived_sex'] #derived_loan_product_type', 'derived_dwelling_category'
xs_dict_all_years = {}
ys_dict_all_years = {}
census_tracts_list = list(census_tracts)
census_tracts_list = sorted(census_tracts_list)
for tract in (census_tracts_list):
    us = []
    vs = []
    for row in rows:
        if row['census_tract'] == tract:
            values = []
            for field in fields_to_use:
                if field == 'income':
                    if row[field] == "NA":
                        pass
                    else:
                        values.append(int(row[field]))
                if field == 'derived_race':
                    if row[field] == 'White':
                        values.append(0)
                    elif row[field] == 'Black or African American':
                        values.append(1)
                elif field == 'derived_sex':
                    if row[field] == 'Female':
                        values.append(0)
                    elif row[field] == 'Male':
                        values.append(1)
                elif field == 'loan_amount':
                    values.append(int(row[field]))
            if len(values) == len(fields_to_use):
                us.append(values)
                field = 'action_taken'
                if row[field] == '3':
                    vs.append(0)
                elif row[field] == '1':
                    vs.append(1)
            ys_dict_all_years[row['census_tract']] = np.array(vs)
            xs_dict_all_years[row['census_tract']] = np.array(us)

reduced_xs = {}
reduced_ys = {}

for tract in xs_dict_all_years:
    if len(xs_dict_all_years[tract]) <=5:
        pass
    elif len(ys_dict_all_years[tract]) == np.sum(ys_dict_all_years[tract]):
        pass
    else:
        reduced_xs[tract] = xs_dict_all_years[tract]
        reduced_ys[tract] = ys_dict_all_years[tract]

for tract in reduced_xs:
    model = LogisticRegression(solver='liblinear', C=10.0, random_state=0)
    model.fit(reduced_xs[tract], reduced_ys[tract])
    model.predict_proba(reduced_xs[tract])
    print(f'Tract: {tract}, slope: {model.coef_}, intercept: {model.intercept_}')

