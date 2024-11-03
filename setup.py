from setuptools import setup, find_packages

with open(README.md, 'r', 'utf-8') as rd:
    readme = rd.read()

setup(
    name='GFinance',
    version='0.1.0',
    author='Samuele Perfetti',
    author_email='samuele.perfetti01@gmail.com',
    description='Get quote from Google Finance',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/SamPerfe/GFinance',
    keywords= 'GoogleFinance',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6'
)