import json

def get_logo(domain):
    return f"https://s2.googleusercontent.com/s2/favicons?domain={domain}&sz=256"

playlist_data = {
    "name": "Mega Playlist 36",
    "groups": [
        {
            "name": "ฟรีทีวีและข่าว",
            "stations": [
                {"name": "ช่อง 3", "url": "https://ch3-web.cdn.byteark.com/live/playlist.m3u8", "domain": "ch3plus.com"},
                {"name": "ช่อง 5", "url": "https://639bc5877c5fe.streamlock.net/tv5hdlive/tv5hdlive/playlist.m3u8", "domain": "tv5hd1.com"},
                {"name": "ช่อง 7", "url": "https://ch7-web.cdn.byteark.com/live/playlist.m3u8", "domain": "ch7.com"},
                {"name": "MCOT HD", "url": "https://mcot-web.cdn.byteark.com/live/playlist.m3u8", "domain": "mcot.net"},
                {"name": "ไทยรัฐ TV", "url": "https://thairath-web.cdn.byteark.com/live/playlist.m3u8", "domain": "thairath.co.th"},
                {"name": "อมรินทร์ TV", "url": "https://amarin-web.cdn.byteark.com/live/playlist.m3u8", "domain": "amarintv.com"},
                {"name": "MONO 29", "url": "https://mono29-web.cdn.byteark.com/live/playlist.m3u8", "domain": "mono29.com"},
                {"name": "WORKPOINT", "url": "https://workpoint-web.cdn.byteark.com/live/playlist.m3u8", "domain": "workpointtv.com"},
                {"name": "PPTV", "url": "https://pptv-web.cdn.byteark.com/live/playlist.m3u8", "domain": "pptvhd36.com"},
                {"name": "TNN16", "url": "https://tnn16-web.cdn.byteark.com/live/playlist.m3u8", "domain": "tnnthailand.com"},
                {"name": "Nation TV", "url": "https://nation-web.cdn.byteark.com/live/playlist.m3u8", "domain": "nationtv.tv"}
            ]
        },
        {
            "name": "กีฬาและฟุตบอล",
            "stations": [
                {"name": "beIN Sports 1", "url": "https://dij0k9i5q0gvn.cloudfront.net/bein1/chunks.m3u8", "domain": "beinsports.com"},
                {"name": "beIN Sports 2", "url": "https://dij0k9i5q0gvn.cloudfront.net/bein2/chunks.m3u8", "domain": "beinsports.com"},
                {"name": "beIN Sports 3", "url": "https://dij0k9i5q0gvn.cloudfront.net/bein3/chunks.m3u8", "domain": "beinsports.com"},
                {"name": "True Sport 2", "url": "https://dij0k9i5q0gvn.cloudfront.net/tsp2/chunks.m3u8", "domain": "truevisions.co.th"},
                {"name": "Premier Football 1", "url": "https://dij0k9i5q0gvn.cloudfront.net/tpf1/chunks.m3u8", "domain": "trueid.net"},
                {"name": "SPOTV 1", "url": "https://dij0k9i5q0gvn.cloudfront.net/spotv/chunks.m3u8", "domain": "spotv.net"}
            ]
        },
        {
            "name": "ภาพยนตร์และสารคดี",
            "stations": [
                {"name": "Animal Show", "url": "https://dij0k9i5q0gvn.cloudfront.net/animalshow/chunks.m3u8", "domain": "animalplanet.com"},
                {"name": "สำรวจโลก", "url": "https://dij0k9i5q0gvn.cloudfront.net/samrujlok/chunks.m3u8", "domain": "nextstep.tv"},
                {"name": "History Channel", "url": "https://dij0k9i5q0gvn.cloudfront.net/history/chunks.m3u8", "domain": "history.com"},
                {"name": "Discovery Channel", "url": "https://dij0k9i5q0gvn.cloudfront.net/discovery/chunks.m3u8", "domain": "discovery.com"},
                {"name": "National Geographic", "url": "https://dij0k9i5q0gvn.cloudfront.net/nat-geo/chunks.m3u8", "domain": "nationalgeographic.com"},
                {"name": "HBO", "url": "https://dij0k9i5q0gvn.cloudfront.net/hbo/chunks.m3u8", "domain": "hbo.com"},
                {"name": "HBO Hits", "url": "https://dij0k9i5q0gvn.cloudfront.net/hbo-hits/chunks.m3u8", "domain": "hbo.com"},
                {"name": "Cinemax", "url": "https://dij0k9i5q0gvn.cloudfront.net/cinemax/chunks.m3u8", "domain": "cinemax.com"},
                {"name": "Rock Entertainment", "url": "https://dij0k9i5q0gvn.cloudfront.net/rock-ent/chunks.m3u8", "domain": "rockentertainment.com"},
                {"name": "Warner TV", "url": "https://dij0k9i5q0gvn.cloudfront.net/warner-tv/chunks.m3u8", "domain": "warnertvasia.com"},
                {"name": "AXN", "url": "https://dij0k9i5q0gvn.cloudfront.net/axn/chunks.m3u8", "domain": "axn-asia.com"},
                {"name": "tvN Asia", "url": "https://dij0k9i5q0gvn.cloudfront.net/tvn-asia/chunks.m3u8", "domain": "tvnasia.net"},
                {"name": "Lifetime", "url": "https://dij0k9i5q0gvn.cloudfront.net/lifetime/chunks.m3u8", "domain": "mylifetime.com"}
            ]
        },
        {
            "name": "การ์ตูนและเด็ก",
            "stations": [
                {"name": "Cartoon Network", "url": "https://dij0k9i5q0gvn.cloudfront.net/cartoon-network/chunks.m3u8", "domain": "cartoonnetworkasia.com"},
                {"name": "Nickelodeon", "url": "https://dij0k9i5q0gvn.cloudfront.net/nickelodeon/chunks.m3u8", "domain": "nick.com"},
                {"name": "Nick Jr", "url": "https://dij0k9i5q0gvn.cloudfront.net/nickjr/chunks.m3u8", "domain": "nickjr.com"},
                {"name": "DreamWorks", "url": "https://dij0k9i5q0gvn.cloudfront.net/dreamworks/chunks.m3u8", "domain": "dreamworks.com"},
                {"name": "Boomerang", "url": "https://dij0k9i5q0gvn.cloudfront.net/boomerang/chunks.m3u8", "domain": "boomerangtv.co.th"}
            ]
        }
    ]
}

# สร้างไฟล์ M3U 
m3u_lines = ["#EXTM3U"]
for group in playlist_data["groups"]:
    for st in group["stations"]:
        logo = get_logo(st["domain"])
        # ใส่ชื่อหมวดหมู่ที่ไม่มี dookeela นำหน้า
        m3u_lines.append(f'#EXTINF:-1 tvg-id="{st["name"]}" tvg-name="{st["name"]}" tvg-logo="{logo}" group-title="{group["name"]}",{st["name"]}')
        m3u_lines.append(st["url"])

with open('playlist.m3u', 'w', encoding='utf-8') as f:
    f.write("\n".join(m3u_lines))

print("สร้างไฟล์ playlist.m3u สำเร็จ (แก้ไขลิงก์และชื่อหมวดหมู่เรียบร้อย)")
