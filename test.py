import numpy as np
import DSSHandler as DSS    

def test_data_normalzier_first():
    quad_dict = {
        "normalize": "first"
    }
    data = np.array([1,2,3,4,5])
    obs = DSS.data_normalizer(data, quad_dict)
    exp = np.array([1,2,3,4,5])
    assert exp.all() == obs.all()

def test_data_normalzier_last():
    quad_dict = {
        "normalize": "last"
    }
    data = np.array([1,2,3,4,5])
    obs = DSS.data_normalizer(data, quad_dict)
    exp = np.array([0.2,.4,.6,.8,1])
    assert np.allclose(exp,obs)

def test_time_derivative():
    #Trivial Solution no change with time
    data =np.array([1,1,1])
    time =np.array([1,2,3])
    exp = np.array([0,0,0])
    obs = DSS.time_derivative(data,time)
    assert np.allclose(exp,obs)

def test_time_derivative_linear():
    #Linear time change
    data = np.array([1,2,3])
    time = np.array([1,2,3])
    exp = np.array([1,1,1])
    obs = DSS.time_derivative(data,time)
    assert np.allclose(exp,obs)

def test_model_data_generator_quad():
    quad_dict = {
        "A" : "1",
        "B" : "1",
        "C" : "1",
        "model":"quad"
    }
    time = np.array([0,1,2])
    obs = DSS.model_data_generator(time,quad_dict)
    exp = np.array([1,3,7])
    assert np.allclose(exp,obs)

def test_model_data_generator_exp():
    quad_dict = {
        "A" : "1",
        "B" : "1",
        "C" : "1",
        "model":"exp"
    }
    time = np.array([-100,0,1])
    obs = DSS.model_data_generator(time,quad_dict)
    exp = np.array([1,2,3.71828])
    assert np.allclose(exp,obs)