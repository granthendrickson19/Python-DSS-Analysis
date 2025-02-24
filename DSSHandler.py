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
    else:
        raise ValueError(
            "Incorrect normilzation option selected"
        )
    

def time_derivative(data, time):
    """Gets timed derivative using finite differences (can calculate omega or omega prime, first and second time derivative of beta respectively)

    Parameters
    ----------
    data : ndarray
        Data set to be normalized
    time : ndarray
        Reference time value of datasets
    
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
        Reference time value of datasets
    
    Returns
    -------
    ndarray
        Array with non-normalized data generated from model
    """
     
    if inputs["model"] == "quad":
        data  = (float(inputs["A"])*time**2)+(float(inputs["B"])*time)+float(inputs["C"])
        return data

    elif inputs["model"] == "exp":
        data = (float(inputs["A"])*np.exp(float(inputs["B"])*time))+float(inputs["C"])
        return data
    else:
        raise ValueError(
            "Incorrect Model Selection"
        )
          
def process_time_generator(beta,omega):

    """Generates process time from an input of beta and omega values

    Parameters
    ----------
    beta : ndarray
        Array with normalized conserved quantity of interest (Betas)
    omega : ndarray
        Array with normalized agents of change (Omegas)
    
    Returns
    -------
    ndarray
        Array with process time values
    """
    return beta/omega

def temporal_displacement_generator(beta,omega,omegaprimes):
    """Generates the Temporal Displacement value.

    Parameters
    ----------
    beta : ndarray
        Array with normalized conserved quantity of interest (Betas)
    omega : ndarray
        Array with normalized agents of change (Omegas)
    omegaprimes : ndarray
        Array with time derivative of Omegas
    
    Returns
    -------
    ndarray
        Array with Temporal Displacement Values
    """
    return (-(beta*omegaprimes)/(omega**2))

def process_action_solver(time,temporalDisplacement):
    """Finds the process action (tau_s) using numerical integration

    Parameters
    ----------
    time : ndarray
        Array with reference time values
    temporalDisplacement : ndarray
        Array with Temporal Displacement Values (D)
    
    Returns
    -------
    process action: float
        Value of Process time
    """
    _sum =0.0
    for i in range(len(time)-1):
        _sum += ((1+temporalDisplacement[i])*(abs(time[i]-time[i+1])))
    return _sum

def normalized_coordinates(omega,referencetime,processtime,processaction):
    """Returns the normalized coordinates and parameters to assess scale distortion

    Parameters
    ----------
    omega : ndarray
        Array with omega values
    referencetime : ndarray
        Array with reference time values
    processtime : ndarray
        Array with process time values
    processaction : float
        Float value of process action
    
    Returns
    -------
    effectmetric : ndarray
        Array of effect metric values
    normalizedreferencetime :ndarray
        Array of normalized reference time values
    normalized reference time :ndarray
        Array of normalzied process time values
        
    """
    
    return (omega*processaction),(referencetime/processaction),(processtime/processaction)