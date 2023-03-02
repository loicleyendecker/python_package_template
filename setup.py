from setuptools import setup, find_packages

setup(
    author="{{cookiecutter.contact}}"
    name="{{cookiecutter.package_name}}",
    version="0.1",
    packages=find_packages(),
    setup_requirements = [
    ]
)
