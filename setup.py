from setuptools import setup, find_packages

setup(
    name = 'tf_models_official_nlp_only', 
    version='2.3.0', 
    packages=find_packages(), 
    install_requires=["gin-config>=0.5.0;python_version>='<3.6>'"],
)

