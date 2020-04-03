# GPX to CSV Converter
A handy tool for converting GPX files exported from Strava, WatShout, etc into easily readable CSV files

I made this tool to make it easier to perform calculations on large amounts of GPX data collected from a GPS.
Rather than manually copy and paste files into an Excel spreadsheet this module simple inputs the GPX file
(as a string, for now) and exports a nicely-formatted CSV file.

### Format

For now the module exports the following GPX tags to the CSV file:
* Timestamp
* Latitude
* Longitude
* Elevation
* Heart Rate

### Usage

1. Install module using pip
```python
pip install gpx-csv-converter
```
2. Import module within Python file
```python
from gpx_csv_converter import Converter
```
3. Converter takes two keyword arguments, 'input_file' and 'output_file'
```python
Converter(input_file="input.gpx", output_file="output.csv")
```
This will output a CSV file to the current directory

### Support

If you have any questions or concerns please shoot me an email at
[ethan.houston@gmail.com](ethan.houston@gmail.com)

https://pypi.org/project/gpx-csv-converter/
