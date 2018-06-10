# coding=UTF-8

"""
Created on 5/6/18

@author: 'johnqiao'
"""
import os
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import urllib.parse
import sys

from yangyang_csv import parse_old, parse


def get_path(word, save_dir='audio', ext='.mp3', index=None):
    """文件路径
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    file_path = os.path.join(
        save_dir,
        (('%03d_%s' % (index, word)) if index is not None else word) + ext)
    return file_path


def download(word, file_path, headers=None):
    """保存音频文件
    """
    url = 'http://dict.youdao.com/dictvoice?audio=%s&le=en' % urllib.parse.quote(word)
    # 设置 header
    user_agent = ('Mozilla/5.0 (Windows NT 6.1; rv:9.0) '
                  'Gecko/20100101 Firefox/9.0')

    print(url, file_path)

    if headers is None:
        headers = {'User-Agent': user_agent}
    headers['Referer'] = ('http://dict.youdao.com/search?q=%s&le=ko&keyfrom'
                          '=dict.result' % word)
    # 读取网页内容
    try:
        request = Request(url=url, headers=headers)
        response = urlopen(request)
    except HTTPError as e:
        # Return code error (e.g. 404, 501, ...)
        print('HTTPError: {}'.format(e.code))
    except URLError as e:
        # Not an HTTP-specific error (e.g. connection refused)
        print('URLError: {}'.format(e.reason))
    else:
        file_data = response.read()
        with open(file_path, 'wb') as output:
            # 写入数据，即保存文件
            output.write(file_data)
        return file_path


def main():
    word_dict = parse(9)
    for k, v in word_dict.items():
        for i, w in enumerate(v):
            w = w.lower()
            path = get_path(w, save_dir='audio/%s' % k, index=i)
            if os.path.exists(path):
                continue
            file_path = download(w, path)
            print("success download!")
            print(os.path.realpath(file_path))
            time.sleep(.1)


if __name__ == '__main__':
    main()
