# gpx-to-csv-converter
A handy tool for converting GPX files exported from Strava, WatShout, etc into easily readable CSV files

Official readme coming soon! I am in the process of packaging this into a real module

### Usage:


1. Install module using pip
```python
pip install gpx-csv-converter
```
2. Import module within Python file
```python
from gpx_csv_converter import Converter
```
3. Currently the module takes two inputs: the GPX string itself and the
desired file name (file parsing coming soon)
```python
Converter(my_gpx_string, 'my_csv_file.csv')
```
This will output a CSV file to the current directory

### Support

If you have any questions or concerns please shoot me an email at
[ethan.houston@gmail.com](ethan.houston@gmail.com)