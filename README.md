## This is also my project proposal initially will update with a more concrete utilization guide at a future date.

+ [![cov](https://granthendrickson19.github.io/Python-DSS-Analysis/badges/coverage.svg)](https://github.com/granthendrickson19/Python-DSS-Analysis/actions)

My python package will perform Dynamical System Scaling (DSS) analysis for inputted datasets and models. DSS is a novel scaling technique that attempts to consider the transient response of a system with its scaling criteria. This allows for distortion between the model and prototype to vary as a function of time. Compared to previous scaling methods (Hierarchical Two-Tiered Scaling, Fractional Scaling Analysis...) distortion being calculated over time rather than a single value is a powerful metric. Say a model predicts a prototype well for the first half of the transient before diverging. DSS would allow engineers to glean useful data in the first part of the transient while discarding the rest. Some of the key DSS values that will be calculated include, the nondimensional conserved values and agents of change, distortion, temporal displacement, and scaling values.

I envision that my python package will import a csv (or similar file structure) data file with time and quantity and interest. Additionally, I would like the package to be able to import a desired model (quadratic, exponential, logarithmic). My package will then calculate all of the desired DSS values and generate associated graphs as well as an output csv file with all the data. As I will be working with matrices and graphing I predict that my package will use Numpy, Matplotlib, and Scipy.


