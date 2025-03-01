from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(77.8946302, 29.8622079, 8)

# # Polygon
# golden_gate_park_lats, golden_gate_park_lons = zip(*[
#     (37.771269, -122.511015),
#     (37.773495, -122.464830),
#     (37.774797, -122.454538)
#     ])
# gmap.plot(golden_gate_park_lats, golden_gate_park_lons, 'cornflowerblue', edge_width=10)

# # Scatter points
# top_attraction_lats, top_attraction_lons = zip(*[
#     (37.769901, -122.498331),
#     (37.768645, -122.475328),
#     (37.771478, -122.468677),
#     (37.769867, -122.466102),
#     (37.767187, -122.467496),
#     (37.770104, -122.470436)
#     ])
# gmap.scatter(top_attraction_lats, top_attraction_lons, '#3B0B39', size=40, marker=False)

# # Marker
# hidden_gem_lat, hidden_gem_lon = 37.770776, -122.461689
# gmap.marker(hidden_gem_lat, hidden_gem_lon, '#3B0B39')

# Draw
gmap.draw("my_map.html")