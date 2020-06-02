import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gpx_csv_converter",
    version="0.2.2",
    author="Ethan Houston",
    author_email="ethan.houston@gmail.com",
    description="An easy way to convert between GPX and CSV files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ethanzh/gpx-csv-converter",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
