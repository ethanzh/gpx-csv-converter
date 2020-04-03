from xml.dom import minidom
import calendar
import dateutil.parser
import pandas as pd
import os

def iso_to_epoch(iso_time):
    return calendar.timegm(dateutil.parser.parse(iso_time).timetuple())


class Converter:

    def __init__(self, **kwargs):
        input_file_name = kwargs.get("input_file")
        output_file_name = kwargs.get("output_file")

        if not input_file_name or not output_file_name:
            raise TypeError("You must specify an input and output file")

        input_file_abs_path = os.path.abspath(input_file_name)
        input_file_exists = os.path.exists(input_file_abs_path)

        if not input_file_exists:
            raise TypeError(f"The file {input_file_name} does not exist.")

        input_extension = os.path.splitext(input_file_name)[1]

        if input_extension != ".gpx":
            raise TypeError(f"Input file must be a GPX file")

        output_extension = os.path.splitext(output_file_name)[1]

        if output_extension != ".csv":
            raise TypeError(f"Output file must be a CSV file")

        with open(input_file_abs_path, "r") as gpx_in:
            gpx_string = gpx_in.read()
            self.convert(gpx_string, output_file_name)


    def convert(self, gpx_string, output_file_name):
        mydoc = minidom.parseString(gpx_string)

        trkpt = mydoc.getElementsByTagName('trkpt')
        timestamp = mydoc.getElementsByTagName('time')
        elevation = mydoc.getElementsByTagName('ele')
        hr = mydoc.getElementsByTagName('gpxtpx:hr')

        lats = []
        lngs = []
        timestamps = []
        elevations = []
        hrs = []
        dates = []

        # parse coordinate pairs
        for elem in trkpt:
            lats.append(elem.attributes['lat'].value)
            lngs.append(elem.attributes['lon'].value)

        # parse timestamp (don't mess with timezone)
        for elem in timestamp:
            timestamps.append(elem.firstChild.data)

        # parse heartrate
        for elem in hr:
            hrs.append(elem.firstChild.data)

        # parse elevation
        for elem in elevation:
            elevations.append(elem.firstChild.data)

        # put all data into a dictionary so Pandas will accept it
        data = {
                'timestamp': pd.Series(timestamps),
                'latitude': pd.Series(lats),
                'longitude': pd.Series(lngs),
                'elevation': pd.Series(elevations),
                'heart_rate': pd.Series(hrs)}

        # create dataframe from dictionary
        df = pd.DataFrame(data=data)

        # specify columns
        df = df[['timestamp', 'latitude', 'longitude', 'elevation', 'heart_rate']]

        # write the pandas dataframe to a CSV file
        df.to_csv(output_file_name, encoding='utf-8', index=False)
