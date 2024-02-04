import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "pmma",
    version = "0.0.1",
    author = "PycraftDev",
    author_email = "thomasjebbo@gmail.com",
    description = "Python Multi-Media API (PMMA) is a multi-purpose API designed to make working on multi-media projects easier and faster!",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/PycraftDeveloper/PMMA",
    project_urls = {
        "Bug Tracker": "https://github.com/PycraftDeveloper/PMMA/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)