PlottingCGM

Copyright 2017 Jason Behrstock
jason.behrstock@gmail.com
Released under the GPL.

PlottingStrava combines information from Strava or other GPX data and a Dexcom CGM (via Clarity) and plots the Strava bike/run data on google maps with the BGs displayed via color (Ranging from red as low through green, to blue as high).

Input: GPX file for GPS data and CSV file from Dexcom Clarity.

Output: html file to display the map.


Required packages:
datetime
gmplot
gpxpy
tzwhere

(a few more if you want to use mathplotlib instead of gmplot)


Other Comments:

1. There are (unused) auxiliary functions in the strava_import.py file which, if desired, allow one to easily import data from a CSV file instead of a box file.
2. There are (unused) auxiliary functions in the plotting.py file which allow one to plot using mathplotlib instead of google maps. This version allows one to display the BG range with a color bar legend. One could easily add openstreetmap data to this map. I’d like to find a way to add the color bar to the google maps data (any ideas on this are welcome).

