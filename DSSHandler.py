import numpy as np
import sys
import argparse
import yaml
from numpy import genfromtxt

#First Function
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
    if inputs["normalize"] == "first":
        return (data / data[0])
    if inputs["normalize"] == "last":
        return (data / data[-1])