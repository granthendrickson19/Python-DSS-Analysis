Theory
======
This serves as a short refresher for Dynamical System Scaling (DSS) analysis. It is heavily recommended that the user reads the founding paper of DSS analysis before using this python package [1]_.

The DSS method is used to optimize process scaling, especially for transient processes. Where previous scaling methodologies attempt to match the parameter of interest, DSS attempts to match the parameter of interest and time rate of change of the parameter of interest.
By attempting to match transient processes, engineers are able to calculate distortion throughout the transient. This is incredibly powerful as previous scaling methodologies could only provide total distortion.

With DSS, engineers may be able to glean useful data from part of the transient (even if as a whole it is poorly scaled) that previously they would've discarded due to a poor total distortion. First the conserved quantity of interest is defined

.. math::
    \beta (t) = \frac{1}{\lambda_0} \int \int \int \lambda(x,t)dV
    \omega = \frac{d\beta}{dt}
    \omega' = \frac{d\omega}{dt}

We can now define a process time:

.. math::
    \tau = \frac{\beta}{\omega}

from [1]_ "...Process time [is defined] as the inverse of the fractional rate of change of a conserved quantity."
By taking the derivative of process time with respect to reference time allows us to define our *temporal displacement rate*

.. math::
    D=\frac{d\tau-dt}{dt}=-\frac{\beta}{\omega^2}\frac{d\omega}{dt}

.. math::
    d\tau = (1+D)dt

For a constant rate process, D=0, which implies that the process time and reference time interval are equivalant. If D is negative, the process time is contracted relative to reference time. If D is positive process time is dislated relative to reference time.
By normalzing our data to process time, we are able to describe processes (and compare different) on a normalized phase space where the difference between prototype and model points represents the distortion in the conserved quantity, and its rate of change.


.. [1] https://glc.ans.org/nureth-16/data/papers/13129.pdf