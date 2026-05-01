import json

def get_logo(domain):
    return f"https://s2.googleusercontent.com/s2/favicons?domain={domain}&sz=256"

playlist_data = {
    "name": "Mega Playlist 36 (Referer Unlocked)",
    "groups": [
        {
            "name": "ฟรีทีวีและข่าว",
            "stations": [
                {"name": "ช่อง 3", "url": "https://ch3-33-web.cdn.byteark.com/live/playlist.m3u8", "domain": "ch3plus.com", "referer": "https://ch3plus.com/"},
                {"name": "ช่อง 5", "url": "https://639bc5877c5fe.streamlock.net/tv5hdlive/tv5hdlive/playlist.m3u8", "domain": "tv5hd1.com", "referer": ""},
                {"name": "ช่อง 7", "url": "http://streaming-hwc.ch7.com/livech7hd/HD_720p.m3u8", "domain": "ch7.com", "referer": "https://www.ch7.com/"},
                {"name": "MCOT HD", "url": "https://live-org-01-cdn.mcot.net/mcothd1080p_edge/smil:mcothd1080p.smil/playlist.m3u8", "domain": "mcot.net", "referer": "https://mcot.net/"},
                {"name": "ไทยรัฐ TV", "url": "https://thairath-web.cdn.byteark.com/live/playlist.m3u8", "domain": "thairath.co.th", "referer": "https://www.thairath.co.th/"},
                {"name": "อมรินทร์ TV", "url": "https://amarin-web.cdn.byteark.com/live/playlist.m3u8", "domain": "amarintv.com", "referer": "https://www.amarintv.com/"},
                {"name": "MONO 29", "url": "https://dij0k9i5q0gvn.cloudfront.net/mono29/chunks.m3u8", "domain": "mono29.com", "referer": "https://dookeela4.live/"},
                {"name": "WORKPOINT", "url": "https://workpoint-web.cdn.byteark.com/live/playlist.m3u8", "domain": "workpointtv.com", "referer": "https://www.workpointtv.com/"},
                {"name": "PPTV", "url": "https://dij0k9i5q0gvn.cloudfront.net/pptv/chunks.m3u8", "domain": "pptvhd36.com", "referer": "https://dookeela4.live/"},
                {"name": "TNN16", "url": "https://tnn16-web.cdn.byteark.com/live/playlist.m3u8", "domain": "tnnthailand.com", "referer": "https://www.tnnthailand.com/"},
                {"name": "Nation TV", "url": "https://nation-web.cdn.byteark.com/live/playlist.m3u8", "domain": "nationtv.tv", "referer": "https://www.nationtv.tv/"}
            ]
        },
        {
            "name": "กีฬาและฟุตบอล",
            "stations": [
                {"name": "beIN Sports 1", "url": "https://dij0k9i5q0gvn.cloudfront.net/bein1/chunks.m3u8", "domain": "beinsports.com", "referer": "https://dookeela4.live/"},
                {"name": "beIN Sports 2", "url": "https://dij0k9i5q0gvn.cloudfront.net/bein2/chunks.m3u8", "domain": "beinsports.com", "referer": "https://dookeela4.live/"},
                {"name": "beIN Sports 3", "url": "https://dij0k9i5q0gvn.cloudfront.net/bein3/chunks.m3u8", "domain": "beinsports.com", "referer": "https://dookeela4.live/"},
                {"name": "True Sport 2", "url": "https://dij0k9i5q0gvn.cloudfront.net/tsp2/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "Premier Football 1", "url": "https://dij0k9i5q0gvn.cloudfront.net/tpf1/chunks.m3u8", "domain": "trueid.net", "referer": "https://dookeela4.live/"},
                {"name": "SPOTV 1", "url": "https://dij0k9i5q0gvn.cloudfront.net/spotv/chunks.m3u8", "domain": "spotv.net", "referer": "https://dookeela4.live/"}
            ]
        },
        {
            "name": "ภาพยนตร์และสารคดี",
            "stations": [
                {"name": "Animal Show", "url": "https://dij0k9i5q0gvn.cloudfront.net/animalshow/chunks.m3u8", "domain": "animalplanet.com", "referer": "https://dookeela4.live/"},
                {"name": "สำรวจโลก", "url": "https://dij0k9i5q0gvn.cloudfront.net/samrujlok/chunks.m3u8", "domain": "nextstep.tv", "referer": "https://dookeela4.live/"},
                {"name": "History Channel", "url": "https://dij0k9i5q0gvn.cloudfront.net/history/chunks.m3u8", "domain": "history.com", "referer": "https://dookeela4.live/"},
                {"name": "Discovery Channel", "url": "https://dij0k9i5q0gvn.cloudfront.net/discovery/chunks.m3u8", "domain": "discovery.com", "referer": "https://dookeela4.live/"},
                {"name": "National Geographic", "url": "https://dij0k9i5q0gvn.cloudfront.net/nat-geo/chunks.m3u8", "domain": "nationalgeographic.com", "referer": "https://dookeela4.live/"},
                {"name": "HBO", "url": "https://dij0k9i5q0gvn.cloudfront.net/hbo/chunks.m3u8", "domain": "hbo.com", "referer": "https://dookeela4.live/"},
                {"name": "HBO Hits", "url": "https://dij0k9i5q0gvn.cloudfront.net/hbo-hits/chunks.m3u8", "domain": "hbo.com", "referer": "https://dookeela4.live/"},
                {"name": "Cinemax", "url": "https://dij0k9i5q0gvn.cloudfront.net/cinemax/chunks.m3u8", "domain": "cinemax.com", "referer": "https://dookeela4.live/"},
                {"name": "Rock Entertainment", "url": "https://dij0k9i5q0gvn.cloudfront.net/rock-ent/chunks.m3u8", "domain": "rockentertainment.com", "referer": "https://dookeela4.live/"},
                {"name": "Warner TV", "url": "https://dij0k9i5q0gvn.cloudfront.net/warner-tv/chunks.m3u8", "domain": "warnertvasia.com", "referer": "https://dookeela4.live/"},
                {"name": "AXN", "url": "https://dij0k9i5q0gvn.cloudfront.net/axn/chunks.m3u8", "domain": "axn-asia.com", "referer": "https://dookeela4.live/"},
                {"name": "tvN Asia", "url": "https://dij0k9i5q0gvn.cloudfront.net/tvn-asia/chunks.m3u8", "domain": "tvnasia.net", "referer": "https://dookeela4.live/"},
                {"name": "Lifetime", "url": "https://dij0k9i5q0gvn.cloudfront.net/lifetime/chunks.m3u8", "domain": "mylifetime.com", "referer": "https://dookeela4.live/"}
            ]
        },
        {
            "name": "การ์ตูนและเด็ก",
            "stations": [
                {"name": "Cartoon Network", "url": "https://dij0k9i5q0gvn.cloudfront.net/cartoon-network/chunks.m3u8", "domain": "cartoonnetworkasia.com", "referer": "https://dookeela4.live/"},
                {"name": "Nickelodeon", "url": "https://dij0k9i5q0gvn.cloudfront.net/nickelodeon/chunks.m3u8", "domain": "nick.com", "referer": "https://dookeela4.live/"},
                {"name": "Nick Jr", "url": "https://dij0k9i5q0gvn.cloudfront.net/nickjr/chunks.m3u8", "domain": "nickjr.com", "referer": "https://dookeela4.live/"},
                {"name": "DreamWorks", "url": "https://dij0k9i5q0gvn.cloudfront.net/dreamworks/chunks.m3u8", "domain": "dreamworks.com", "referer": "https://dookeela4.live/"},
                {"name": "Boomerang", "url": "https://dij0k9i5q0gvn.cloudfront.net/boomerang/chunks.m3u8", "domain": "boomerangtv.co.th", "referer": "https://dookeela4.live/"}
            ]
        }
    ]
}

# สร้างไฟล์ M3U แบบบังคับแนบ Referer
m3u_lines = ["#EXTM3U"]
for group in playlist_data["groups"]:
    for st in group["stations"]:
        logo = get_logo(st["domain"])
        ref = st.get("referer", "")
        
        m3u_lines.append(f'#EXTINF:-1 tvg-id="{st["name"]}" tvg-name="{st["name"]}" tvg-logo="{logo}" group-title="{group["name"]}",{st["name"]}')
        
        if ref:
            # ฝัง Referer ลงไป 3 แบบครอบคลุมเครื่องเล่นทุกชนิด
            m3u_lines.append(f'#EXTVLCOPT:http-referrer={ref}')
            m3u_lines.append(f'#EXTHTTP:{{"referer":"{ref}"}}')
            m3u_lines.append(f'{st["url"]}|Referer={ref}')
        else:
            m3u_lines.append(st["url"])

with open('playlist.m3u', 'w', encoding='utf-8') as f:
    f.write("\n".join(m3u_lines))

print("สร้างไฟล์ playlist.m3u พร้อมระบบทะลุบล็อก Referer สำเร็จ!")
