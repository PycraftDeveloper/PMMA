from setuptools import setup, find_packages
from requests import get
from json import loads

# Get the latest tag from GitHub
tag_data = get("https://api.github.com/repos/PycraftDeveloper/PMMA/tags")
latest_tag = loads(tag_data.text)[0]["name"]

# Read the long description from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read the requirements from requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as req_file:
    requirements = req_file.read().splitlines()

package_data={
        "pmma": ["*"],  # Include all file types
        "": ["__init__.py", "c_setup.py"],  # Include these root files
    }

# Manually specify packages
packages = [
    "pmma.cython_src",
    "pmma.python_src",
    "pmma.shaders",
]

setup(
    name="pmma",
    version=latest_tag,
    author="PycraftDev",
    author_email="thomasjebbo@gmail.com",
    description="Python Multi-Media API (PMMA) is a multi-purpose API designed to make working on multi-media projects easier and faster!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PycraftDeveloper/PMMA",
    project_urls={
        "Bug Tracker": "https://github.com/PycraftDeveloper/PMMA/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=packages,  # Include the pmma package and all its sub-packages
    python_requires=">=3.6",
    install_requires=requirements,
    include_package_data=True,
    package_data=package_data,
)