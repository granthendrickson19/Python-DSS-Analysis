Quickstart Guide
============
------------
Implementing to Existing Projects
-----------

For users uninterested in cloning the source directory, they may use the functions simply by using pip to install the package.

.. code-block::
    pip install PythonDSSAnalysis

With this users can import the package into their current working files with:

.. code-block::
    from PythonDSSAnalysis import DSSHandler as DSS

Users can now call all the functions available by invoking the DSS module

.. code-block::
    betas = DSS.data_normalizer(someData)


----------
Cloning the Repo
----------
First, it is recommended the users clone the repository into a fresh directory with a virtual environment

.. code-block::
    git clone https://github.com/granthendrickson19/Python-DSS-Analysis.git

Now the user should navigate into the Python-DSS-Analysis working directory (where the pyproject.toml file is located) to install the dependencies

.. code-block::
    pip install .

This should install numpy and pyyaml as the two dependencies the project requires.


------
Running Examples
------
Included with the repository, is sample data, a sampleRun.py file which can be called from the command line, and two sample model files. Both models fit the sample data, one with a quadratic fit, the other with an exponential.

Users can quickly run the two example problems by switching their directory to the working directory (where sampleRun.py is located). Running sampleRun.py from the command line takes 3 flags:
1. -m the model file, this is the .yml files which should be structured as the sample files provided
2. -d the data file, This is time demarked data of a single parameter of interest the first column must be time, the second column is the parameter of interest. Upon reading the file. the sampleRun skips the first line assuming titles of the data.
3. -o This is the output file name, it will be created in the same directory at which the sampleRun.py file is invoked.

.. code-block::
    python3 -m sampleRun.py -d sampledata.csv -m samplemodel.yml -o quadraticOutput

This will create a quadraticOutput.csv file with all the DSS parameters calculated