#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用 Playwright 浏览器自动化：百度搜索
"""

from playwright.sync_api import sync_playwright
import time

def baidu_search():
    print("=" * 70)
    print("使用 Playwright 浏览器自动化进行百度搜索")
    print("=" * 70)
    print()
    
    with sync_playwright() as p:
        print("正在启动浏览器...")
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        page = context.new_page()
        
        try:
            print("正在打开百度首页...")
            page.goto('https://www.baidu.com', timeout=30000)
            
            print("等待页面加载...")
            time.sleep(2)
            
            print("正在输入搜索内容: Trae IDE")
            page.evaluate('''() => {
                const input = document.querySelector('input[name="wd"]') || document.querySelector('#kw');
                if (input) {
                    input.value = 'Trae IDE';
                    input.dispatchEvent(new Event('input', { bubbles: true }));
                }
            }''')
            
            print("正在提交搜索...")
            page.evaluate('''() => {
                const form = document.querySelector('form') || document.querySelector('#form');
                if (form) {
                    form.submit();
                }
            }''')
            
            print("等待搜索结果加载...")
            time.sleep(3)
            
            print("正在提取第一条搜索结果...")
            
            title = page.evaluate('''() => {
                const result = document.querySelector('.result') || document.querySelector('#content_left > div');
                if (result) {
                    const h3 = result.querySelector('h3');
                    if (h3) return h3.textContent.trim();
                    return result.textContent.trim().split('\\n')[0];
                }
                return null;
            }''')
            
            if title:
                print("\n" + "=" * 70)
                print("第一条搜索结果")
                print("=" * 70)
                print(f"\n标题: {title}")
                print()
                return title
            else:
                print("未找到搜索结果")
                page.screenshot(path='/Users/wuchang/trae/skilltest/baidu_debug.png')
                print("已保存截图用于调试")
                return None
                
        except Exception as e:
            print(f"发生错误: {str(e)}")
            import traceback
            traceback.print_exc()
            try:
                page.screenshot(path='/Users/wuchang/trae/skilltest/baidu_error.png')
            except:
                pass
            return None
        finally:
            print("\n正在关闭浏览器...")
            browser.close()

if __name__ == '__main__':
    result = baidu_search()
    if result:
        print(f"\n✅ 搜索完成！第一条结果的标题是: {result}")
