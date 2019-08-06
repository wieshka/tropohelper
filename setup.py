from setuptools import setup

setup(
    name='tropohelper',
    version='0.0.1',
    description='Little helper to ease work building troposphere templates for sceptre',
    url='https://github.com/wieshka/troposphere-helper-template',
    author='Viesturs Proskins',
    author_email='viesturs.proskins@gmail.com',
    license='New BSD license',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='troposphere cloudformation aws sceptre',
    packages=['tropohelper'],
    install_requires=['troposphere'],
)