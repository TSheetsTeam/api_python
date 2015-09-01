from distutils.core import setup
from setuptools import find_packages


packages = [
    'tsheets',
    'tsheets.repos',
    'tsheets.models',
    ]

setup(
    name='tsheets',
    version='0.3',
    description='API library helper for TSheets.com',
    long_description='Allows to use the TSheets.com API to manage the timesheets and all other related data',
    author='Kannan Ponnusamy',
    author_email ='kannan@endpoint.com',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    url='https://github.com/tsheets/api_python',
    download_url='https://github.com/tsheets/api_python/tarball/0.3',
    keywords=['api', 'rest', 'tsheets'],
    install_requires=['requests>=2.7.0']
)
