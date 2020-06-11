import folium
import pandas
import webbrowser
from folium import IFrame


def auto_open(path, var):
    html_page = f'{path}'
    var.save(html_page)
    new = 2
    webbrowser.open(html_page, new=new)


def color_picker(population):
    if population > 100000000:
        return 'green'


# map = folium.Map(location=[49.276, 19.90], zoom_start=5, tiles="OpenStreetMap", max_zoom=18, min_zoom=2.3)
map = folium.Map(location=[49.276, 19.90], zoom_start=5, tiles="cartodbpositron", max_zoom=18, min_zoom=2.3)

# Hover over
fgp = folium.FeatureGroup(name="Hover - orange", overlay=True, control=True, show=False)
fgp.add_child(folium.GeoJson(data=open('world_geojson_from_prg.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'orange'},
                             tooltip=folium.GeoJsonTooltip(fields=('NAME', 'POP2005'),
                                                           aliases=('Country', 'Population'))))
# Tricolor
fgp2 = folium.FeatureGroup(name="Population - tricolor", overlay=True, control=True, show=True)
fgp2.add_child(folium.GeoJson(data=open('world_geojson_from_prg.json', 'r', encoding='utf-8-sig').read(),
                              style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                              else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Italy black
fgp3 = folium.FeatureGroup(name="Italy dark", overlay=True, control=True, show=False)
fgp3.add_child(folium.GeoJson(data=open('world_geojson_from_prg.json', 'r', encoding='utf-8-sig').read(),
                              style_function=lambda x: {'fillColor': 'darkred' if x['properties']['NAME'] == "Italy"
                              else 'white'}))

countries = ("Hungary", "Bulgaria", "Belgium")

# LIST COLORED
fgp4 = folium.FeatureGroup(name="LIST COLORED", overlay=True, control=True, show=False)
fgp4.add_child(folium.GeoJson(data=open('world_geojson_from_prg.json', 'r', encoding='utf-8-sig').read(),
                              style_function=lambda x: {'fillColor': 'darkred' if x['properties']['NAME'] in countries
                              else 'white'}))



# text = 'your text here'
#
# iframe = folium.IFrame(text, width=200, height=100)
# popup = folium.Popup(iframe, max_width=3000)
#
# Text = folium.Marker(location=[49.276, 19.90], popup=popup,
#                      icon=folium.Icon(icon_color='green'))
#
# map.add_child(Text)


map.add_child(fgp)
map.add_child(fgp2)
map.add_child(fgp3)
map.add_child(fgp4)
map.add_child(folium.LayerControl(collapsed=False))
map.save("Mapi.html")
# auto_open("Mapi.html", map)

webbrowser.open("Mapi.html", map)
