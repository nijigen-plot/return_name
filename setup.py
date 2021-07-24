import setuptools

setuptools.setup(
    name='returnname',
    version='1.0',
    description='test for pip install git+',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts':[
            'return = returnname.return:call'
        ]
    }
)