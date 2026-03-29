#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用 Playwright 浏览器自动化访问腾讯网站获取十大新闻
"""

from playwright.sync_api import sync_playwright
import time

def get_tencent_news_with_browser():
    print("=" * 60)
    print("使用 Playwright 浏览器自动化获取腾讯新闻")
    print("=" * 60)
    print()
    
    with sync_playwright() as p:
        print("正在启动浏览器...")
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        page = context.new_page()
        
        try:
            print("正在访问腾讯网站: https://www.qq.com/")
            page.goto('https://www.qq.com/', wait_until='networkidle', timeout=30000)
            
            print("等待页面加载完成...")
            time.sleep(2)
            
            print("正在提取新闻标题...")
            
            news_items = page.query_selector_all('a[href*="news.qq.com"]')
            
            news_list = []
            seen_titles = set()
            
            for item in news_items:
                try:
                    title = item.inner_text().strip()
                    href = item.get_attribute('href')
                    
                    if len(title) > 10 and title not in seen_titles and href:
                        if 'news.qq.com' in href or href.startswith('https://'):
                            seen_titles.add(title)
                            news_list.append({
                                'title': title,
                                'url': href
                            })
                            
                            if len(news_list) >= 10:
                                break
                except Exception as e:
                    continue
            
            if not news_list:
                print("使用备用选择器...")
                all_links = page.query_selector_all('a')
                
                for item in all_links:
                    try:
                        title = item.inner_text().strip()
                        href = item.get_attribute('href')
                        
                        if len(title) > 10 and title not in seen_titles and href:
                            if href.startswith('http'):
                                seen_titles.add(title)
                                news_list.append({
                                    'title': title,
                                    'url': href
                                })
                                
                                if len(news_list) >= 10:
                                    break
                    except Exception as e:
                        continue
            
            print("\n" + "=" * 60)
            print("腾讯网站十大新闻")
            print("=" * 60)
            print()
            
            if news_list:
                for i, item in enumerate(news_list, 1):
                    print(f"{i}. {item['title']}")
                    print(f"   链接: {item['url']}")
                    print()
            else:
                print("未能获取到新闻数据")
            
            print("=" * 60)
            
            return news_list
            
        except Exception as e:
            print(f"发生错误: {str(e)}")
            return []
        finally:
            print("\n正在关闭浏览器...")
            browser.close()

if __name__ == '__main__':
    get_tencent_news_with_browser()
