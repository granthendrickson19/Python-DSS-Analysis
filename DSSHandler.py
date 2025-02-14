import numpy as np
import math



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
    elif inputs["normalize"] == "last":
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

def model_data_generator(time,inputs):
    """Generates the model dataset for comparison to experimental data

    Parameters
    ----------
    data : inputs
        Input file with model values specified 
    time : ndarray
        Time value of datasets
    
    Returns
    -------
    ndarray
        Array with non-normalized data generated from model
    """
     
    if inputs["model"] == "quad":
        data  = (float(inputs["A"])*time**2)+(float(inputs["B"])*time)+float(inputs["C"])
        return data

    elif inputs["model"] == "exp":
        data = (float(inputs["A"])*math.exp(float(inputs["B"])*time))+float(inputs["C"])
        print("hello")
        return data
    else:
        raise ValueError(
            "Incorrect Model Selection"
        )
          