from setuptools import setup, find_packages


setup(
    name='zocrypt',
    version='1.1.5',
    license='MIT',
    author="Siddhant Mohile",
    author_email='meetsiddhant@gmail.com',
    packages=find_packages('zocrypt'),
    package_dir={'': 'src'},
    url='https://github.com/SidmoGoesBrrr/zocrypt',
    keywords=['encrypt','decrypt','encoding','secret messages'],
    install_requires=[],

)
