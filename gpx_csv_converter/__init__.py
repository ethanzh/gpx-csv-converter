from xml.dom import minidom
import csv
import os


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

        trkpt = mydoc.getElementsByTagName("trkpt")
        timestamp = mydoc.getElementsByTagName("time")
        elevation = mydoc.getElementsByTagName("ele")
        hr = mydoc.getElementsByTagName("gpxtpx:hr")

        lats = []
        lngs = []
        timestamps = []
        elevations = []
        hrs = []
        dates = []

        # parse coordinate pairs
        for elem in trkpt:
            lats.append(elem.attributes["lat"].value)
            lngs.append(elem.attributes["lon"].value)

        # parse timestamp (don't mess with timezone)
        for elem in timestamp:
            timestamps.append(elem.firstChild.data)
        # remove the first <time>, which is a meta tag
        timestamps = timestamps[1:]

        # parse heartrate
        for elem in hr:
            hrs.append(elem.firstChild.data)

        # parse elevation
        for elem in elevation:
            elevations.append(elem.firstChild.data)

        row_list = []

        assert len(lats) == len(lngs), "length of latitudes and longitudes differ"
        assert len(lngs) == len(
            timestamps
        ), "length of longitudes and timestamps differ"
        assert (
            len(timestamps) == len(hrs) or len(hrs) == 0
        ), "length of timestamps and heart rates differ"
        assert (
            len(hrs) == len(elevations) or len(elevations) == 0
        ), "length of heart rates and elevations diff"

        # we are sure these are all equal
        num_rows = len(lats)

        for i in range(num_rows):
            timestamp = timestamps[i]
            lat = lats[i]
            lng = lngs[i]
            elevation = elevations[i] if len(elevations) != 0 else None
            heart_rate = hrs[i] if len(hrs) != 0 else None
            this_row = [timestamp, lat, lng, elevation, heart_rate]
            row_list.append(this_row)

        columns = ["timestamp", "latitude", "longitude", "elevation", "heart_rate"]

        with open(output_file_name, "w", newline="") as output_file:
            writer = csv.writer(output_file)
            writer.writerow(columns)
            writer.writerows(row_list)
