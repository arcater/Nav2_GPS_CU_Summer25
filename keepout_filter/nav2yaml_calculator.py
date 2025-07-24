from geonav_conversions import *

###########################################################################
# Begin User Input
###########################################################################

# Latitude and Longitude of your map origin
map_origin_lon = -75.00 # y
map_origin_lat = 44.663 # x

# World file data

#pixel size in the x and y direction
dpx = 0.00000107108
dpy = -0.00000107108

# Latitude and Longitude of the uper left pixel of your image
top_left_lon = -75.00272385428000632
top_left_lat = 44.66428934945999885

# Resolution of your image (horizontal, vertical)
image_resolution = (4258, 2925)

###########################################################################
# End User Input
###########################################################################

# Calculate lat and lon of the bottom left pixel of your image
bottom_left_lat = top_left_lat + (dpy * (image_resolution[1] - 1))
bottom_left_lon = top_left_lon

# Calculate lat and lon of the top left corner of your image
tlc_lat = top_left_lat - (dpx / 2)
tlc_lon = top_left_lon - (dpy / 2)

# Calculate lat and lon of the bottom left corner of your image
blc_lat = tlc_lat + (dpy * image_resolution[1])
blc_lon = tlc_lon

# Calculate lat and lon of the top right corner of your image
trc_lat = tlc_lat
trc_lon = tlc_lon + (dpx * image_resolution[0])

# Calculate map coordinates of 3 corners from you image
tlc = ll2xy(tlc_lat, tlc_lon, map_origin_lat, map_origin_lon)
blc = ll2xy(blc_lat, blc_lon, map_origin_lat, map_origin_lon)
trc = ll2xy(trc_lat, trc_lon, map_origin_lat, map_origin_lon)

# Calculate the height of the image in meters by
# subtracting the y coordinate of the two left corners
image_height_meters = abs(tlc[1] - blc[1])

# Determine the resolution parameter for the nav2 yaml file
# meters per pixel
yaml_resolution = image_height_meters / image_resolution[1]

# determine the width of the image from the yaml_resolution
implied_width_meters = yaml_resolution * image_resolution[0]

# Calculate the width of the image by
# subtracting the x coordinate of the two top corners
image_width_meters = abs(tlc[0] - trc[0])

# Calculate how much to scale the image horizontaly so it
# lines up with where it is expected on the map
percent_reduction = image_width_meters / implied_width_meters
new_image_resolution_x = image_resolution[0] * percent_reduction

print(f"yaml_resolution: {yaml_resolution}")
print(f"yaml_origin: [{blc[0]} ,{blc[1]}, 0]")
print(f"new_image_resolution_x: {round(new_image_resolution_x)}")

