"""Python package configuration."""

from setuptools import setup

setup(
    name='turtle',
    version='0.1.0',
    packages=['turtle'],
    include_package_data=True,
    install_requires=[
        'websocket-client==0.47.0',
        'pycodestyle==2.3.1',
        'pydocstyle==2.0.0',
        'pylint==1.8.1',
    ],
)
