import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('LICENSE') as f:
    license = f.read()

setuptools.setup(
    name = "Hoodwink",
    version = "0.4.5",
    author = "Ethan Rasmussen",
    author_email = "eraz021102@gmail.com",
    description = "A simple package for snatching basic stock data from Robinhood.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/ethanrasmussen/hoodwink",
    python_requires='>=3.7',
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    install_requires=[
        "selenium",
        ],
)
