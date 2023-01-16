# setup.py placed at root directory
from setuptools import setup, find_packages

setup(
    name='django-q',
    version='1.0',
    author='Rajeev-KL',
    author_email="rajeev@prodot.in",
    description='django-q',
    long_description='',
    url='test',
    python_requires='>=3.8',
    install_requires=[
        "arrow==1.2.2",
        "blessed==1.19.1",
        "django-picklefield==3.0.1"
    ],
    packages=find_packages(),
    include_package_data=True,
)