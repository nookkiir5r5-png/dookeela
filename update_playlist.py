import json

playlist = {
    "name": "Dookeela Clean Playlist",
    "author": "AI Assistant",
    "image": "https://raw.githubusercontent.com/nookkiir5r5-png/-1/refs/heads/main/images.jpeg",
    "groups": [
        {
            "name": "dookeela [ฟรีทีวีและข่าว]",
            "stations": [
                {
                    "name": "ช่อง 3 HD",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/ch3/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "ช่อง 5 HD",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/ch5/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "ช่อง 7 HD",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/ch7/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "ไทยรัฐ TV",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/thairath-tv/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                }
            ]
        },
        {
            "name": "dookeela [กีฬา]",
            "stations": [
                {
                    "name": "beIN Sports 1",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/bein1/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "beIN Sports 2",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/bein2/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Premier Football 1",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/tpf1/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                }
            ]
        }
    ]
}

with open('playlist.json', 'w', encoding='utf-8') as f:
    json.dump(playlist, f, ensure_ascii=False, indent=2)

print("สร้างไฟล์ playlist.json สำเร็จ")
