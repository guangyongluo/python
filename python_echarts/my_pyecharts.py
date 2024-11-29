import json

from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

# line = Line()
#
# line.add_xaxis(['中国', '美国', '英国'])
#
# line.add_yaxis("GDP", [30, 50 ,10])
#
# line.render()

file_usa = open("../data/usa.txt", "r", encoding="UTF-8")
usa_data = file_usa.read()

file_india = open("../data/india.txt", "r", encoding="UTF-8")
india_data = file_india.read()

file_japan = open("../data/japan.txt", "r", encoding="UTF-8")
japan_data = file_japan.read()

usa_data = usa_data.replace("jsonp_1629344292311_69436(", "")
usa_data = usa_data[:-2]

india_data = india_data.replace("jsonp_1629350745930_63180(", "")
india_data = india_data[:-2]

japan_data = japan_data.replace("jsonp_1629350871167_29498(", "")
japan_data = japan_data[:-2]

usa_dict = json.loads(usa_data)
india_dict = json.loads(india_data)
japan_dict = json.loads(japan_data)

usa_trend_data = usa_dict['data'][0]['trend']
usa_x_data = usa_trend_data['updateDate'][:314]
usa_y_data = usa_trend_data['list'][0]['data'][:314]

india_trend_data = india_dict['data'][0]['trend']
india_x_data = india_trend_data['updateDate'][:314]
india_y_data = india_trend_data['list'][0]['data'][:314]

japan_trend_data = japan_dict['data'][0]['trend']
japan_x_data = japan_trend_data['updateDate'][:314]
japan_y_data = japan_trend_data['list'][0]['data'][:314]

# 生成图表
line = Line()

# 添加x轴数据
line.add_xaxis(usa_x_data)

# 添加y轴数据
line.add_yaxis("美国确证人数", usa_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确证人数", india_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确证人数", japan_y_data, label_opts=LabelOpts(is_show=False))

# 设置全局选项
line.set_global_opts(
    # 标题设置
    title_opts=TitleOpts(title="2020年美日印三国确证人数对比图", pos_left="center", pos_bottom="1%")
)


if __name__ == '__main__':
    # 调用render方法，生成图表
    line.render()

    file_usa.close()
    file_india.close()
    file_japan.close()


