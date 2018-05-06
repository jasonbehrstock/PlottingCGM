
from strava_import import *
from plotting import *
from CGM_import_match import *

    

def main():
    CGM_filename=input('Enter name of Dexcom Clarity file (CGM info as csv file): ')
    if CGM_filename=='':
        CGM_filename='clarity.csv'

    strava_filename=input('Enter name of location data file (any GPX file): ')
    if strava_filename=='':
        strava_filename='strava.gpx'


    #CGM_filename='clarity.csv'
    #CGM_filename='clarity_7_8_17.csv'

    #strava_filename='Afternoon_Ride.csv'
    #strava_data=import_strava_locations_from_csv(strava_filename)

    #strava_filename='Afternoon_Ride_7_8_17.gpx'
    strava_data=import_strava_from_gpx(strava_filename)

    CGM_data=import_CGM_data(CGM_filename)

    match=match_strava_CGM(strava_data,CGM_data)

    Lat_values=[match[i]['Latitude'] for i in match]
    Long_values=[match[i]['Longitude'] for i in match]
    SG_values=[match[i]['SG'] for i in match]

    #output_name="BG_map.html"
    output_name=strava_filename[:-4]+"_CGM_map.html"
    plotting_gmap(Lat_values,Long_values,SG_values,output_name)
    #plotting_basemap(Lat_values,Long_values,SG_values)



if __name__ == '__main__':
    main()

