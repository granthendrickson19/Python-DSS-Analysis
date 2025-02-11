import numpy as np
import sys
import argparse
import yaml
from numpy import genfromtxt


if __name__ == "__main__":
    parser  = argparse.ArgumentParser(
        description="This command line program will take an input CSV file and apply DSS analysis "
        )
    parser.add_argument('-d','--data',required=True, help='Data file to analyze')
    parser.add_argument('-m','--model',required=True, help='Model YAML file for data predicition')
    args = parser.parse_args(sys.argv[1:])
    my_data = genfromtxt(args.data, delimiter =',',skip_header=1)
    with open(args.model,'r') as f:
        inputs = yaml.safe_load(f)
    
#parser.add_argument('-o','--output',required=True, help='Output file name')
###
#print (args.data)
#print (args.model)

#print(my_data)


def data_normalizer(data, inputs):
    """Normalizes Data to Users Input, Creates conserved quantity for DSS analysis

    Parameters
    ----------
    data : ndarray
        Data set to be normalized
    inputs : dictionary
        Input file with corresponding model and data settings
    
    Returns
    -------
    ndarray
        Array with normalized data (array of Beta's in DSS terminology)
    """
