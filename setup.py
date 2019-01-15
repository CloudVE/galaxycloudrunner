import ast
import os
import re

import setuptools

# Cannot use "from galaxycloudrunner import get_version" because that would
# try to import the six package which may not be installed yet.
reg = re.compile(r"__version__\s*=\s*(.+)")
with open(os.path.join("galaxycloudrunner", "__init__.py")) as f:
    for line in f:
        m = reg.match(line)
        if m:
            version = ast.literal_eval(m.group(1))
            break

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="galaxycloudrunner",
    description="A library for supporting cloud bursting in Galaxy.",
    version=version,
    author="Galaxy and GVL projects",
    author_email="help@genome.edu.au",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cloudve/galaxycloudrunner",
    packages=setuptools.find_packages(),
    install_requires=[
        "cachetools==3.0.0",
        "cloudlaunch-cli==0.2.1"
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6"
    ],
)
