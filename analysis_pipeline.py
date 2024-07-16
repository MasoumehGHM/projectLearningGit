import sys
import numpy as np

inputs = sys.argv
data_file = inputs[1]

data_dict = {'county_name':[], 'population':[], 'area':[]}
with open(data_file, 'r') as df:
    for line in df:
        name, _, pop, area = line.strip('\n').split(',')
        data_dict['county_name'].append(name)
        data_dict['population'].append(int(pop))
        data_dict['area'].append(float(area))
        
# Q1: mean and std of population
pop_mean = np.mean(data_dict['population'])
pop_std = np.std(data_dict['population'])
print(f"population mean:, {pop_mean}!")
print(f"population stdev:, {pop_std}!")

# Q2: List three largest populations
zip_name_pop = list(zip(data_dict['county_name'],data_dict['population']))
#three_largest_county = [x for x,_ in  sorted(zip_name_pop,reverse = True, key=lambda x:x[1])][0:3]
three_largest_county_withpop = sorted(zip_name_pop,reverse = True, key = lambda x : x[1])[0:3]
print("3 largest population counties:")
print(three_largest_county_withpop)

#Q3 
zip_name_area = list(zip(data_dict['county_name'],data_dict['area']))
#three_largest_county = [x for x,_ in  sorted(zip_name_pop,reverse = True, key=lambda x:x[1])][0:3]
three_largest_county_witharea = sorted(zip_name_area,reverse = True, key = lambda x : x[1])[0:3]
print("3 largest area counties:")
print(three_largest_county_witharea)
