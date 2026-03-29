# Trae IDE Skills Test Project

这是一个用于测试和演示 Trae IDE Skills 功能的项目，主要包含浏览器自动化和网页数据抓取相关功能。

## 项目结构

```
skilltest/
├── .trae/
│   └── skills/
│       └── agent-browser/       # 浏览器自动化 Skill
├── baidu_search.py              # 百度搜索自动化脚本
├── browser_automation.py        # 腾讯新闻抓取脚本
├── scrape_tencent_news.py       # 腾讯新闻爬虫脚本
└── package.json                 # Node.js 依赖配置
```

## 功能模块

### 1. Agent Browser Skill

浏览器自动化 Skill，提供以下功能：

- **页面导航** - 访问 URL、处理重定向、管理多标签页
- **元素交互** - 点击、填写表单、选择下拉框、上传文件
- **数据提取** - 抓取文本、结构化数据、截图、生成 PDF
- **同步等待** - 等待元素出现、网络请求完成

### 2. 百度搜索自动化 (`baidu_search.py`)

使用 Playwright 实现百度搜索自动化：

```bash
python3 baidu_search.py
```

功能：
- 自动打开百度首页
- 输入搜索关键词
- 提取第一条搜索结果

### 3. 腾讯新闻抓取 (`browser_automation.py`)

使用 Playwright 浏览器自动化抓取腾讯新闻：

```bash
python3 browser_automation.py
```

功能：
- 启动无头浏览器
- 访问腾讯网站
- 提取十大新闻标题和链接

### 4. 腾讯新闻爬虫 (`scrape_tencent_news.py`)

使用 BeautifulSoup 快速抓取腾讯新闻：

```bash
python3 scrape_tencent_news.py
```

功能：
- 轻量级 HTTP 请求
- HTML 解析提取新闻
- 去重处理

## 技术栈

- **Python 3.8+**
- **Playwright** - 浏览器自动化
- **BeautifulSoup4** - HTML 解析
- **Requests** - HTTP 请求
- **Node.js 18+** - agent-browser 依赖

## 安装依赖

### Python 依赖

```bash
pip install playwright beautifulsoup4 requests
python3 -m playwright install chromium
```

### Node.js 依赖

```bash
npm install
```

## 使用示例

### 百度搜索

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.baidu.com')
    # ... 更多操作
```

### 网页抓取

```python
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.qq.com')
soup = BeautifulSoup(response.text, 'html.parser')
# ... 提取数据
```

## Skills 说明

### Agent Browser Skill

位置：`.trae/skills/agent-browser/SKILL.md`

这个 Skill 提供了完整的浏览器自动化能力，遵循以下原则：

1. 使用真实浏览器进行自动化操作
2. 支持处理 JavaScript 渲染的动态内容
3. 提供反爬虫绕过机制
4. 支持无头模式和有头模式

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！
