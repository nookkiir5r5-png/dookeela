import requests
import re
import json

# รายชื่อช่องหลักที่ใช้งานได้จริง
ALL_CHANNELS = {
    "ฟรีทีวีและข่าว": {
        "ช่อง 3 HD": "ch3",
        "ช่อง 5 HD": "ch5",
        "ช่อง 7 HD": "ch7",
        "ไทยรัฐ TV": "thairath-tv",
        "อมรินทร์ TV": "amarin-tv",
        "MONO 29": "mono29"
    },
    "กีฬา [สากลและฟุตบอล]": {
        "beIN Sports 1": "bein1",
        "beIN Sports 2": "bein2",
        "beIN Sports 3": "bein3",
        "True Sport 2": "tsp2",
        "True Sport 7": "tsp7",
        "Premier Football 1": "tpf1",
        "Premier Football 2": "tpf2"
    },
    "การ์ตูนและเด็ก": {
        "Cartoon Network": "cartoon-network",
        "Nickelodeon": "nickelodeon",
        "Boomerang": "boomerang"
    }
}

def get_stream_url(ch_id):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Referer': 'https://dookeela4.live/'
        }
        response = requests.get(f"https://dookeela4.live/live-tv/{ch_id}", headers=headers, timeout=8)
        
        if response.status_code == 200 and "Video unavailable" not in response.text:
            token_match = re.search(r'wmsAuthSign=([^"\'& ]+)', response.text)
            if token_match:
                token = token_match.group(1)
                return f"https://live2.stream.liveplayback.net/dookeela/{ch_id}/chunks.m3u8?wmsAuthSign={token}"
    except:
        pass
    return None

playlist = {
    "name": "Dookeela Clean Playlist",
    "author": "AI Assistant",
    "image": "https://raw.githubusercontent.com/nookkiir5r5-png/-1/refs/heads/main/images.jpeg",
    "groups": []
}

for cat_name, channels in ALL_CHANNELS.items():
    current_group = {"name": f"dookeela [{cat_name}]", "stations": []}
    for name, ch_id in channels.items():
        print(f"กำลังตรวจสอบช่อง: {name}...")
        url = get_stream_url(ch_id)
        if url:
            current_group["stations"].append({
                "name": name,
                "url": url,
                "referer": "https://dookeela4.live/",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "playInNatPlayer": True
            })
    if current_group["stations"]:
        playlist["groups"].append(current_group)

with open('playlist.json', 'w', encoding='utf-8') as f:
    json.dump(playlist, f, ensure_ascii=False, indent=2)

print("สร้างไฟล์สำเร็จ")
