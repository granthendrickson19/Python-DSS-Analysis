import numpy as np
import sys
import argparse
import yaml
import DSSHandler
from numpy import genfromtxt

#Argparsing for running this through the commandline 
if __name__ == "__main__":
    parser  = argparse.ArgumentParser(
        description="This command line program will take an input CSV file and apply DSS analysis "
        )
    parser.add_argument('-d','--data',required=True, help='Data file to analyze')
    parser.add_argument('-m','--model',required=True, help='Model YAML file for data predicition')
    parser.add_argument('-o','--output',required=True, help='Output folder name')
    args = parser.parse_args(sys.argv[1:])
    my_data = genfromtxt(args.data, delimiter =',',skip_header=1)
    with open(args.model,'r') as f:
        inputs = yaml.safe_load(f)

_splitdata = np.array_split(my_data,2,1)
_time = np.concatenate(_splitdata[0])
_rawdata = np.concatenate(_splitdata[1])


#First I calculate all experimental data parameters
dataBetas = DSSHandler.data_normalizer(_rawdata,inputs)
dataOmegas = DSSHandler.time_derivative(dataBetas,_time)
dataOmegaPrimes = DSSHandler.time_derivative(dataOmegas,_time)
dataTaus = DSSHandler.process_time_generator(dataBetas,dataOmegas)
dataD = DSSHandler.temporal_displacement_generator(dataBetas,dataOmegas,dataOmegaPrimes)
dataProcessAction = DSSHandler.process_action_solver(_time,dataD)
effectMetricExperiment,normalizedReferenceTimeExperiment,normalziedProcesstimeExperiment = DSSHandler.normalized_coordinates(dataOmegas,_time,dataTaus,dataProcessAction)
dataEffectParameter = DSSHandler.effect_parameter_solver(effectMetricExperiment)

#Then my model DSS parameters
modelData = DSSHandler.model_data_generator(_time,inputs)
modelBetas = DSSHandler.data_normalizer(modelData,inputs)
modelOmegas = DSSHandler.time_derivative(modelBetas,_time)
modelOmegaPrimes = DSSHandler.time_derivative(modelOmegas,_time)
modelTaus = DSSHandler.process_time_generator(modelBetas,modelOmegas)
modelD = DSSHandler.temporal_displacement_generator(modelBetas,modelOmegas,modelOmegaPrimes)
modelProcessAction = DSSHandler.process_action_solver(_time,modelD)
effectMetricModel,normalizedReferenceTimeModel,normalizedProcesstimeModel = DSSHandler.normalized_coordinates(modelOmegas,_time,modelTaus,modelProcessAction)
modelEffectParameter = DSSHandler.effect_parameter_solver(effectMetricModel)

#This will calculate the distortion between my model and prototype 
localseparation,totalseparation = DSSHandler.geodesic_separation(dataBetas,dataD,effectMetricModel,effectMetricExperiment)
standardErrorEstimate = DSSHandler.standard_error(localseparation)

# Now I make my outlet folder which will concatenate my 
#########
#Data (beta omega D tau...) Model (...) Distortion Values
#########
#my header array with the order of
Header = np.array(["Beta","Omega","Omega Prime","Process time","Temporal Displacement","Effect Metric","Normalized Process Time","Normalized Reference Time","Process Action","Effect Parameter"])
Data = np.vstack((modelBetas,modelOmegas,modelOmegaPrimes,modelTaus,modelD,effectMetricModel,normalizedProcesstimeModel,normalizedReferenceTimeModel)).T
np.savetxt(args.output,Data,delimiter=',')
print(modelBetas)