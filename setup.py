from distutils.core import setup
setup(
    name='tsheets',
    packages=['tsheets'],
    version='0.1',
    description='API library helper for TSheets.com',
    long_description='Allows to use the TSheets.com API to manage the timesheets and all other related data',
    author='Kannan Ponnusamy',
    author_email ='kannan@endpoint.com',
    license='MIT',
    url='https://github.com/tsheets/api_python',
    download_url='https://github.com/tsheets/api_python/tarball/0.1',
    keywords=['api', 'rest', 'tsheets'],
    install_requires=['requests>=2.7.0']
)
