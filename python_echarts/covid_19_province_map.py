import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

file_data = open("../data/covid_19.txt", 'r', encoding='UTF-8')

covid_19_data = file_data.read()

file_data.close()

covid_19_dict = json.loads(covid_19_data)

henan_province_data = covid_19_dict['areaTree'][0]['children'][3]['children']

data_list = []

for city in henan_province_data:
    city_name = city['name'] + '市'
    city_confirm = city['total']['confirm']
    data_list.append((city_name, city_confirm))

cities_map = Map()

cities_map.add("河南省份确诊人数", data_list, "河南")

cities_map.set_global_opts(
    title_opts=TitleOpts(title="河南省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1~99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100~999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000~4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000~99人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "1~99人", "color": "#CC3333"},
            {"min": 100000,  "label": "100000+", "color": "#990033"},
        ]
    )
)

cities_map.render("河南省疫情地图.html")