import requests
import json


def get_info_by_name(name):
    # https://movie.douban.com/j/subject_suggest?q=%E8%82%96%E7%94%B3%E5%85%8B%E7%9A%84%E6%95%91%E8%B5%8E
    url = 'https://movie.douban.com/subject/1292052/?suggest=%E8%82%96%E7%94%B3%E5%85%8B%E7%9A%84%E6%95%91%E8%B5%8E'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.50'}
    r = requests.get(url, headers=header)
    r = json.loads(r)


if __name__ == '__main__':
    get_info_by_name('肖申克的救赎')
