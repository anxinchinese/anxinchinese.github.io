# 安心中文跟读材料站

本仓库用于发布「安心中文」的跟读材料，适合日本人自学中文使用。  
使用 GitHub Pages 托管，用户可以直接在网页上边看 PDF 边听 MP3，无需下载。

---

## 📂 目录结构说明

```plaintext
anxinchinese.github.io/
├── index.html                 ← 主页：介绍安心中文、使用方法
├── contents.html              ← 所有课程系列的目录页

├── demo/                      ← 试听或试验用
│   └── lesson01/
│       ├── index.html
│       ├── lesson01.pdf
│       └── lesson01.mp3

├── pinying/                   ← 拼音课系列
│   └── lesson01/
│       ├── index.html
│       ├── lesson01.pdf
│       └── lesson01.mp3

├── trip/                      ← 旅行中文
│   ├── lesson01/
│   │   ├── index.html
│   │   ├── lesson01.pdf
│   │   └── lesson01.mp3
│   └── lesson02/
│       ├── index.html
│       ├── lesson02.pdf
│       └── lesson02.mp3

├── vocabulary/                ← 词汇类
│   └── lesson01/

├── business-scene/            ← 商务场景
│   └── lesson01/

├── news-culture/              ← 文化新闻类
│   └── lesson01/

├── daily-conversation/        ← 日常对话
│   └── lesson01/

├── assets/                    ← 网站统一资源（图片、样式）
│   ├── style.css
│   └── logo.png

└── README.md                  ← 当前说明文件
```

---

## 📁 文件命名约定

- 每课使用独立目录，文件命名为 `index.html`, `lesson01.pdf`, `lesson01.mp3`
- 所有课程页面使用统一结构，便于用户边看边听

---

## 📢 网页Style（CSS版本）更新

   ### ✅ 步骤

   1. 修改样式文件：`asserts/style.css`

   2. 修改完毕后，在项目根目录运行脚本：`python update_css_version.py`

      **脚本功能：**
      - 扫描当前目录及所有子目录下的 `.html` 文件
      - 将所有引用 `asserts/style.css` 的链接（无论有没有 `?v=...`）  
        自动替换成：
     
        ```
        assets/style.css?v=当天日期（例如 20250708）
        ```


   ### 📦 效果
   - 浏览器发现 CSS 链接地址变了，就会重新加载最新样式
   - 应对用户的浏览器缓存问题，保证用户能第一时间看到最新样式


   ### ✅ 小提示
   - 只要 CSS 有更新，就运行一次脚本

---
