import json

from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

# my_map = Map()
#
# data = [
#     ("北京市", 99),
#     ("上海市", 199),
#     ("湖南省", 299),
#     ("台湾省", 399),
#     ("广东省", 99)
# ]
#
# # 添加数据
# my_map.add("测试地图", data, "china")
#
# my_map.set_global_opts(
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[
#             {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
#             {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
#             {"min": 100, "max": 500, "label": "100-500", "color": "#990033"}
#         ]
#     )
# )
#
# # 绘图
# my_map.render()

covid_file = open("../data/covid_19.txt", "r", encoding="UTF-8")
file_data = covid_file.read()

covid_file.close()

covid_data = json.loads(file_data)

province_data_list = covid_data['areaTree'][0]['children']

data_list = []

for province_data in province_data_list:
    province_name = province_data['name']
    province_confirm = province_data['total']['confirm']
    data_list.append((province_name, province_confirm))

covid_map = Map()

covid_map.add("各省份确诊人数", data_list, "china")

covid_map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
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

covid_map.render("全国疫情地图.html")
