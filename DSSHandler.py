import numpy as np
import sys
import argparse
import yaml

parser  = argparse.ArgumentParser(
    description="This command line program will take an input CSV file and apply DSS analysis "
    )
parser.add_argument('-d','--data',required=True, help='Data file to analyze')
parser.add_argument('-m','--model',required=True, help='Model YAML file for data predicition')
parser.add_argument('-o','--output',required=True, help='Output file name')



args = parser.parse_args(sys.argv[1:])