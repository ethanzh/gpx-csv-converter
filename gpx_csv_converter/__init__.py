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
            raise TypeError("The file %s does not exist." % input_file_name)

        input_extension = os.path.splitext(input_file_name)[1]

        if input_extension != ".gpx":
            raise TypeError("Input file must be a GPX file")

        output_extension = os.path.splitext(output_file_name)[1]

        if output_extension != ".csv":
            raise TypeError("Output file must be a CSV file")

        with open(input_file_abs_path, "r") as gpx_in:
            gpx_string = gpx_in.read()
            self.convert(gpx_string, output_file_name)

    def convert(self, gpx_string, output_file_name):
        mydoc = minidom.parseString(gpx_string)

        trkpt = mydoc.getElementsByTagName("trkpt")
        row_list = []
        
        columns = ["timestamp", "latitude", "longitude", "elevation", "heart_rate"]

        # define type of heart rate field
        # garmin and other providers may have different elements for the hr field
        potential_fields_hr=["ns3:hr","gpxtpx:hr"]
        heart_rate_field=potential_fields_hr[0] # default
        for potential_field in potential_fields_hr:
            if len(mydoc.getElementsByTagName(potential_field))>0:
               heart_rate_field=potential_field

        # parse trackpoint elements. Search for child elements in each trackpoint so they stay in sync.
        for elem in trkpt:
            etimestamp=elem.getElementsByTagName("time")
            timestamp=None
            for selem in etimestamp:
                timestamp=(selem.firstChild.data)

            lat=(elem.attributes["lat"].value)
            lng=(elem.attributes["lon"].value)
            
            eelevation=elem.getElementsByTagName("ele")
            elevation=None
            for selem in eelevation:
                elevation=(selem.firstChild.data)
            
            eheart_rate=elem.getElementsByTagName(heart_rate_field)
            heart_rate=None
            for selem in eheart_rate:
                heart_rate=(selem.firstChild.data)
            
            this_row = [timestamp, lat, lng, elevation, heart_rate]
            row_list.append(this_row)

        with open(output_file_name, "wb") as output_file:
            writer = csv.writer(output_file)
            writer.writerow(columns)
            writer.writerows(row_list) 
