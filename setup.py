"""
    Project: shhistory (https://github.com/azazelm3dj3d/shhistory)
    Author: azazelm3dj3d (https://github.com/azazelm3dj3d)
    License: BSD 2-Clause
"""

import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "shhistory",
    version = "0.1.8",
    author = "azazelm3dj3d",
    description = "Simple Python library to return your shell history or dump to a nicely formatted JSON file.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/azazelm3dj3d/shhistory",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    py_modules=["shhistory"],
    python_requires = ">=3.6"
)