########### imports
import sys
import numpy as np


########## functions

def imput_data():
    # Get data file if any
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return -1

def read_data(data_path):
    data_dict = {'county_name':[], 'population':[], 'area':[]}
    with open(data_path, 'r') as df:
        for line in df:
            name, _, pop, area = line.strip('\n').split(',')
            data_dict['county_name'].append(name)
            data_dict['population'].append(int(pop))
            data_dict['area'].append(float(area))
    return data_dict

def mean_std_list(list1):
    return np.mean(list1), np.std(list1)

def largest_three_list(list1, col=1):
    return sorted(list1, key = lambda x : x[col])[-3:0]
    
##########
# main
def main():
    # get data path file
    data_path = imput_data()
    if data_path == -1:
        print("No data file is given.")
        return 0 
    if !exists(data_path):
        print("The data path does not exits.")
        return 0 
    
    # Get data
    dict = read_data(data_path)
    mu, sigma = mean_std_list(dict['population'])
    pop_three_largest = largest_three_list(list(zip(dict['county_name'],dict['population'])), col=1)
    area_three_largest = largest_three_list(list(zip(dict['county_name'],dict['area'])), col=1):
    
    # Print result
    print(f"population mean:, {mu}!")
    print(f"population stdev:, {sigma}!")
    print("3 largest population counties:")
    print(pop_three_largest)
    print("3 largest area counties:")
    print(area_three_largest)
    
    return 0
    
    
        
        



