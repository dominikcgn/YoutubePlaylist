#! /usr/bin/python3

banner = r'''
#########################################################################
#      ____            _           _   __  __                           #
#     |  _ \ _ __ ___ (_) ___  ___| |_|  \/  | ___   ___  ___  ___      #
#     | |_) | '__/ _ \| |/ _ \/ __| __| |\/| |/ _ \ / _ \/ __|/ _ \     #
#     |  __/| | | (_) | |  __/ (__| |_| |  | | (_) | (_) \__ \  __/     #
#     |_|   |_|  \___// |\___|\___|\__|_|  |_|\___/ \___/|___/\___|     #
#                   |__/                                                #
#########################################################################
'''

import requests
import os
import sys
import re
import yt_dlp

def grab(url):
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'format': 'best[ext=m3u8]',  # Spezifisch nach m3u8 Format suchen
            'simulate': True,
            'skip_download': True,
            'extract_flat': False,
            'force_generic_extractor': False
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if info.get('url'):
                print(info['url'])
                return
            elif info.get('formats'):
                for f in info['formats']:
                    if f.get('ext') == 'm3u8':
                        print(f['url'])
                        return
                    
    except Exception as e:
        print(f'# Failed to grab {url}: {str(e)}')
        print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')


print('#EXTM3U x-tvg-url="https://github.com/botallen/epg/releases/download/latest/epg.xml"')
print(banner)

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
