#!/usr/bin/env python3
"""Generate index.html from days.json. status: live (needs url) | tomorrow | soon."""
import json, html
days = json.load(open('days.json', encoding='utf-8'))
ar = lambda n: str(n).translate(str.maketrans('0123456789', '٠١٢٣٤٥٦٧٨٩'))
label = {'live': 'متاح الآن', 'tomorrow': 'بكرة', 'soon': 'قريبًا'}
cards = ''
for d in days:
    st = d['status']
    if st == 'live' and d.get('url'):
        btn = f'<a class="btn" href="{html.escape(d["url"])}" target="_blank" rel="noopener">شوف الريل</a>'
    else:
        btn = '<span class="btn off">قريبًا</span>'
    note = f'<div class="note">{html.escape(d["note"])}</div>' if d.get('note') else ''
    cards += f'''<li class="item {st}"><div class="num">{ar(d["day"])}</div><div class="info"><div class="day">اليوم {ar(d["day"])} <span class="tag {st}">{label[st]}</span></div><div class="rng">{html.escape(d["range"])}</div>{note}</div>{btn}</li>\n'''
page = open('template.html', encoding='utf-8').read().replace('{{CARDS}}', cards)
open('index.html', 'w', encoding='utf-8').write(page)
print('built', len(days), 'days')
