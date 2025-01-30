#! /usr/bin/python3
import streamlink
import requests
import os
import sys

def grab(url):
    try:
        streams = streamlink.streams(url)
        if streams:
            best_stream = streams['best']
            print(best_stream.url)
            return
    except Exception as e:
        print(f'# Failed to grab {url}: {str(e)}')
        print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')

print('#EXTM3U x-tvg-url="https://github.com/botallen/epg/releases/download/latest/epg.xml"')

with open('../youtube_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if '|' in line:
            parts = line.split('|')
            ch_name = parts[0].strip()
            url = parts[1].strip()
            print(f'\n#EXTINF:-1 group-title="Thailand", {ch_name}')
            grab(url)
