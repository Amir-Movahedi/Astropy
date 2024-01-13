

import sys
import csv
import numpy as np 
from astropy.io import fits

def main():
    # Check if an argument is provided
    if len(sys.argv) != 2:
        print("Usage: python myscript.py input_value")
        sys.exit(1)

    # Get the input value from the command line
    input_value = sys.argv[1]

    # Your code here
    return input_value


def find_extrema(x, y):
    # Finding the index of minimum and maximum
    min_index = np.argmin(y)
    max_index = np.argmax(y)

    # getting the points of minimum and maximum
    min_point = (x[min_index], y[min_index])
    max_point = (x[max_index], y[max_index])

    return max_point, min_point


def class_pulsar(average, max_point, min_point):
    #average
    a = np.abs(max_point - average)
    b = np.abs(min_point -average)

    ratio_one = a / b
    ratio_two = b / a
    #clasification
    if (ratio_one <= 1.2) and (ratio_two >= 0.8):
        #classification = 'group1'
        classification = 1
    elif a > b:
        #classification = 'group2'
        classification = 2
    elif b < a:
        #classification = 'group3'
        classification = 3
    
    return classification









if __name__ == "__main__":
    
    address = main()

    file = fits.open(address)

    #NAME
    pulsarNAME = file[0].header['SRC_NAME']
    #FREQUENCY
    pulsarFREQUENCY = file['HISTORY'].data['CTR_FREQ'][0]


    #data
    data = file['SUBINT'].data

    flux_data = data['DATA']
    V = flux_data[0, 3, :]


    max_point, min_point = find_extrema(np.linspace(0, 10, len(V[0])), V[0])
    average = np.mean(V[0])


    pulsarCLASS = class_pulsar(average, max_point[1], min_point[1])


    #print(pulsarNAME, pulsarFREQUENCY, pulsarCLASS)

    #CSV name
    file_path = 'data.csv'


    new_data = [pulsarNAME, "{:.2f}".format(pulsarFREQUENCY), pulsarCLASS]

    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_data)

    print(f'Data has been added to {file_path}')


