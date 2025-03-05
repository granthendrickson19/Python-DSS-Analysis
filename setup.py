from setuptools import setup, find_packages

setup(
    name='PythonDSSAnalysis',
    version='1.3',    
    description='A python package for DSS Analysis',
    url='https://github.com/granthendrickson19/Python-DSS-Analysis',
    author='Grant Hendrickson',
    author_email='granthendrickson19@gmail.com',
    license='MIT',
    install_requires=[
                      'numpy>=2.0',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.9',
    ],
)