import numpy as np
import sys
import argparse
import yaml
from numpy import genfromtxt


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

def time_derivative(data, time):
    """Gets timed derivative using finite differences (can calculate omega or omega prime, first and second time derivative of beta respectively)

    Parameters
    ----------
    data : ndarray
        Data set to be normalized
    time : ndarray
        Time value of datasets
    
    Returns
    -------
    ndarray
        Array with normalized data (array of omegas's in DSS terminology)
    """
    return np.gradient(data,time)