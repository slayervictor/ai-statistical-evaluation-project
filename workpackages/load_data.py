import pandas as pd
import numpy as np

def brainweight():

    data = pd.read_csv('day1/brainweight.txt', delimiter='\s+')

    data['log_body'] = np.log(data['body'])
    data['log_brain'] = np.log(data['brain'])

    return data


def calcium():

    data = pd.read_csv('day1/calcium.txt', delimiter='\s+')

    return data


def labor():

    data = pd.read_csv('day1/labor.txt', delimiter='\t')

    return data

def conidia(): 

    data = pd.DataFrame({
    'cold': [1575, 2019, 1921, 2019, 2323],
    'medium': [2003, 902, 1510, 1991, 1720],
    'warm': [1742, 1764, 787, 1470, 1769]
    })

    return data

def caffeeine():
    data = {
    "0": [652, 36, 218],
    "1-150": [1537, 46, 327],
    "151-300": [598, 38, 106],
    ">300": [242, 21, 67]
    }

    df = pd.DataFrame(data, index=["married", "divorced", "single"])

    return df

def fertilizer():
    yield_data = [10.3, 10.3, -4.95, -4.65, -6, -11]
    fert_data = ["a", "b", "a", "b", "a", "b"]
    field_data = ["a", "a", "b", "b", "c", "c"]
    

    fertilizer_data = pd.DataFrame({"Yield": yield_data, "fertilizer": fert_data, "field": field_data})

    fertilizer_data['fertilizer'] = pd.Categorical(fertilizer_data['fertilizer'])
    fertilizer_data['field'] = pd.Categorical(fertilizer_data['field'])

    return fertilizer_data

def filter():

    data = pd.read_csv('day2/filter.txt', delimiter='\t')

    return data

def poison():

    # Read the file
    with open('day2/Poison.txt', 'r') as file:
        lines = file.readlines()

    # Remove the " symbols
    lines = [line.replace('"', '') for line in lines]

    # Write the modified lines back to the file
    with open('day2/Poison.txt', 'w') as file:
        file.writelines(lines)

    data = pd.read_csv('day2/Poison.txt', delimiter='\s+')

    return data

def kalk():

    data = pd.read_csv('day3/kalk.txt', delimiter='\s+')

    return data

def sheets():

    data = pd.read_csv('day3/sheets.txt', delimiter='\s+')

    return data

def compas():

    data = pd.read_csv('day3/compas_exercise_data.csv', delimiter=',')

    return data

def root():

    # Define the data in the specified format
    data = {
        'grazed_state': ['Ungrazed'] * 20 + ['grazed'] * 20,
        'type': ['Fruit'] * 20 + ['Roots'] * 20 + ['Fruit'] * 20 + ['Roots'] * 20,
        'Fruit': [59.77, 60.98, 14.73, 19.28, 34.25, 35.53, 87.73, 63.21, 24.25, 64.34, 52.92, 32.35, 53.61, 54.86, 64.81, 73.24, 80.64, 18.89, 75.49, 46.73] + [None] * 20,
        'Roots': [6.225, 6.487, 4.919, 5.13, 5.417, 5.359, 7.614, 6.352, 4.975, 6.93, 6.248, 5.451, 6.013, 5.928, 6.264, 7.181, 7.001, 4.426, 7.302, 5.836] + [None] * 20,
        'Grazed': ['Fruit', 'Roots'] * 20 + [None] * 20,
        'Fruit': [80.31, 82.35, 105.1, 73.79, 50.08, 78.28, 41.48, 98.47, 40.15, 116.1, 38.94, 60.77, 84.37, 70.11, 14.95, 70.7, 71.01, 83.03, 52.26, 46.64] + [None] * 20,
        'Roots': [8.988, 8.975, 9.844, 8.508, 7.354, 8.643, 7.916, 9.351, 7.066, 10.25, 6.958, 8.001, 9.039, 8.91, 6.106, 7.691, 8.515, 8.53, 8.158, 7.382] + [None] * 20,
    }

    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data)

    return df



