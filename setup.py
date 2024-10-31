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
    package_dir={"": "."},  # Set root as the package directory
    packages=find_packages(where="."),  # Find all packages in root and subdirectories
    python_requires=">=3.6",
    install_requires=requirements,
)
