from pyecharts.charts import Line

line = Line()

line.add_xaxis(['中国', '美国', '英国'])

line.add_yaxis("GDP", [30, 50 ,10])

if __name__ == '__main__':
    line.render()

