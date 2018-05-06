
from datetime import datetime, timedelta



def import_timestamp(s):
    #see: http://strftime.org
    datetime_object = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
    ###check that month is "zero-padded" otherwise need %-m (also for hour)
    return datetime_object



def import_CGM_data(filename):
#import from clarity CSV file

#this outputs a 'definition' which given a time as key
#outputs the Sensor Glucose value.

    ## Read file
    file_open_w = open(filename, 'r')

    CGMdata = {}

    with file_open_w as f:
        next(f)
        for line in f:            
            line_split = line.split(',')

            if len(line_split)<2:
                continue
            if line_split[1].find('T')!=-1:
                #timedate_split = line_split[1].split('T')
                timedate_clean = line_split[1].replace('T',' ')
            #timedate example: 2016-12-20T19:32:02 
            #timedate_split[0]=date, 2016-12-14
            #timedate_split[1]=time, 20:24:48
            
                CGMdata[import_timestamp(timedate_clean)]={'SG':float (line_split[7])}

    return CGMdata


def match_strava_CGM(strava_data,CGM_data):

    relevantdata = {}

    time_stamps=list()
    for key in strava_data.keys():
        time_stamps.append((key,'fast'))
    for key in CGM_data.keys():
        time_stamps.append((key,'slow'))

    time_stamps.sort()


    
    
    currentbg=100

    for obj in time_stamps:
        if obj[1]=='slow':
            currentbg=CGM_data[obj[0]]
        if obj[1]=='fast':
            #relevantCGMdata[obj[0]]=currentbg
            relevantdata[obj[0]]={'SG':int (currentbg['SG']), 'Latitude':float (strava_data[obj[0]]['Latitude']), 'Longitude':float (strava_data[obj[0]]['Longitude'])}
            #print('fast:',relevantdata[obj[0]])

    return relevantdata

