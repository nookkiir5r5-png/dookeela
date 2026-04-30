import json

playlist = {
    "name": "Dookeela Ultimate Playlist",
    "author": "AI Assistant",
    "image": "https://raw.githubusercontent.com/nookkiir5r5-png/-1/refs/heads/main/images.jpeg",
    "groups": [
        {
            "name": "dookeela [ฟรีทีวีและข่าว]",
            "stations": [
                {
                    "name": "ช่อง 3",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/ch3/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "ช่อง 5",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/ch5/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "ช่อง 7",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/ch7/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "MCOT HD",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/ch9/chunks.m3u8",
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
                },
                {
                    "name": "อมรินทร์ TV",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/amarin-tv/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "MONO 29",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/mono29/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "WORKPOINT",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/workpoint/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "PPTV",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/pptv/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "TNN16",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/tnn16/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Nation TV",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/nation-tv/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                }
            ]
        },
        {
            "name": "dookeela [กีฬาและฟุตบอล]",
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
                    "name": "beIN Sports 3",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/bein3/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "True Sport 2",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/tsp2/chunks.m3u8",
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
                },
                {
                    "name": "SPOTV 1",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/spotv/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                }
            ]
        },
        {
            "name": "dookeela [ภาพยนตร์และสารคดี]",
            "stations": [
                {
                    "name": "Animal Show",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/animalshow/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "สำรวจโลก",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/samrujlok/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "History Channel",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/history/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Discovery Channel",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/discovery/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "National Geographic",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/nat-geo/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "HBO Asia",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/hbo-asia/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Cinemax",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/cinemax/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                }
            ]
        },
        {
            "name": "dookeela [การ์ตูนและเด็ก]",
            "stations": [
                {
                    "name": "Cartoon Network",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/cartoon-network/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Nickelodeon",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/nickelodeon/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Nick Jr",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/nickjr/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "DreamWorks",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/dreamworks/chunks.m3u8",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Boomerang",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/boomerang/chunks.m3u8",
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
