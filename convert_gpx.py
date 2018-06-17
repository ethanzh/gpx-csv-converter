from xml.dom import minidom
import calendar
import dateutil.parser
import pandas as pd


def iso_to_epoch(iso_time):
    return calendar.timegm(dateutil.parser.parse(iso_time).timetuple())


class Converter:

    def __init__(self, string, name):

        # parse an xml file by name
        mydoc = minidom.parseString("""<?xml version="1.0" encoding="UTF-8"?><gpx xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd">
    <metadata>
        <time>2018-06-16T17:45:13Z</time>
    </metadata>
    <trk>
        <name>Test name</name>
        <type>1</type>
        <trkseg id="trkseg">
            <trkpt lat="37.4270128" lon="-122.1096353">
                <ele>0.0</ele>
                <time>2018-06-16T17:45:19Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4270239" lon="-122.1095977">
                <ele>0.0</ele>
                <time>2018-06-16T17:45:24Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.427033" lon="-122.1095565">
                <ele>0.0</ele>
                <time>2018-06-16T17:45:29Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4270363" lon="-122.1095386">
                <ele>0.0</ele>
                <time>2018-06-16T17:45:34Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4269868" lon="-122.1096091">
                <ele>0.0</ele>
                <time>2018-06-16T17:45:51Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4269452" lon="-122.1096271">
                <ele>0.0</ele>
                <time>2018-06-16T17:45:56Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4269271" lon="-122.10964">
                <ele>0.0</ele>
                <time>2018-06-16T17:46:01Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4268721" lon="-122.109696">
                <ele>0.0</ele>
                <time>2018-06-16T17:46:06Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4265343" lon="-122.1101322">
                <ele>0.0</ele>
                <time>2018-06-16T17:46:11Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4262623" lon="-122.1109352">
                <ele>0.0</ele>
                <time>2018-06-16T17:46:16Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4261181" lon="-122.1109982">
                <ele>0.0</ele>
                <time>2018-06-16T17:46:22Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4258509" lon="-122.1110847">
                <ele>0.0</ele>
                <time>2018-06-16T17:46:27Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4257518" lon="-122.1108771">
                <ele>-29.899999618530273</ele>
                <time>2018-06-16T17:46:32Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4257407" lon="-122.1108705">
                <ele>0.0</ele>
                <time>2018-06-16T17:46:37Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4257147" lon="-122.1108456">
                <ele>0.0</ele>
                <time>2018-06-16T17:46:42Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4255471" lon="-122.1106861">
                <ele>0.0</ele>
                <time>2018-06-16T17:46:48Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4250423" lon="-122.1104653">
                <ele>0.0</ele>
                <time>2018-06-16T17:46:53Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4245786" lon="-122.1104487">
                <ele>0.0</ele>
                <time>2018-06-16T17:46:58Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4246028" lon="-122.1104472">
                <ele>0.0</ele>
                <time>2018-06-16T17:47:03Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4244657" lon="-122.11054">
                <ele>0.0</ele>
                <time>2018-06-16T17:47:08Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4240676" lon="-122.1108393">
                <ele>0.0</ele>
                <time>2018-06-16T17:47:13Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4237921" lon="-122.1111034">
                <ele>0.0</ele>
                <time>2018-06-16T17:47:19Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4235161" lon="-122.1113633">
                <ele>-27.5</ele>
                <time>2018-06-16T17:47:24Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4233448" lon="-122.1115666">
                <ele>0.0</ele>
                <time>2018-06-16T17:47:29Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.423255" lon="-122.1116618">
                <ele>0.0</ele>
                <time>2018-06-16T17:47:34Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4229273" lon="-122.1118547">
                <ele>0.0</ele>
                <time>2018-06-16T17:47:40Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4228266" lon="-122.1119284">
                <ele>0.0</ele>
                <time>2018-06-16T17:47:45Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4227723" lon="-122.1120349">
                <ele>0.0</ele>
                <time>2018-06-16T17:47:50Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4226954" lon="-122.1120577">
                <ele>0.0</ele>
                <time>2018-06-16T17:48:05Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4225816" lon="-122.1120236">
                <ele>0.0</ele>
                <time>2018-06-16T17:48:10Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4224777" lon="-122.1120433">
                <ele>0.0</ele>
                <time>2018-06-16T17:48:15Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4222414" lon="-122.111894">
                <ele>0.0</ele>
                <time>2018-06-16T17:48:21Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4221372" lon="-122.1117529">
                <ele>0.0</ele>
                <time>2018-06-16T17:48:26Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4221119" lon="-122.1117228">
                <ele>0.0</ele>
                <time>2018-06-16T17:48:31Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4221087" lon="-122.111624">
                <ele>0.0</ele>
                <time>2018-06-16T17:48:37Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4220736" lon="-122.1116894">
                <ele>0.0</ele>
                <time>2018-06-16T17:48:43Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4215717" lon="-122.1112918">
                <ele>-23.600000381469727</ele>
                <time>2018-06-16T17:48:48Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4205796" lon="-122.1104581">
                <ele>-23.600000381469727</ele>
                <time>2018-06-16T17:48:53Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.42027" lon="-122.1101941">
                <ele>0.0</ele>
                <time>2018-06-16T17:48:59Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4200968" lon="-122.1101787">
                <ele>0.0</ele>
                <time>2018-06-16T17:49:04Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.419924" lon="-122.110228">
                <ele>0.0</ele>
                <time>2018-06-16T17:49:09Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4197669" lon="-122.1102929">
                <ele>0.0</ele>
                <time>2018-06-16T17:49:14Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4194251" lon="-122.110712">
                <ele>-27.600000381469727</ele>
                <time>2018-06-16T17:49:19Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4192047" lon="-122.1110351">
                <ele>-27.600000381469727</ele>
                <time>2018-06-16T17:49:24Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4190252" lon="-122.111323">
                <ele>0.0</ele>
                <time>2018-06-16T17:49:29Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4188994" lon="-122.1115517">
                <ele>0.0</ele>
                <time>2018-06-16T17:49:35Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4188474" lon="-122.1115645">
                <ele>0.0</ele>
                <time>2018-06-16T17:49:41Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4186219" lon="-122.1124357">
                <ele>0.0</ele>
                <time>2018-06-16T17:49:46Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.418533" lon="-122.1129881">
                <ele>0.0</ele>
                <time>2018-06-16T17:49:52Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4183898" lon="-122.1133499">
                <ele>0.0</ele>
                <time>2018-06-16T17:49:57Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4181891" lon="-122.113762">
                <ele>0.0</ele>
                <time>2018-06-16T17:50:02Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4179196" lon="-122.1142912">
                <ele>0.0</ele>
                <time>2018-06-16T17:50:08Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4175908" lon="-122.1147731">
                <ele>-24.299999237060547</ele>
                <time>2018-06-16T17:50:13Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4175106" lon="-122.1148688">
                <ele>-24.299999237060547</ele>
                <time>2018-06-16T17:50:18Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4173724" lon="-122.1151595">
                <ele>-24.299999237060547</ele>
                <time>2018-06-16T17:50:23Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4170082" lon="-122.1159006">
                <ele>0.0</ele>
                <time>2018-06-16T17:50:29Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4168561" lon="-122.1161836">
                <ele>0.0</ele>
                <time>2018-06-16T17:50:34Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4166922" lon="-122.1164112">
                <ele>0.0</ele>
                <time>2018-06-16T17:50:40Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.416545" lon="-122.1165318">
                <ele>0.0</ele>
                <time>2018-06-16T17:50:46Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4163771" lon="-122.1167344">
                <ele>0.0</ele>
                <time>2018-06-16T17:50:51Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4158393" lon="-122.1174706">
                <ele>0.0</ele>
                <time>2018-06-16T17:50:56Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4153636" lon="-122.1179277">
                <ele>0.0</ele>
                <time>2018-06-16T17:51:02Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4153072" lon="-122.1179827">
                <ele>0.0</ele>
                <time>2018-06-16T17:51:07Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4152143" lon="-122.1182095">
                <ele>0.0</ele>
                <time>2018-06-16T17:51:12Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4151853" lon="-122.1182693">
                <ele>0.0</ele>
                <time>2018-06-16T17:51:17Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4149055" lon="-122.1185595">
                <ele>0.0</ele>
                <time>2018-06-16T17:51:23Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4148863" lon="-122.1186137">
                <ele>0.0</ele>
                <time>2018-06-16T17:51:28Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4142711" lon="-122.1190155">
                <ele>0.0</ele>
                <time>2018-06-16T17:51:33Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4137947" lon="-122.1195771">
                <ele>0.0</ele>
                <time>2018-06-16T17:51:38Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4135113" lon="-122.1198472">
                <ele>0.0</ele>
                <time>2018-06-16T17:51:43Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4131416" lon="-122.1201624">
                <ele>0.0</ele>
                <time>2018-06-16T17:51:49Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4130132" lon="-122.1202113">
                <ele>0.0</ele>
                <time>2018-06-16T17:51:54Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4129147" lon="-122.1202532">
                <ele>0.0</ele>
                <time>2018-06-16T17:51:59Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4128528" lon="-122.1203348">
                <ele>0.0</ele>
                <time>2018-06-16T17:52:04Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4124069" lon="-122.121076">
                <ele>0.0</ele>
                <time>2018-06-16T17:52:10Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4121792" lon="-122.1212723">
                <ele>0.0</ele>
                <time>2018-06-16T17:52:15Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4120156" lon="-122.1214877">
                <ele>0.0</ele>
                <time>2018-06-16T17:52:21Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4115996" lon="-122.1220124">
                <ele>-15.5</ele>
                <time>2018-06-16T17:52:26Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4114391" lon="-122.1222286">
                <ele>-15.5</ele>
                <time>2018-06-16T17:52:31Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4111743" lon="-122.1225604">
                <ele>-15.5</ele>
                <time>2018-06-16T17:52:36Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4111074" lon="-122.1226462">
                <ele>-15.5</ele>
                <time>2018-06-16T17:52:42Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4109557" lon="-122.122966">
                <ele>0.0</ele>
                <time>2018-06-16T17:52:47Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4101653" lon="-122.1236121">
                <ele>-15.399999618530273</ele>
                <time>2018-06-16T17:52:53Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4096349" lon="-122.1238624">
                <ele>-14.399999618530273</ele>
                <time>2018-06-16T17:52:58Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4093922" lon="-122.1239262">
                <ele>-12.399999618530273</ele>
                <time>2018-06-16T17:53:03Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4089063" lon="-122.1241964">
                <ele>-8.699999809265137</ele>
                <time>2018-06-16T17:53:08Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4088066" lon="-122.1243802">
                <ele>-14.399999618530273</ele>
                <time>2018-06-16T17:53:14Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4085476" lon="-122.1247585">
                <ele>-10.300000190734863</ele>
                <time>2018-06-16T17:53:19Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4083773" lon="-122.1249759">
                <ele>-10.300000190734863</ele>
                <time>2018-06-16T17:53:25Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4081918" lon="-122.1251424">
                <ele>-10.300000190734863</ele>
                <time>2018-06-16T17:53:30Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4081098" lon="-122.1251411">
                <ele>0.0</ele>
                <time>2018-06-16T17:53:35Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4079876" lon="-122.1252134">
                <ele>0.0</ele>
                <time>2018-06-16T17:53:40Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4079618" lon="-122.1252667">
                <ele>0.0</ele>
                <time>2018-06-16T17:53:46Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4079416" lon="-122.1252756">
                <ele>0.0</ele>
                <time>2018-06-16T17:53:51Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.408087" lon="-122.1253333">
                <ele>0.0</ele>
                <time>2018-06-16T17:53:56Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4072393" lon="-122.1257662">
                <ele>-10.300000190734863</ele>
                <time>2018-06-16T17:54:02Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4060599" lon="-122.1263669">
                <ele>0.0</ele>
                <time>2018-06-16T17:54:07Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4060014" lon="-122.1264066">
                <ele>0.0</ele>
                <time>2018-06-16T17:54:12Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4057577" lon="-122.1265817">
                <ele>0.0</ele>
                <time>2018-06-16T17:54:17Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4054466" lon="-122.1268037">
                <ele>0.0</ele>
                <time>2018-06-16T17:54:22Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4050862" lon="-122.1270034">
                <ele>0.0</ele>
                <time>2018-06-16T17:54:27Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4046783" lon="-122.1272028">
                <ele>0.0</ele>
                <time>2018-06-16T17:54:32Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4042501" lon="-122.1275259">
                <ele>0.0</ele>
                <time>2018-06-16T17:54:38Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4039686" lon="-122.127758">
                <ele>0.0</ele>
                <time>2018-06-16T17:54:43Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4037613" lon="-122.1278751">
                <ele>0.0</ele>
                <time>2018-06-16T17:54:49Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4034351" lon="-122.1281405">
                <ele>0.0</ele>
                <time>2018-06-16T17:54:54Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4029674" lon="-122.1284093">
                <ele>0.0</ele>
                <time>2018-06-16T17:54:59Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4025958" lon="-122.1286198">
                <ele>0.0</ele>
                <time>2018-06-16T17:55:04Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4025253" lon="-122.1287164">
                <ele>0.0</ele>
                <time>2018-06-16T17:55:09Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4023313" lon="-122.1287592">
                <ele>0.0</ele>
                <time>2018-06-16T17:55:15Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.402353" lon="-122.1287111">
                <ele>0.0</ele>
                <time>2018-06-16T17:55:20Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4023388" lon="-122.1287094">
                <ele>0.0</ele>
                <time>2018-06-16T17:55:25Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.402108" lon="-122.1289815">
                <ele>0.0</ele>
                <time>2018-06-16T17:55:30Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4015826" lon="-122.1294799">
                <ele>-2.299999952316284</ele>
                <time>2018-06-16T17:55:35Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.401202" lon="-122.1297034">
                <ele>0.0</ele>
                <time>2018-06-16T17:55:40Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4008475" lon="-122.1302748">
                <ele>0.0</ele>
                <time>2018-06-16T17:55:46Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4007663" lon="-122.1306044">
                <ele>0.0</ele>
                <time>2018-06-16T17:55:51Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4006136" lon="-122.1309024">
                <ele>0.0</ele>
                <time>2018-06-16T17:55:56Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4005245" lon="-122.1310636">
                <ele>0.0</ele>
                <time>2018-06-16T17:56:02Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4004861" lon="-122.1311548">
                <ele>0.0</ele>
                <time>2018-06-16T17:56:06Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4004502" lon="-122.131233">
                <ele>0.0</ele>
                <time>2018-06-16T17:56:12Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4002704" lon="-122.1316181">
                <ele>0.0</ele>
                <time>2018-06-16T17:56:17Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.400264" lon="-122.1317269">
                <ele>0.0</ele>
                <time>2018-06-16T17:56:22Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.4002036" lon="-122.1320017">
                <ele>0.0</ele>
                <time>2018-06-16T17:56:27Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3999379" lon="-122.1326393">
                <ele>0.0</ele>
                <time>2018-06-16T17:56:32Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3997218" lon="-122.1329741">
                <ele>0.0</ele>
                <time>2018-06-16T17:56:37Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3994436" lon="-122.1335008">
                <ele>0.0</ele>
                <time>2018-06-16T17:56:42Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3993976" lon="-122.1336269">
                <ele>0.0</ele>
                <time>2018-06-16T17:56:48Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3993125" lon="-122.1337373">
                <ele>0.0</ele>
                <time>2018-06-16T17:56:54Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3992285" lon="-122.1338569">
                <ele>0.0</ele>
                <time>2018-06-16T17:57:00Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3991853" lon="-122.133885">
                <ele>0.0</ele>
                <time>2018-06-16T17:57:05Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.399174" lon="-122.1339419">
                <ele>0.0</ele>
                <time>2018-06-16T17:57:10Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3991716" lon="-122.1338274">
                <ele>0.0</ele>
                <time>2018-06-16T17:57:15Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3991758" lon="-122.1339046">
                <ele>0.0</ele>
                <time>2018-06-16T17:57:20Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3991061" lon="-122.1339455">
                <ele>0.0</ele>
                <time>2018-06-16T17:57:25Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3990251" lon="-122.134016">
                <ele>0.0</ele>
                <time>2018-06-16T17:57:30Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.398998" lon="-122.1341053">
                <ele>0.0</ele>
                <time>2018-06-16T17:57:36Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.398846" lon="-122.1341622">
                <ele>0.0</ele>
                <time>2018-06-16T17:57:41Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3985898" lon="-122.1344401">
                <ele>0.0</ele>
                <time>2018-06-16T17:57:46Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3985672" lon="-122.134466">
                <ele>0.0</ele>
                <time>2018-06-16T17:57:51Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3985483" lon="-122.1344698">
                <ele>0.0</ele>
                <time>2018-06-16T17:57:56Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3984717" lon="-122.1346667">
                <ele>0.0</ele>
                <time>2018-06-16T17:58:01Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3976399" lon="-122.1363745">
                <ele>0.0</ele>
                <time>2018-06-16T17:58:07Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.397452" lon="-122.1366411">
                <ele>0.0</ele>
                <time>2018-06-16T17:58:13Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3974573" lon="-122.1367159">
                <ele>0.0</ele>
                <time>2018-06-16T17:58:19Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3972956" lon="-122.1372573">
                <ele>0.0</ele>
                <time>2018-06-16T17:58:25Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3971868" lon="-122.1375122">
                <ele>0.0</ele>
                <time>2018-06-16T17:58:30Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3969337" lon="-122.1380314">
                <ele>0.0</ele>
                <time>2018-06-16T17:58:35Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3966811" lon="-122.1383515">
                <ele>0.0</ele>
                <time>2018-06-16T17:58:41Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.396023" lon="-122.1394358">
                <ele>0.0</ele>
                <time>2018-06-16T17:58:47Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3958858" lon="-122.1394742">
                <ele>0.0</ele>
                <time>2018-06-16T17:58:53Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3958578" lon="-122.1394821">
                <ele>0.0</ele>
                <time>2018-06-16T17:58:58Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3957106" lon="-122.1397596">
                <ele>0.0</ele>
                <time>2018-06-16T17:59:04Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3955515" lon="-122.1400549">
                <ele>0.0</ele>
                <time>2018-06-16T17:59:10Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3953722" lon="-122.14034">
                <ele>0.0</ele>
                <time>2018-06-16T17:59:16Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3952761" lon="-122.1404928">
                <ele>0.0</ele>
                <time>2018-06-16T17:59:21Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3952402" lon="-122.14055">
                <ele>0.0</ele>
                <time>2018-06-16T17:59:27Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3947145" lon="-122.1419276">
                <ele>0.0</ele>
                <time>2018-06-16T17:59:33Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3944524" lon="-122.1428559">
                <ele>0.0</ele>
                <time>2018-06-16T17:59:39Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3943292" lon="-122.1435391">
                <ele>0.0</ele>
                <time>2018-06-16T17:59:45Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3941922" lon="-122.143743">
                <ele>0.0</ele>
                <time>2018-06-16T17:59:51Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3942007" lon="-122.1438208">
                <ele>0.0</ele>
                <time>2018-06-16T17:59:56Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3942208" lon="-122.1438873">
                <ele>0.0</ele>
                <time>2018-06-16T18:00:02Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3942217" lon="-122.1439861">
                <ele>0.0</ele>
                <time>2018-06-16T18:00:08Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3942069" lon="-122.1443614">
                <ele>0.0</ele>
                <time>2018-06-16T18:00:15Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.394102" lon="-122.1448294">
                <ele>0.0</ele>
                <time>2018-06-16T18:00:20Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.393323" lon="-122.1458303">
                <ele>0.0</ele>
                <time>2018-06-16T18:00:25Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3930509" lon="-122.1460373">
                <ele>0.0</ele>
                <time>2018-06-16T18:00:30Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3929489" lon="-122.1461497">
                <ele>0.0</ele>
                <time>2018-06-16T18:00:36Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3929094" lon="-122.1462939">
                <ele>0.0</ele>
                <time>2018-06-16T18:00:43Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3928551" lon="-122.1466831">
                <ele>0.0</ele>
                <time>2018-06-16T18:00:48Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3928227" lon="-122.1473597">
                <ele>0.0</ele>
                <time>2018-06-16T18:00:53Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3928279" lon="-122.1475255">
                <ele>0.0</ele>
                <time>2018-06-16T18:00:58Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3928448" lon="-122.1476224">
                <ele>0.0</ele>
                <time>2018-06-16T18:01:04Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3928016" lon="-122.1476602">
                <ele>0.0</ele>
                <time>2018-06-16T18:01:09Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.392796" lon="-122.1476795">
                <ele>0.0</ele>
                <time>2018-06-16T18:01:15Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3926056" lon="-122.1478683">
                <ele>0.0</ele>
                <time>2018-06-16T18:01:21Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3923231" lon="-122.1484714">
                <ele>0.0</ele>
                <time>2018-06-16T18:01:26Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3921117" lon="-122.1489822">
                <ele>0.0</ele>
                <time>2018-06-16T18:01:31Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3920712" lon="-122.1490775">
                <ele>0.0</ele>
                <time>2018-06-16T18:01:36Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3919447" lon="-122.1491046">
                <ele>0.0</ele>
                <time>2018-06-16T18:01:41Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3918876" lon="-122.1491909">
                <ele>0.0</ele>
                <time>2018-06-16T18:01:48Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3917803" lon="-122.1494392">
                <ele>0.0</ele>
                <time>2018-06-16T18:01:54Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3916781" lon="-122.1496761">
                <ele>0.0</ele>
                <time>2018-06-16T18:01:59Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3913246" lon="-122.1500549">
                <ele>0.0</ele>
                <time>2018-06-16T18:02:04Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3909337" lon="-122.1496953">
                <ele>0.0</ele>
                <time>2018-06-16T18:02:09Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3907184" lon="-122.1499671">
                <ele>0.0</ele>
                <time>2018-06-16T18:02:14Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.390605" lon="-122.1501103">
                <ele>0.0</ele>
                <time>2018-06-16T18:02:19Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3904793" lon="-122.1500433">
                <ele>0.0</ele>
                <time>2018-06-16T18:02:25Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3900187" lon="-122.150551">
                <ele>0.0</ele>
                <time>2018-06-16T18:02:31Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3898352" lon="-122.1507533">
                <ele>0.0</ele>
                <time>2018-06-16T18:02:37Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3897479" lon="-122.1508495">
                <ele>0.0</ele>
                <time>2018-06-16T18:02:43Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3895887" lon="-122.150976">
                <ele>0.0</ele>
                <time>2018-06-16T18:02:48Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3887404" lon="-122.1510923">
                <ele>0.0</ele>
                <time>2018-06-16T18:02:54Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3882032" lon="-122.1510975">
                <ele>0.0</ele>
                <time>2018-06-16T18:03:01Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3880962" lon="-122.1511003">
                <ele>0.0</ele>
                <time>2018-06-16T18:03:06Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3880621" lon="-122.1511011">
                <ele>0.0</ele>
                <time>2018-06-16T18:03:12Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3878742" lon="-122.1511904">
                <ele>0.0</ele>
                <time>2018-06-16T18:03:17Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3872673" lon="-122.1510909">
                <ele>0.0</ele>
                <time>2018-06-16T18:03:23Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3870568" lon="-122.1510565">
                <ele>0.0</ele>
                <time>2018-06-16T18:03:29Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3868673" lon="-122.1513791">
                <ele>0.0</ele>
                <time>2018-06-16T18:03:35Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3869934" lon="-122.1513302">
                <ele>0.0</ele>
                <time>2018-06-16T18:03:41Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3870591" lon="-122.1510321">
                <ele>0.0</ele>
                <time>2018-06-16T18:03:47Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.387113" lon="-122.150788">
                <ele>0.0</ele>
                <time>2018-06-16T18:03:52Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3871582" lon="-122.1505829">
                <ele>0.0</ele>
                <time>2018-06-16T18:03:58Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.387189" lon="-122.1504434">
                <ele>0.0</ele>
                <time>2018-06-16T18:04:04Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3872034" lon="-122.1503782">
                <ele>0.0</ele>
                <time>2018-06-16T18:04:09Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3872119" lon="-122.1503397">
                <ele>0.0</ele>
                <time>2018-06-16T18:04:15Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3872175" lon="-122.1503145">
                <ele>0.0</ele>
                <time>2018-06-16T18:04:20Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3872213" lon="-122.1502969">
                <ele>0.0</ele>
                <time>2018-06-16T18:04:26Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3853607" lon="-122.1572375">
                <ele>0.0</ele>
                <time>2018-06-16T18:04:33Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3853027" lon="-122.1574539">
                <ele>0.0</ele>
                <time>2018-06-16T18:04:38Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3852907" lon="-122.1574987">
                <ele>0.0</ele>
                <time>2018-06-16T18:04:44Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3852819" lon="-122.157526">
                <ele>0.0</ele>
                <time>2018-06-16T18:04:50Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3861803" lon="-122.1546708">
                <ele>0.0</ele>
                <time>2018-06-16T18:04:55Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3868724" lon="-122.1536554">
                <ele>0.0</ele>
                <time>2018-06-16T18:05:01Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3872704" lon="-122.1530714">
                <ele>0.0</ele>
                <time>2018-06-16T18:05:07Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3875715" lon="-122.1534766">
                <ele>0.0</ele>
                <time>2018-06-16T18:05:13Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3877667" lon="-122.1537393">
                <ele>0.0</ele>
                <time>2018-06-16T18:05:19Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3875534" lon="-122.1542407">
                <ele>0.0</ele>
                <time>2018-06-16T18:05:24Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3874227" lon="-122.1545479">
                <ele>0.0</ele>
                <time>2018-06-16T18:05:29Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3875286" lon="-122.1552951">
                <ele>0.0</ele>
                <time>2018-06-16T18:05:35Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3876157" lon="-122.1559089">
                <ele>0.0</ele>
                <time>2018-06-16T18:05:41Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3876548" lon="-122.1561851">
                <ele>0.0</ele>
                <time>2018-06-16T18:05:47Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3877197" lon="-122.1567999">
                <ele>0.0</ele>
                <time>2018-06-16T18:05:52Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3877117" lon="-122.1568297">
                <ele>0.0</ele>
                <time>2018-06-16T18:05:57Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3877453" lon="-122.1568174">
                <ele>0.0</ele>
                <time>2018-06-16T18:06:03Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3877396" lon="-122.1567975">
                <ele>0.0</ele>
                <time>2018-06-16T18:06:09Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3877182" lon="-122.1567577">
                <ele>0.0</ele>
                <time>2018-06-16T18:06:21Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3877179" lon="-122.1567931">
                <ele>0.0</ele>
                <time>2018-06-16T18:06:26Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.38769" lon="-122.1568582">
                <ele>0.0</ele>
                <time>2018-06-16T18:06:30Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3876989" lon="-122.1568881">
                <ele>0.0</ele>
                <time>2018-06-16T18:06:36Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3877045" lon="-122.1569071">
                <ele>0.0</ele>
                <time>2018-06-16T18:06:42Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3877083" lon="-122.1569198">
                <ele>0.0</ele>
                <time>2018-06-16T18:06:49Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3877487" lon="-122.1568986">
                <ele>0.0</ele>
                <time>2018-06-16T18:06:59Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3877658" lon="-122.1569229">
                <ele>0.0</ele>
                <time>2018-06-16T18:07:04Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3877707" lon="-122.1569087">
                <ele>0.0</ele>
                <time>2018-06-16T18:07:09Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3877726" lon="-122.1569212">
                <ele>0.0</ele>
                <time>2018-06-16T18:07:15Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3877423" lon="-122.1569349">
                <ele>0.0</ele>
                <time>2018-06-16T18:07:20Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3875701" lon="-122.1565209">
                <ele>0.0</ele>
                <time>2018-06-16T18:07:26Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3874544" lon="-122.1562427">
                <ele>0.0</ele>
                <time>2018-06-16T18:07:32Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3863669" lon="-122.1533979">
                <ele>0.0</ele>
                <time>2018-06-16T18:07:38Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3857236" lon="-122.151715">
                <ele>0.0</ele>
                <time>2018-06-16T18:07:43Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3851937" lon="-122.1503289">
                <ele>0.0</ele>
                <time>2018-06-16T18:07:49Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.384818" lon="-122.1493459">
                <ele>0.0</ele>
                <time>2018-06-16T18:07:53Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3841321" lon="-122.1478047">
                <ele>0.0</ele>
                <time>2018-06-16T18:07:58Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3881437" lon="-122.161324">
                <ele>0.0</ele>
                <time>2018-06-16T18:08:03Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3893841" lon="-122.1655042">
                <ele>0.0</ele>
                <time>2018-06-16T18:08:09Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3898054" lon="-122.1669239">
                <ele>0.0</ele>
                <time>2018-06-16T18:08:14Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3892488" lon="-122.1643476">
                <ele>0.0</ele>
                <time>2018-06-16T18:08:20Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3885967" lon="-122.1611984">
                <ele>0.0</ele>
                <time>2018-06-16T18:08:25Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3885484" lon="-122.1586955">
                <ele>0.0</ele>
                <time>2018-06-16T18:08:30Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3885179" lon="-122.1571198">
                <ele>0.0</ele>
                <time>2018-06-16T18:08:35Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3884964" lon="-122.1560021">
                <ele>0.0</ele>
                <time>2018-06-16T18:08:40Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3884872" lon="-122.1555267">
                <ele>0.0</ele>
                <time>2018-06-16T18:08:47Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.388162" lon="-122.1561257">
                <ele>0.0</ele>
                <time>2018-06-16T18:08:52Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3879276" lon="-122.1565573">
                <ele>0.0</ele>
                <time>2018-06-16T18:08:58Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3877912" lon="-122.1568084">
                <ele>0.0</ele>
                <time>2018-06-16T18:09:04Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.38774" lon="-122.1569028">
                <ele>0.0</ele>
                <time>2018-06-16T18:09:09Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3877228" lon="-122.1569344">
                <ele>0.0</ele>
                <time>2018-06-16T18:09:14Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3877177" lon="-122.1569439">
                <ele>0.0</ele>
                <time>2018-06-16T18:09:20Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3875818" lon="-122.1597074">
                <ele>0.0</ele>
                <time>2018-06-16T18:09:37Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3876476" lon="-122.1602331">
                <ele>0.0</ele>
                <time>2018-06-16T18:09:44Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3876604" lon="-122.1603355">
                <ele>0.0</ele>
                <time>2018-06-16T18:09:50Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3876641" lon="-122.1603657">
                <ele>0.0</ele>
                <time>2018-06-16T18:09:56Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3876352" lon="-122.1604133">
                <ele>0.0</ele>
                <time>2018-06-16T18:10:02Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3875106" lon="-122.1612984">
                <ele>0.0</ele>
                <time>2018-06-16T18:10:07Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3874338" lon="-122.1618445">
                <ele>0.0</ele>
                <time>2018-06-16T18:10:12Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3873694" lon="-122.1623024">
                <ele>0.0</ele>
                <time>2018-06-16T18:10:17Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3873115" lon="-122.1627134">
                <ele>0.0</ele>
                <time>2018-06-16T18:10:22Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3869683" lon="-122.1634905">
                <ele>0.0</ele>
                <time>2018-06-16T18:10:27Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3869521" lon="-122.1635271">
                <ele>0.0</ele>
                <time>2018-06-16T18:10:33Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3869383" lon="-122.1638843">
                <ele>0.0</ele>
                <time>2018-06-16T18:10:39Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3868931" lon="-122.164185">
                <ele>0.0</ele>
                <time>2018-06-16T18:10:45Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3866954" lon="-122.1653917">
                <ele>0.0</ele>
                <time>2018-06-16T18:10:51Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.386676" lon="-122.1655117">
                <ele>0.0</ele>
                <time>2018-06-16T18:10:56Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3858875" lon="-122.1654691">
                <ele>0.0</ele>
                <time>2018-06-16T18:11:02Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3852657" lon="-122.1654335">
                <ele>0.0</ele>
                <time>2018-06-16T18:11:08Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3850054" lon="-122.1657165">
                <ele>0.0</ele>
                <time>2018-06-16T18:11:15Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3849142" lon="-122.1658134">
                <ele>0.0</ele>
                <time>2018-06-16T18:11:19Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3849092" lon="-122.1663388">
                <ele>0.0</ele>
                <time>2018-06-16T18:11:24Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3848854" lon="-122.1662836">
                <ele>0.0</ele>
                <time>2018-06-16T18:11:30Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3848682" lon="-122.1663768">
                <ele>0.0</ele>
                <time>2018-06-16T18:11:35Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3848407" lon="-122.1666131">
                <ele>0.0</ele>
                <time>2018-06-16T18:11:40Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3847654" lon="-122.1674632">
                <ele>0.0</ele>
                <time>2018-06-16T18:11:45Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.384749" lon="-122.1677247">
                <ele>0.0</ele>
                <time>2018-06-16T18:11:51Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.384759" lon="-122.1676996">
                <ele>0.0</ele>
                <time>2018-06-16T18:11:56Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.384781" lon="-122.1680555">
                <ele>0.0</ele>
                <time>2018-06-16T18:12:07Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3847515" lon="-122.1689054">
                <ele>0.0</ele>
                <time>2018-06-16T18:12:12Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3849497" lon="-122.1693877">
                <ele>51.900001525878906</ele>
                <time>2018-06-16T18:12:18Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3850862" lon="-122.1696837">
                <ele>0.0</ele>
                <time>2018-06-16T18:12:25Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3853011" lon="-122.1699888">
                <ele>0.0</ele>
                <time>2018-06-16T18:12:30Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3853151" lon="-122.1701117">
                <ele>0.0</ele>
                <time>2018-06-16T18:12:36Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3853359" lon="-122.1702049">
                <ele>0.0</ele>
                <time>2018-06-16T18:12:40Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3853673" lon="-122.1702475">
                <ele>0.0</ele>
                <time>2018-06-16T18:12:45Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3853825" lon="-122.1702681">
                <ele>0.0</ele>
                <time>2018-06-16T18:12:51Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3853256" lon="-122.1703239">
                <ele>0.0</ele>
                <time>2018-06-16T18:12:57Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3852835" lon="-122.1703652">
                <ele>0.0</ele>
                <time>2018-06-16T18:13:02Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3852493" lon="-122.1703987">
                <ele>0.0</ele>
                <time>2018-06-16T18:13:08Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3852033" lon="-122.1704438">
                <ele>0.0</ele>
                <time>2018-06-16T18:13:14Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3851865" lon="-122.1704487">
                <ele>0.0</ele>
                <time>2018-06-16T18:13:21Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3851777" lon="-122.1704512">
                <ele>0.0</ele>
                <time>2018-06-16T18:13:27Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3866757" lon="-122.1732129">
                <ele>0.0</ele>
                <time>2018-06-16T18:13:38Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.386821" lon="-122.1734797">
                <ele>0.0</ele>
                <time>2018-06-16T18:13:44Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3869485" lon="-122.1737139">
                <ele>0.0</ele>
                <time>2018-06-16T18:13:50Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3870327" lon="-122.1738686">
                <ele>0.0</ele>
                <time>2018-06-16T18:13:56Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3870798" lon="-122.1739551">
                <ele>0.0</ele>
                <time>2018-06-16T18:14:01Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3871001" lon="-122.1739924">
                <ele>0.0</ele>
                <time>2018-06-16T18:14:07Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3871117" lon="-122.1740138">
                <ele>0.0</ele>
                <time>2018-06-16T18:14:13Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3871193" lon="-122.1740276">
                <ele>0.0</ele>
                <time>2018-06-16T18:14:19Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3860355" lon="-122.1720441">
                <ele>0.0</ele>
                <time>2018-06-16T18:14:25Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3856844" lon="-122.1714014">
                <ele>0.0</ele>
                <time>2018-06-16T18:14:30Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3854718" lon="-122.1710123">
                <ele>0.0</ele>
                <time>2018-06-16T18:14:36Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3853397" lon="-122.1707705">
                <ele>0.0</ele>
                <time>2018-06-16T18:14:42Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3852819" lon="-122.1706648">
                <ele>0.0</ele>
                <time>2018-06-16T18:14:48Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3852487" lon="-122.170604">
                <ele>0.0</ele>
                <time>2018-06-16T18:14:54Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3852272" lon="-122.1705646">
                <ele>0.0</ele>
                <time>2018-06-16T18:15:00Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3852123" lon="-122.1705373">
                <ele>0.0</ele>
                <time>2018-06-16T18:15:05Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3852015" lon="-122.1705176">
                <ele>0.0</ele>
                <time>2018-06-16T18:15:10Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3851935" lon="-122.170503">
                <ele>0.0</ele>
                <time>2018-06-16T18:15:15Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3851805" lon="-122.1704793">
                <ele>0.0</ele>
                <time>2018-06-16T18:15:20Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3851752" lon="-122.1704696">
                <ele>0.0</ele>
                <time>2018-06-16T18:15:26Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3851696" lon="-122.1704593">
                <ele>0.0</ele>
                <time>2018-06-16T18:15:44Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3841939" lon="-122.1733632">
                <ele>0.0</ele>
                <time>2018-06-16T18:15:59Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3850611" lon="-122.1880192">
                <ele>0.0</ele>
                <time>2018-06-16T18:20:05Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3849269" lon="-122.187988">
                <ele>0.0</ele>
                <time>2018-06-16T18:20:08Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3848846" lon="-122.1880963">
                <ele>0.0</ele>
                <time>2018-06-16T18:20:13Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3848734" lon="-122.1881249">
                <ele>0.0</ele>
                <time>2018-06-16T18:20:19Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3849582" lon="-122.1883005">
                <ele>0.0</ele>
                <time>2018-06-16T18:20:25Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3849947" lon="-122.1883761">
                <ele>0.0</ele>
                <time>2018-06-16T18:20:30Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3850263" lon="-122.1884413">
                <ele>0.0</ele>
                <time>2018-06-16T18:20:36Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3850424" lon="-122.1884747">
                <ele>0.0</ele>
                <time>2018-06-16T18:20:42Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3837625" lon="-122.1912033">
                <ele>0.0</ele>
                <time>2018-06-16T18:20:47Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.383549" lon="-122.1916586">
                <ele>0.0</ele>
                <time>2018-06-16T18:20:52Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3834219" lon="-122.1917775">
                <ele>0.0</ele>
                <time>2018-06-16T18:20:58Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3832751" lon="-122.1921445">
                <ele>0.0</ele>
                <time>2018-06-16T18:21:03Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3833314" lon="-122.1920735">
                <ele>0.0</ele>
                <time>2018-06-16T18:21:09Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3832451" lon="-122.1920985">
                <ele>0.0</ele>
                <time>2018-06-16T18:21:15Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3826557" lon="-122.1926873">
                <ele>0.0</ele>
                <time>2018-06-16T18:21:21Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3824899" lon="-122.1928529">
                <ele>0.0</ele>
                <time>2018-06-16T18:21:26Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3824017" lon="-122.1930171">
                <ele>0.0</ele>
                <time>2018-06-16T18:21:32Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3823229" lon="-122.1932277">
                <ele>0.0</ele>
                <time>2018-06-16T18:21:38Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.382248" lon="-122.193428">
                <ele>0.0</ele>
                <time>2018-06-16T18:21:45Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3822364" lon="-122.1936519">
                <ele>0.0</ele>
                <time>2018-06-16T18:21:51Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3821239" lon="-122.193649">
                <ele>0.0</ele>
                <time>2018-06-16T18:21:56Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3821392" lon="-122.193698">
                <ele>0.0</ele>
                <time>2018-06-16T18:22:01Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3821368" lon="-122.1937334">
                <ele>0.0</ele>
                <time>2018-06-16T18:22:07Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3821172" lon="-122.1940398">
                <ele>0.0</ele>
                <time>2018-06-16T18:22:19Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3819225" lon="-122.194159">
                <ele>0.0</ele>
                <time>2018-06-16T18:22:24Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3819613" lon="-122.1940832">
                <ele>0.0</ele>
                <time>2018-06-16T18:22:30Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3820104" lon="-122.1939872">
                <ele>0.0</ele>
                <time>2018-06-16T18:22:37Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.382052" lon="-122.1939059">
                <ele>0.0</ele>
                <time>2018-06-16T18:22:42Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3820796" lon="-122.1938519">
                <ele>0.0</ele>
                <time>2018-06-16T18:22:48Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3814609" lon="-122.1931981">
                <ele>0.0</ele>
                <time>2018-06-16T18:22:54Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3810717" lon="-122.1927867">
                <ele>0.0</ele>
                <time>2018-06-16T18:23:00Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3807661" lon="-122.1924637">
                <ele>0.0</ele>
                <time>2018-06-16T18:23:06Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3806078" lon="-122.1922965">
                <ele>0.0</ele>
                <time>2018-06-16T18:23:12Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3805099" lon="-122.192193">
                <ele>0.0</ele>
                <time>2018-06-16T18:23:18Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3800783" lon="-122.1943343">
                <ele>0.0</ele>
                <time>2018-06-16T18:23:23Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3794905" lon="-122.1964429">
                <ele>0.0</ele>
                <time>2018-06-16T18:23:29Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3794416" lon="-122.1962632">
                <ele>0.0</ele>
                <time>2018-06-16T18:23:35Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3794005" lon="-122.1963469">
                <ele>0.0</ele>
                <time>2018-06-16T18:23:40Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3793678" lon="-122.1963618">
                <ele>0.0</ele>
                <time>2018-06-16T18:23:46Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3793507" lon="-122.1963366">
                <ele>0.0</ele>
                <time>2018-06-16T18:23:51Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3792292" lon="-122.196494">
                <ele>0.0</ele>
                <time>2018-06-16T18:23:56Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3791205" lon="-122.1966836">
                <ele>0.0</ele>
                <time>2018-06-16T18:24:03Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3790215" lon="-122.1965123">
                <ele>0.0</ele>
                <time>2018-06-16T18:24:08Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3790569" lon="-122.1965502">
                <ele>0.0</ele>
                <time>2018-06-16T18:24:14Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3785454" lon="-122.1968616">
                <ele>0.0</ele>
                <time>2018-06-16T18:24:19Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3781264" lon="-122.1971166">
                <ele>0.0</ele>
                <time>2018-06-16T18:24:24Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.377323" lon="-122.1976944">
                <ele>0.0</ele>
                <time>2018-06-16T18:24:30Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3767449" lon="-122.1981898">
                <ele>0.0</ele>
                <time>2018-06-16T18:24:35Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3765536" lon="-122.1985962">
                <ele>0.0</ele>
                <time>2018-06-16T18:24:40Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3765269" lon="-122.1986219">
                <ele>0.0</ele>
                <time>2018-06-16T18:24:45Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3766089" lon="-122.1987701">
                <ele>0.0</ele>
                <time>2018-06-16T18:24:50Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3766482" lon="-122.1988417">
                <ele>0.0</ele>
                <time>2018-06-16T18:24:55Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3768137" lon="-122.1992217">
                <ele>0.0</ele>
                <time>2018-06-16T18:25:00Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3769212" lon="-122.1995779">
                <ele>0.0</ele>
                <time>2018-06-16T18:25:06Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3770749" lon="-122.1998874">
                <ele>0.0</ele>
                <time>2018-06-16T18:25:12Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3771032" lon="-122.1999502">
                <ele>0.0</ele>
                <time>2018-06-16T18:25:18Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3770759" lon="-122.2000138">
                <ele>0.0</ele>
                <time>2018-06-16T18:25:24Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3770285" lon="-122.2002161">
                <ele>0.0</ele>
                <time>2018-06-16T18:25:30Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3769694" lon="-122.2007576">
                <ele>0.0</ele>
                <time>2018-06-16T18:25:36Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3770027" lon="-122.2009898">
                <ele>0.0</ele>
                <time>2018-06-16T18:25:41Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3770119" lon="-122.2010513">
                <ele>0.0</ele>
                <time>2018-06-16T18:25:46Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.376978" lon="-122.2011252">
                <ele>0.0</ele>
                <time>2018-06-16T18:25:53Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3769503" lon="-122.2012508">
                <ele>0.0</ele>
                <time>2018-06-16T18:25:58Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3767136" lon="-122.2012865">
                <ele>0.0</ele>
                <time>2018-06-16T18:26:04Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.376129" lon="-122.2014417">
                <ele>0.0</ele>
                <time>2018-06-16T18:26:09Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3755856" lon="-122.2015274">
                <ele>0.0</ele>
                <time>2018-06-16T18:26:14Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3754883" lon="-122.2015836">
                <ele>0.0</ele>
                <time>2018-06-16T18:26:20Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3754965" lon="-122.2016217">
                <ele>0.0</ele>
                <time>2018-06-16T18:26:26Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.375411" lon="-122.2017276">
                <ele>0.0</ele>
                <time>2018-06-16T18:26:32Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3753103" lon="-122.2027937">
                <ele>0.0</ele>
                <time>2018-06-16T18:26:37Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3752514" lon="-122.2034436">
                <ele>0.0</ele>
                <time>2018-06-16T18:26:43Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3752327" lon="-122.2035346">
                <ele>0.0</ele>
                <time>2018-06-16T18:26:49Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3752288" lon="-122.2035534">
                <ele>0.0</ele>
                <time>2018-06-16T18:26:55Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3752788" lon="-122.2035451">
                <ele>0.0</ele>
                <time>2018-06-16T18:27:07Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.375044" lon="-122.203921">
                <ele>0.0</ele>
                <time>2018-06-16T18:27:13Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3749134" lon="-122.20413">
                <ele>0.0</ele>
                <time>2018-06-16T18:27:19Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3748046" lon="-122.2043042">
                <ele>0.0</ele>
                <time>2018-06-16T18:27:24Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3741785" lon="-122.2051749">
                <ele>0.0</ele>
                <time>2018-06-16T18:27:31Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3741051" lon="-122.205277">
                <ele>0.0</ele>
                <time>2018-06-16T18:27:36Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3739941" lon="-122.2054366">
                <ele>0.0</ele>
                <time>2018-06-16T18:27:42Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3738674" lon="-122.205567">
                <ele>0.0</ele>
                <time>2018-06-16T18:27:48Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3738405" lon="-122.2055963">
                <ele>0.0</ele>
                <time>2018-06-16T18:27:54Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3738037" lon="-122.2057637">
                <ele>0.0</ele>
                <time>2018-06-16T18:28:00Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.373776" lon="-122.2058645">
                <ele>0.0</ele>
                <time>2018-06-16T18:28:05Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3737719" lon="-122.205884">
                <ele>0.0</ele>
                <time>2018-06-16T18:28:11Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3737468" lon="-122.2059026">
                <ele>0.0</ele>
                <time>2018-06-16T18:28:16Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.37369" lon="-122.2060416">
                <ele>132.5</ele>
                <time>2018-06-16T18:28:22Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3735465" lon="-122.2062738">
                <ele>132.5</ele>
                <time>2018-06-16T18:28:27Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3735022" lon="-122.2063328">
                <ele>132.5</ele>
                <time>2018-06-16T18:28:32Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3734558" lon="-122.2063668">
                <ele>132.5</ele>
                <time>2018-06-16T18:28:37Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3734926" lon="-122.2063439">
                <ele>0.0</ele>
                <time>2018-06-16T18:28:44Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3735068" lon="-122.2063211">
                <ele>0.0</ele>
                <time>2018-06-16T18:28:50Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3734826" lon="-122.2063933">
                <ele>0.0</ele>
                <time>2018-06-16T18:28:56Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3733269" lon="-122.2066072">
                <ele>0.0</ele>
                <time>2018-06-16T18:29:01Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.373207" lon="-122.2067813">
                <ele>0.0</ele>
                <time>2018-06-16T18:29:06Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3728585" lon="-122.2074523">
                <ele>0.0</ele>
                <time>2018-06-16T18:29:13Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3727945" lon="-122.2075079">
                <ele>0.0</ele>
                <time>2018-06-16T18:29:18Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3727372" lon="-122.2075563">
                <ele>0.0</ele>
                <time>2018-06-16T18:29:24Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3727124" lon="-122.2075679">
                <ele>0.0</ele>
                <time>2018-06-16T18:29:29Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3727064" lon="-122.207714">
                <ele>0.0</ele>
                <time>2018-06-16T18:29:34Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3727021" lon="-122.2077409">
                <ele>0.0</ele>
                <time>2018-06-16T18:29:39Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3726926" lon="-122.2078079">
                <ele>0.0</ele>
                <time>2018-06-16T18:29:44Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3727067" lon="-122.2078027">
                <ele>0.0</ele>
                <time>2018-06-16T18:29:49Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3727116" lon="-122.2077464">
                <ele>0.0</ele>
                <time>2018-06-16T18:29:55Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3726552" lon="-122.2074498">
                <ele>0.0</ele>
                <time>2018-06-16T18:30:02Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.3725975" lon="-122.2074761">
                <ele>0.0</ele>
                <time>2018-06-16T18:30:08Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.372587" lon="-122.2074203">
                <ele>0.0</ele>
                <time>2018-06-16T18:30:17Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.37261" lon="-122.2073875">
                <ele>0.0</ele>
                <time>2018-06-16T18:30:23Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
            <trkpt lat="37.372576" lon="-122.2077049">
                <ele>0.0</ele>
                <time>2018-06-16T18:30:28Z</time>
                <extensions>
                    <gpxtpx:TrackPointExtension>
                        <gpxtpx:hr>69</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                </extensions>
            </trkpt>
        </trkseg>
    </trk>
</gpx>
""")

        trkpt = mydoc.getElementsByTagName('trkpt')
        time = mydoc.getElementsByTagName('time')
        ele = mydoc.getElementsByTagName('ele')
        hr = mydoc.getElementsByTagName('gpxtpx:hr')

        lats = []
        longs = []
        times = []
        eles = []
        hrs = []
        dates = []
        parsed_times = []

        for elem in trkpt:
            lats.append(elem.attributes['lat'].value)
            longs.append(elem.attributes['lon'].value)

        for elem in time:
            times.append(elem.firstChild.data)

        for elem in hr:
            hrs.append(elem.firstChild.data)

        times.pop(0)
        base_time = iso_to_epoch(times[0])

        time_differences = []

        for item in times:
            time_differences.append(iso_to_epoch(item) - base_time)
            date_obj = (dateutil.parser.parse(item))
            dates.append(str(date_obj.year) + "-" + str(date_obj.month) + "-" + str(date_obj.day))
            parsed_times.append(str(date_obj.hour) + ":" + str(date_obj.minute) + ":" + str(date_obj.second))

        for elem in ele:
            eles.append(elem.firstChild.data)

        data = {'date': dates,
                'time': parsed_times,
                'latitude': lats,
                'longitude': longs,
                'elevation': eles,
                'heart_rate': hrs}

        df = pd.DataFrame(data=data)

        df = df[['date', 'time', 'latitude', 'longitude', 'elevation', 'heart_rate']]

        df.to_csv('csv_temp/' + name, encoding='utf-8', index=False)

convert = Converter('test', 'test.csv')