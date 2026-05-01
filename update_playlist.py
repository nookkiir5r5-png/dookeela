import json

playlist_data = {
    "name": "Dookeela Mega Playlist with Logos",
    "author": "AI Assistant",
    "image": "https://raw.githubusercontent.com/nookkiir5r5-png/-1/refs/heads/main/images.jpeg",
    "groups": [
        {
            "name": "dookeela [ฟรีทีวีและข่าว]",
            "stations": [
                {
                    "name": "ช่อง 3",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/ch3/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Channel_3_Thailand_logo.svg/120px-Channel_3_Thailand_logo.svg.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "ช่อง 5",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/ch5/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/e/eb/TV5HD1_logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "ช่อง 7",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/ch7/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/b/ba/Ch7HD_logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "MCOT HD",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/ch9/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/0/07/MCOT_HD_Logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "ไทยรัฐ TV",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/thairath-tv/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Thairath_TV_logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "อมรินทร์ TV",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/amarin-tv/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/1/15/Amarin_TV_logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "MONO 29",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/mono29/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/1/10/Mono29_logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "WORKPOINT",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/workpoint/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Workpoint_TV_logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "PPTV",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/pptv/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/1/1f/PPTV_HD_36_Logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "TNN16",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/tnn16/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/6/69/TNN16_logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Nation TV",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/nation-tv/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/3/36/Nation_TV_logo.png",
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
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a3/BeIN_Sports_logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "beIN Sports 2",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/bein2/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a3/BeIN_Sports_logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "beIN Sports 3",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/bein3/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a3/BeIN_Sports_logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "True Sport 2",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/tsp2/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/6/66/Truevisions-logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Premier Football 1",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/tpf1/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/6/66/Truevisions-logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "SPOTV 1",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/spotv/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/3/30/SPOTV_logo.png",
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
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/3/3b/Animal_Planet_logo.svg",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "สำรวจโลก",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/samrujlok/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Thairath_TV_logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "History Channel",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/history/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/6/64/The_History_Channel_%282008%29.svg",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Discovery Channel",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/discovery/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/b/ba/Discovery_Channel_2009_logo.svg",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Discovery Asia",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/discovery-asia/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/b/ba/Discovery_Channel_2009_logo.svg",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "National Geographic",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/nat-geo/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/c/cc/National_Geographic_logo.svg",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Crime + Investigation",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/crime-investigation/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/6/66/Truevisions-logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "HBO",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/hbo/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/b/b5/HBO_logo.svg",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "HBO Family",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/hbo-family/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/b/b5/HBO_logo.svg",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "HBO Hits",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/hbo-hits/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/b/b5/HBO_logo.svg",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "HBO Signature",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/hbo-signature/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/b/b5/HBO_logo.svg",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Cinemax",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/cinemax/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/b/b5/HBO_logo.svg",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Fashion TV",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/fashion-tv/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/b/b4/FashionTV_new_logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Rock Entertainment",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/rock-ent/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/6/66/Truevisions-logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Rock Action",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/rock-action/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/6/66/Truevisions-logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "True Asian More",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/true-asian-more/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/6/66/Truevisions-logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Warner TV",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/warner-tv/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/3/34/Warner_TV_logo.svg",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "AXN",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/axn/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/5/5e/AXN_logo.svg",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "tvN Asia",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/tvn-asia/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/1/1b/TvN_Asia_logo.png",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Lifetime",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/lifetime/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/5/56/Lifetime_logo.png",
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
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/8/89/Cartoon_Network_logo_2010.svg",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Nickelodeon",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/nickelodeon/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/9/94/Nickelodeon_2023_logo.svg",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Nick Jr",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/nickjr/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/6/6c/Nick_Jr._2009_logo.svg",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "DreamWorks",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/dreamworks/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/0/07/DreamWorks_Animation_logo.svg",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                },
                {
                    "name": "Boomerang",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/boomerang/chunks.m3u8",
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/2/22/Boomerang_logo_%282012%29.svg",
                    "referer": "https://dookeela4.live/",
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "playInNatPlayer": True
                }
            ]
        }
    ]
}

# สร้างไฟล์ playlist.json
with open('playlist.json', 'w', encoding='utf-8') as f:
    json.dump(playlist_data, f, ensure_ascii=False, indent=2)

# สร้างไฟล์ playlist.m3u ที่มีโลโก้
m3u_lines = ["#EXTM3U"]
for group in playlist_data["groups"]:
    for station in group["stations"]:
        logo_url = station.get("logo", "")
        m3u_lines.append(f'#EXTINF:-1 tvg-id="{station["name"]}" tvg-name="{station["name"]}" tvg-logo="{logo_url}" group-title="{group["name"]}",{station["name"]}')
        m3u_lines.append(station["url"])

with open('playlist.m3u', 'w', encoding='utf-8') as f:
    f.write("\n".join(m3u_lines))

print("สร้างไฟล์ playlist.json และ playlist.m3u สำเร็จ")
