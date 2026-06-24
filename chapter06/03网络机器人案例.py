from idlelib import __main__

import requests, csv
from lxml import html

# 定义常量
MOVIE_LIST_FILE = "resources/movie_list.csv"
TMDB_BASE_URL = "https://www.themoviedb.org"
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated" # 高分电影榜单的URL
TMDB_TOP


def get_movie_info(movie_info_url):
    # 1. 发送请求，获取电影详细信息
    response = requests.get(url=movie_info_url, timeout=60, headers={"accept-language": "zh-CN,zh;q=0.9"})

    # 2. 解析HTML内容，获取电影名称、评分、上映时间等信息
    movie_document = html.fromstring(response.text)

    # 3. 电影名称
    movie_name = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/a/text()')
    movie_year = movie_document.xpath('///*[@id="original_header"]/div[2]/section/div[1]/h2/span/text()')
    movie_release_date = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[2]/text()')
    movie_tags = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[3]/a/text()')
    movie_time = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[4]/text()')
    movie_score = movie_document.xpath('//*[@id="consensus_pill"]/div/div[1]/div/div/@data-percent')
    movie_language = movie_document.xpath('//*[@id="media_v4"]/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()')
    movie_director = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()')
    movie_author = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()')
    movie_slogan = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/h3[1]/text()')
    movie_summary = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/div/p/text()')
    return {
        "电影名": movie_name[0].strip() if movie_name else "",
        "电影年份": movie_year[0].strip() if movie_year else "",
        "上映时间": movie_release_date[0].strip() if movie_release_date else "",
        "电影类型": ",".join(movie_tags).strip() if movie_tags else "",
        "电影时长": movie_time[0].strip() if movie_time else "",
        "电影评分": movie_score[0].strip() if movie_score else "",
        "语言": movie_language[0].strip() if movie_language else "",
        "导演": movie_director[0].strip() if movie_director else "",
        "原著作者": movie_author[0].strip() if movie_author else "",
        "电影宣传语": movie_slogan[0].strip() if movie_slogan else "",
        "简介": movie_summary[0].strip() if movie_summary else ""
    }


def save_all_movies(all_moves):
    with open(MOVIE_LIST_FILE, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["电影名", "电影年份", "上映时间", "电影类型", "电影时长", "电影评分", "语言", "导演", "原著作者", "电影宣传语", "简介"])
        writer.writeheader()
        writer.writerows(all_moves)
    pass


# 主函数核心逻辑
def main():
    # 1.发送请求，获取高分电影榜单数据
    response = requests.get(url=TMDB_TOP_URL, timeout=60)

    # 2.解析HTML内容，获取电影列表
    document = html.fromstring(response.text)
    movie_list = document.xpath("//*[@id='page_1']/div[@class='card style_1']")

    # 3.遍历电影列表，获取电影名称、评分、上映时间等信息
    all_moves = []
    for movie in movie_list:
        movie_urls = movie.xpath('./div/div/a/@href')
        if movie_urls:
            movie_info_url = TMDB_BASE_URL + movie_urls[0]
            movie_info = get_movie_info(movie_info_url)
            all_moves.append(movie_info)
    print(all_moves)

    # 4.将电影信息保存到CSV文件中
    save_all_movies(all_moves)


if __main__:
    main()