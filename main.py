import json
import simplekml
import utm

utm_x,utm_y,zone,letter = utm.from_latlon(52.39075, 16.951533)
utm_z=68
x =[]
y=[]
z=[]
x_wgs84 =[]
y_wgs84=[]
z_wgs84=[]

f = open('drones/Drone 4/trajectory.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['points']:
    x.append((i[1][0]+utm_x))
    y.append(i[1][1]+utm_y)
    z.append(i[1][2])

f.close()

for (a,b,c) in zip(x,y,z):
  a,b = utm.to_latlon(a, b, zone, northern=True)
  c=c+utm_z
  z_wgs84.append(c)
  x_wgs84.append(a)
  y_wgs84.append(b)

kml = simplekml.Kml()
ls = kml.newlinestring(name="Drone path")

for i in range (len(x)):
  ls.coords.addcoordinates([(y_wgs84[i],x_wgs84[i],z_wgs84[i])])

kml.save("trace_of_drone.kml")


