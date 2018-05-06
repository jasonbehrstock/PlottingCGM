
import gmplot


def plotting_gmap(lat,long,SG,outputname):

    gmap = gmplot.GoogleMapPlotter(sum(lat)/len(lat), sum(long)/len(long), 13)


    #gmap.scatter(lat, long, edge_width=3, marker=False)

    i=0
    while i <len(lat):
        a=[lat[i]]
        b=[long[i]]
        #print(color(SG[i]),SG[i])
        gmap.scatter(a,b,color(SG[i]) , edge_width=3, marker=False)
        i+=1

    gmap.draw(outputname)
 

def rgb(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    ratio = 2 * (value-minimum) / (maximum - minimum)
    r = int(max(0, 255*(1 - ratio)))
    b = int(max(0, 255*(ratio - 1)))
    g = 255 - b - r
    return r, g, b

def rgb_value(value):
    if value<50:
        return 255,0,0
    elif value>300:
        return 0,0,255
    else:
        return rgb(50, 250, value)

def color(value):
    return "#%02x%02x%02x" % rgb_value(value)






############## Below is an alternate way to plot using Basemap
############## the only current advantage of this is that it is easy to display a colorbar
############## and also to modify the color specture.

############## one could consider using the following function with openstreeetmap

#####uncomment the next two import commands if using the plotting below
#import numpy as np
#from mpl_toolkits.basemap  import Basemap
#import matplotlib as mpl
#import matplotlib.pyplot as plt

def plotting_basemap(lat,long,SG):

    ### Define the projection, scale, the corners of the map, and the resolution.

        ####Currently hardwired for a particular map
        ###if this is used in the future, replace boundary corners with max/min of lat/long


    #####Central park ride:
    #m = Basemap(projection='merc',llcrnrlat=40.75,urcrnrlat=40.8,\
    #            llcrnrlon=-74.0,urcrnrlon=-73.95,lat_ts=.001,resolution='c')

    m = Basemap(projection='merc',llcrnrlat=40.75,urcrnrlat=41.0,\
                llcrnrlon=-74.1,urcrnrlon=-73.75,lat_ts=.001,resolution='c')


    # Draw the coastlines
    m.drawcoastlines()
    ## Color the continents
    #m.fillcontinents(color='coral',lake_color='aqua')


    ## draw parallels and meridians.
    #m.drawparallels(np.arange(-90.,91.,30.))
    #m.drawmeridians(np.arange(-180.,181.,60.))
    ## fill in the oceans
    #m.drawmapboundary(fill_color='aqua')

    x, y = m(long,lat)
    #m.scatter(x,y,3,marker='o',color='k')
    m.scatter(x,y,3,marker='o',c=SG)
    m.colorbar()


    plt.title("BG data")
    plt.show()




