import gpxpy

import pytz
from tzwhere import tzwhere


def find_timezone(lat,long):
    tz = tzwhere.tzwhere()
    timezone_str = tz.tzNameAt(lat, long)
    #print(timezone_str)

    local_timezone = pytz.timezone(timezone_str)
    return local_timezone


  
def gmt_to_local(time,local_timezone):

    gmt=pytz.timezone('GMT')

    time_gmt=gmt.localize(time)
    
    time_local=time_gmt.astimezone(local_timezone)

    time_clean=time_local.replace(tzinfo=None)
    #print(time,time_gmt,time_local,time_clean)

    return time_clean

    


def import_strava_from_gpx(pfilename):
#input: GPX file
#outputs a 'definition' which given a time as key
#outputs the latitude and longitude as floats.

    position_data={}
    with open(pfilename, 'r') as gpxfile:
        # print (pfilename)
        gpx = gpxpy.parse(gpxfile)

        timezone='GMT'
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    timezone=find_timezone(point.latitude,point.longitude)
                    break
                break
            break
        
        
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    timedate_clean=gmt_to_local(point.time,timezone)
                    #print(timedate_clean)
                    position_data[timedate_clean]={'Latitude':float (point.latitude), 'Longitude':float (point.longitude)}
                            ####'Elevation' : point.elevation
    return position_data   


################################# Below this is for CSV imports
################################# This is not used in current implemenation.



def import_strava_locations_from_csv(pfilename):
#from csv
#this outputs a 'definition' which given a time as key
#outputs the latitude and longitude as floats.

    ## Read file
    file_open_w = open(pfilename, 'r')
    #contents = file_open_w.readlines()

    position_data = {}

    with file_open_w as f:
        next(f)
        for line in f:
            line_split = line.split(',')

            timedate_clean = line_split[1]

            
            #timedate_split = line_split[1].split(' ')
            #timedate_split[0]=date, 2016-12-14
            #timedate_split[1]=time, 20:24:48

            position_data[timedate_clean]={'Latitude':float (line_split[2]), 'Longitude':float (line_split[3])}

    return position_data



def import_strava_date_from_csv():
    #from csv

    filename='Afternoon_Ride.csv'
    file_open_w = open(filename, 'r')
    
    with file_open_w as f:
        next(f)
        temp=f.readline()
        temp1=str(temp).split(',')
        temp2=temp1[1].split(' ')

        temp3=temp2[0]

    return temp3       


