#! /usr/bin/python3
import requests
import json

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

def grab(url):
    try:
        video_id = url.split('watch?v=')[1]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        instances = [
            'https://invidious.snopyta.org',
            'https://inv.riverside.rocks',
            'https://invidious.kavin.rocks',
            'https://vid.puffyan.us'
        ]
        
        for instance in instances:
            try:
                api_url = f'{instance}/api/v1/videos/{video_id}'
                response = requests.get(api_url, headers=headers, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if 'adaptiveFormats' in data:
                        for format in data['adaptiveFormats']:
                            if format.get('type', '').startswith('video/mp4'):
                                print(format['url'])
                                return
            except:
                continue
                
        raise Exception("No valid stream URL found")
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
