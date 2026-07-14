import requests, csv
from lxml import html

# 定义常量
MOVIE_LIST_FILE = "resources/movie_list.csv"
TMDB_BASE_URL = "https://www.themoviedb.org"
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated" # 高分电影榜单的URL

TMDB_ITEMS_URL = "https://www.themoviedb.org/discover/movie/items"




def get_movie_info(movie_info_url):
    # 1. 发送请求，获取电影详细信息
    response = requests.get(url=movie_info_url, timeout=60, headers={"accept-language": "zh-CN,zh;q=0.9"})

    # 2. 解析HTML内容，获取电影名称、评分、上映时间等信息
    movie_document = html.fromstring(response.text)

    # 3. 电影名称
    movie_name = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/a/text()')
    movie_year = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/span/text()')
    movie_release_date = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class="release"]/text()')
    movie_tags = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class="genres"]/a/text()')
    movie_time = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class="runtime"]/text()')
    movie_score = movie_document.xpath('//*[@id="consensus_pill"]/div/div[1]/div/div/@data-percent')
    movie_language = movie_document.xpath('//*[@id="media_v4"]/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()')
    movie_director = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()')
    movie_author = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[position()>=2]/p[1]/a/text()')
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
        "导演": ",".join(movie_director).strip() if movie_director else "",
        "原著作者": ",".join(movie_author).strip() if movie_author else "",
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

    all_moves = []

    for page_num in range(1, 6):

        if page_num == 1:
            # 1.发送请求，获取高分电影榜单数据
            response = requests.get(url=TMDB_TOP_URL, timeout=60)
        else:
            response = requests.post(url=TMDB_ITEMS_URL, data=f"air_date.gte=&air_date.lte=&certification=&certification_country=HK&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2027-01-14&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=HK&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400", timeout=60)

        # 2.解析HTML内容，获取电影列表
        document = html.fromstring(response.text)
        movie_list = document.xpath("//*[@class='media-list-results contents']/div/div/div/a")

        # 3.遍历电影列表，获取电影名称、评分、上映时间等信息
        for movie in movie_list:
            movie_urls = movie.xpath('./@href')
            if movie_urls:
                movie_info_url = TMDB_BASE_URL + movie_urls[0]
                movie_info = get_movie_info(movie_info_url)
                all_moves.append(movie_info)

    # 4.将电影信息保存到CSV文件中
    save_all_movies(all_moves)


if __name__ == '__main__':
    main()