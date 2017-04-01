from setuptools import setup, find_packages


def readfile(filename):
    with open(filename, mode="rt") as f:
        return f.read()

setup(
    name='quotation',
    version='0.0.1',
    url="https://github.com/Cuizi7/quotation",
    packages=find_packages(),
    package_data={'': ['*.*']},
    author="Cuizi7",
    install_requires=readfile("requirements.txt"),
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    description="A simple package to get real-time chinese stock quotation"
)
