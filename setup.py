from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('LICENSE') as f:
    license = f.read()

setuptools.setup(
    name = "Hoodwink",
    version = "0.2",
    author = "Ethan M. Rasmussen",
    author_email = "ethan@razgroup.com",
    description = "A simple package for snatching basic stock data from Robinhood.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/ethanrasmussen/hoodwink",
    packages = setuptools.find_packages(),
)
