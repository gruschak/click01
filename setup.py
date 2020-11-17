from setuptools import setup, find_packages
#     py_modules=['main'],

setup(
    name='my_test_package',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        weather=main:weather
        passw=main:pwd
    ''',
)
