import webbrowser

import folium
from folium import plugins
from folium.plugins import Search

m = folium.Map(location=[49.276, 19.90], zoom_start=4, tiles="cartodbpositron", max_zoom=18, min_zoom=2.3)


# folium.GeoJson(data=open('world_geojson_from_prg.json', 'r', encoding='utf-8-sig').read(),
#                style_function=lambda x: {'fillColor': 'orange'},
#                tooltip=folium.GeoJsonTooltip(fields=('NAME', 'POP2005'),
#                                              aliases=('Country', 'Population')))


def colorPicker(population):
    if population < 10000000:
        return 'green'
    elif population >= 10000000 and population < 500000000:
        return 'orange'
    else:
        return 'red'


folium.GeoJson(open('world_geojson_from_prg.json', 'r', encoding='utf-8-sig').read(),
               name='Population',
               # style_function=lambda x: {'fillColor': colorPicker(x['properties']['POP2005'])},
               style_function=lambda x: {'fillColor': 'white'},
               tooltip=folium.GeoJsonTooltip(fields=('NAME', 'POP2005',),
                                             aliases=('Country', 'Population')),
               show=True).add_to(m)

# [longitude, latitude]
points = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "name": "one"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [12.4963655, 41.9027835]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "two"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [19.0402, 47.4979]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "three"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [25.4858, 42.7339]
            }
        }
    ]
}

geojson_obj = folium.GeoJson(points).add_to(m)

statesearch = Search(layer=geojson_obj,
                     geom_type='Point',
                     placeholder="Search",
                     collapsed=False,
                     search_label='name',
                     search_zoom=4,
                     position='topright'
                     ).add_to(m)

m.save('example.html')
webbrowser.open("example.html", m)
