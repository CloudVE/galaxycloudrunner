import ast
import os
import re

import setuptools

reg = re.compile(r"__version__\s*=\s*(.+)")
with open(os.path.join("galaxycloudrunner", "__init__.py")) as f:
    for line in f:
        m = reg.match(line)
        if m:
            version = ast.literal_eval(m.group(1))
            break

with open("README.md", "r") as fh:
    long_description = fh.read()

REQS_FULL = [
    "cachetools==3.1.0",
    "cloudlaunch-cli==0.2.1"
]

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
    install_requires=REQS_FULL,
    extras_require={
        'dev': (['sphinx', 'sphinx_rtd_theme'] + REQS_FULL)
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
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
