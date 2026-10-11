#!/usr/bin/env python3
"""把 PokeSchool/dist/web/index.html 放進這個 repo，加上「加入主畫面」用的 PWA 設定"""
import pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
src = (HERE.parent / 'PokeSchool' / 'dist' / 'web' / 'index.html').read_text('utf-8')
meta = ('<meta name="description" content="國小一年級 注音・國語・數學・英語 練習（康軒國數・仁愛國小進度）">\n'
        '<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="mobile-web-app-capable" content="yes">\n'
        '<meta name="apple-mobile-web-app-title" content="寶可夢學堂">\n<meta name="theme-color" content="#EEF3F9">\n'
        '<link rel="apple-touch-icon" href="icon-180.png">\n<link rel="icon" href="icon-192.png">\n<link rel="manifest" href="manifest.json">\n')
out = src.replace('<title>寶可夢學堂</title>\n', '<title>寶可夢學堂</title>\n' + meta, 1)
assert out != src
(HERE / 'index.html').write_text(out, 'utf-8')
print('index.html', len(out.encode()) // 1024, 'KB')
