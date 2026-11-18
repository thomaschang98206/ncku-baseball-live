"""把「及時資料處理」內嵌的 DEMO 資料複製進線上觀賽頁。
用法：python -I build_live.py ../realtime/及時資料處理/index.html index.src.html index.html"""
import sys
rt, src, out = sys.argv[1:4]
r = open(rt, encoding='utf-8').read()
a = r.index('<script id="demo-data" type="application/json">') + len('<script id="demo-data" type="application/json">')
b = r.index('</script>', a)
s = open(src, encoding='utf-8').read()
assert s.count('__DEMO_DATA__') == 1
open(out, 'w', encoding='utf-8', newline='').write(s.replace('__DEMO_DATA__', r[a:b]))
print('demo bytes', b - a)
