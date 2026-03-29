#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import time

def get_tencent_news():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    
    url = 'https://www.qq.com/'
    
    try:
        print(f"正在访问腾讯网站: {url}")
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        
        if response.status_code != 200:
            print(f"访问失败，状态码: {response.status_code}")
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        news_list = []
        
        news_items = soup.find_all(['a', 'h2', 'h3'], limit=100)
        
        seen_titles = set()
        
        for item in news_items:
            title = item.get_text(strip=True)
            href = item.get('href', '')
            
            if len(title) > 10 and title not in seen_titles:
                if href and (href.startswith('http') or href.startswith('//')):
                    if href.startswith('//'):
                        href = 'https:' + href
                    
                    seen_titles.add(title)
                    news_list.append({
                        'title': title,
                        'url': href
                    })
                    
                    if len(news_list) >= 10:
                        break
        
        return news_list
        
    except Exception as e:
        print(f"发生错误: {str(e)}")
        return []

if __name__ == '__main__':
    print("=" * 60)
    print("腾讯网站十大新闻")
    print("=" * 60)
    print()
    
    news = get_tencent_news()
    
    if news:
        for i, item in enumerate(news, 1):
            print(f"{i}. {item['title']}")
            print(f"   链接: {item['url']}")
            print()
    else:
        print("未能获取到新闻数据")
    
    print("=" * 60)
