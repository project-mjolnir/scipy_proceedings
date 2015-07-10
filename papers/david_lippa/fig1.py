pts = [(47.618874900000002, -122.1964424),
 (29.488524999999999, -98.570601199999999),
 (37.277239000000002, -121.88028559999999),
 (32.1702437, -110.91052620000001),
 (42.486862100000003, -71.197028200000005),
 (30.3129618, -97.853445300000004),
 (36.024881000000001, -79.876040500000002),
 (26.092246800000002, -80.367706299999995),
 (47.769761000000003, -122.1856538),
 (33.385969000000003, -84.173788000000002),
 (38.628791999999997, -90.194776599999997),
 (28.001427, -82.571681999999996),
 (42.508916200000009, -71.150593799999996),
 (35.930585000000001, -78.882419900000002),
 (37.380600999999999, -122.02050800000001),
 (34.100585299999999, -118.3449945),
 (29.733003799999999, -95.419411199999999),
 (33.916299000000002, -118.28280700000001),
 (26.2638812, -80.141950499999993),
 (34.013342999999999, -118.27794),
 (35.161099999999998, -106.6375),
 (41.939233000000002, -87.8777829),
 (42.012113999999997, -87.969560700000002),
 (42.047507299999999, -88.122128599999996),
 (37.355508200000003, -121.8512972),
 (35.765258000000003, -78.731181000000007),
 (29.922787599999999, -95.686415999999994),
 (35.345738900000001, -80.788582899999994),
 (30.1691711, -97.796608399999997),
 (33.446348, -112.043772),
 (39.6779607, -105.0047397),
 (37.399231100000002, -122.0455178),
 (33.738732599999999, -117.8220235),
 (38.620699999999999, -90.265799999999999),
 (37.792252300000001, -122.3941085),
 (28.386642999999999, -81.403953999999999),
 (38.694616000000003, -90.432343200000005),
 (38.553850099999998, -90.412987799999996),
 (33.744980599999998, -117.8376244),
 (30.263074, -97.743483800000007),
 (39.734492600000003, -105.0000469),
 (47.616529999999997, -122.13340549999999),
 (29.601104200000002, -98.538486500000005),
 (27.857520900000001, -82.829909400000005),
 (35.087552700000003, -89.930835000000002),
 (44.930048499999998, -93.385582999999997),
 (42.325126500000003, -71.585025799999997),
 (32.928766099999997, -97.019660899999991),
 (35.332892000000001, -80.819075999999995),
 (25.795235000000002, -80.378045999999998)]
pts = [(y, x) for x, y in pts]

# divide by 111000
circles = [([  47.66838863, -122.1718339 ], 11389.144550559206, 3),
 ([ 29.96696722, -98.10052504], 74665.581687680882, 5),
 ([  37.44096632, -122.03834342], 55656.680649132904, 5),
 ([  32.1702437, -110.9105262], 94992.608181311152, 1),
 ([ 42.4403016, -71.3108826], 33101.491753712049, 3),
 ([ 35.67987098, -79.81946006], 121519.43873626104, 5),
 ([ 26.05045433, -80.29590093], 29846.341270481953, 3),
 ([ 33.385969, -84.173788], 111319.9, 1),
 ([ 38.62448953, -90.3264769 ], 14668.685489703783, 4),
 ([ 28.08186363, -82.26851513], 102048.01644022643, 3),
 ([  33.9027881 , -118.11307788], 37192.653166721015, 5),
 ([ 29.8278957, -95.5529136], 18233.154179062341, 2),
 ([  35.1611, -106.6375], 111319.9, 1),
 ([ 41.9996181 , -87.98982407], 15663.253867876974, 3),
 ([  33.446348, -112.043772], 94992.608181311152, 1),
 ([  39.70622665, -105.0023933 ], 3157.3854637783279, 2),
 ([ 35.0875527, -89.930835 ], 111319.9, 1),
 ([ 44.9300485, -93.385583 ], 111319.9, 1),
 ([ 32.9287661, -97.0196609], 111319.9, 1)]
circles = [((lon, lat), rad / 111319.9, count) for (lat, lon), rad, count in circles]
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


m = Basemap(projection='merc',llcrnrlat=25,urcrnrlat=50,
            llcrnrlon=-125,urcrnrlon=-67)
m.drawcoastlines()
m.drawcountries()
m.drawstates()
for center, radius, count in circles:
    m.plot(center[0], center[1], 'bo', latlon=True, markersize=radius * 15,
           color='b', fillstyle='none')
for p in pts:
    m.plot(p[0], p[1], 'bo', latlon=True, markersize=3, color='c')
#plt.show()
plt.savefig('/tmp/figure1.svg', frameon=True, dpi=1000, bbox_inches='tight', pad_inches=0.05)