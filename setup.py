#for installing local package in virtual environment
from setuptools import find_packages, setup

setup (
    name='mcqgenerator',
    version='0.0.1',
    author='Chahak Jain',
    author_email='chahakjain.0510@gmail.com',
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)