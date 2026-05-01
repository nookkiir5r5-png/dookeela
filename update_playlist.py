import json

def get_logo(domain):
    return f"https://s2.googleusercontent.com/s2/favicons?domain={domain}&sz=256"

playlist_data = {
    "name": "Dookeela Mega Playlist 36 (Updated Links)",
    "author": "AI Assistant",
    "image": "https://raw.githubusercontent.com/nookkiir5r5-png/-1/refs/heads/main/images.jpeg",
    "groups": [
        {
            "name": "dookeela [ฟรีทีวีและข่าว]",
            "stations": [
                {
                    "name": "ช่อง 3",
                    "url": "https://ch3-33-web.cdn.byteark.com/live/playlist.m3u8",
                    "logo": get_logo("ch3plus.com"),
                    "image": get_logo("ch3plus.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "ช่อง 5",
                    "url": "https://639bc5877c5fe.streamlock.net/tv5hdlive/tv5hdlive/playlist.m3u8",
                    "logo": get_logo("tv5hd1.com"),
                    "image": get_logo("tv5hd1.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "ช่อง 7",
                    "url": "http://streaming-hwc.ch7.com/livech7hd/HD_720p.m3u8",
                    "logo": get_logo("ch7.com"),
                    "image": get_logo("ch7.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "MCOT HD",
                    "url": "https://live-org-01-cdn.mcot.net/mcothd1080p_edge/smil:mcothd1080p.smil/playlist.m3u8",
                    "logo": get_logo("mcot.net"),
                    "image": get_logo("mcot.net"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "ไทยรัฐ TV",
                    "url": "https://cdn6.goprimetime.info/feed/202306140918/chthairath3/index.m3u8",
                    "logo": get_logo("thairath.co.th"),
                    "image": get_logo("thairath.co.th"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "อมรินทร์ TV",
                    "url": "https://cdn6.goprimetime.info/feed/202306140918/chamarin/index.m3u8",
                    "logo": get_logo("amarintv.com"),
                    "image": get_logo("amarintv.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "MONO 29",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/mono29/chunks.m3u8",
                    "logo": get_logo("mono29.com"),
                    "image": get_logo("mono29.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "WORKPOINT",
                    "url": "https://cdn6.goprimetime.info/feed/202306140918/chworkpoint3/index.m3u8",
                    "logo": get_logo("workpointtv.com"),
                    "image": get_logo("workpointtv.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "PPTV",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/pptv/chunks.m3u8",
                    "logo": get_logo("pptvhd36.com"),
                    "image": get_logo("pptvhd36.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "TNN16",
                    "url": "https://cdn6.goprimetime.info/feed/202306140918/chtnn3/index.m3u8",
                    "logo": get_logo("tnnthailand.com"),
                    "image": get_logo("tnnthailand.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "Nation TV",
                    "url": "https://cdn6.goprimetime.info/feed/202306140918/chnation3/index.m3u8",
                    "logo": get_logo("nationtv.tv"),
                    "image": get_logo("nationtv.tv"),
                    "userAgent": "Mozilla/5.0",
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
                    "logo": get_logo("beinsports.com"),
                    "image": get_logo("beinsports.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "beIN Sports 2",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/bein2/chunks.m3u8",
                    "logo": get_logo("beinsports.com"),
                    "image": get_logo("beinsports.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "beIN Sports 3",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/bein3/chunks.m3u8",
                    "logo": get_logo("beinsports.com"),
                    "image": get_logo("beinsports.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "beIN Sports 4",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/bein4/chunks.m3u8",
                    "logo": get_logo("beinsports.com"),
                    "image": get_logo("beinsports.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "beIN Sports 5",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/bein5/chunks.m3u8",
                    "logo": get_logo("beinsports.com"),
                    "image": get_logo("beinsports.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "True Sport 1",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/tsp1/chunks.m3u8",
                    "logo": get_logo("truevisions.co.th"),
                    "image": get_logo("truevisions.co.th"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "True Sport 2",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/tsp2/chunks.m3u8",
                    "logo": get_logo("truevisions.co.th"),
                    "image": get_logo("truevisions.co.th"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "True Sport 7",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/tsp7/chunks.m3u8",
                    "logo": get_logo("truevisions.co.th"),
                    "image": get_logo("truevisions.co.th"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "Premier Football 1",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/tpf1/chunks.m3u8",
                    "logo": get_logo("trueid.net"),
                    "image": get_logo("trueid.net"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "Premier Football 2",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/tpf2/chunks.m3u8",
                    "logo": get_logo("trueid.net"),
                    "image": get_logo("trueid.net"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "SPOTV 1",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/spotv/chunks.m3u8",
                    "logo": get_logo("spotv.net"),
                    "image": get_logo("spotv.net"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "SPOTV 2",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/spotv2/chunks.m3u8",
                    "logo": get_logo("spotv.net"),
                    "image": get_logo("spotv.net"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "MUTV",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/mutv/chunks.m3u8",
                    "logo": get_logo("manutd.com"),
                    "image": get_logo("manutd.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "Golf Channel",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/golf-channel/chunks.m3u8",
                    "logo": get_logo("golfchannel.co.th"),
                    "image": get_logo("golfchannel.co.th"),
                    "userAgent": "Mozilla/5.0",
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
                    "logo": get_logo("animalplanet.com"),
                    "image": get_logo("animalplanet.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "สำรวจโลก",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/samrujlok/chunks.m3u8",
                    "logo": get_logo("nextstep.tv"),
                    "image": get_logo("nextstep.tv"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "History Channel",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/history/chunks.m3u8",
                    "logo": get_logo("history.com"),
                    "image": get_logo("history.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "Discovery Channel",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/discovery/chunks.m3u8",
                    "logo": get_logo("discovery.com"),
                    "image": get_logo("discovery.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "Discovery Asia",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/discovery-asia/chunks.m3u8",
                    "logo": get_logo("discovery.com"),
                    "image": get_logo("discovery.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "National Geographic",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/nat-geo/chunks.m3u8",
                    "logo": get_logo("nationalgeographic.com"),
                    "image": get_logo("nationalgeographic.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "Crime + Investigation",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/crime-investigation/chunks.m3u8",
                    "logo": get_logo("crimeandinvestigation.co.uk"),
                    "image": get_logo("crimeandinvestigation.co.uk"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "HBO",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/hbo/chunks.m3u8",
                    "logo": get_logo("hbo.com"),
                    "image": get_logo("hbo.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "HBO Family",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/hbo-family/chunks.m3u8",
                    "logo": get_logo("hbo.com"),
                    "image": get_logo("hbo.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "HBO Hits",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/hbo-hits/chunks.m3u8",
                    "logo": get_logo("hbo.com"),
                    "image": get_logo("hbo.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "HBO Signature",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/hbo-signature/chunks.m3u8",
                    "logo": get_logo("hbo.com"),
                    "image": get_logo("hbo.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "Cinemax",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/cinemax/chunks.m3u8",
                    "logo": get_logo("cinemax.com"),
                    "image": get_logo("cinemax.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "Fashion TV",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/fashion-tv/chunks.m3u8",
                    "logo": get_logo("fashiontv.com"),
                    "image": get_logo("fashiontv.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "Rock Entertainment",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/rock-ent/chunks.m3u8",
                    "logo": get_logo("rockentertainment.com"),
                    "image": get_logo("rockentertainment.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "Rock Action",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/rock-action/chunks.m3u8",
                    "logo": get_logo("rockentertainment.com"),
                    "image": get_logo("rockentertainment.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "True Asian More",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/true-asian-more/chunks.m3u8",
                    "logo": get_logo("truevisions.co.th"),
                    "image": get_logo("truevisions.co.th"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "Warner TV",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/warner-tv/chunks.m3u8",
                    "logo": get_logo("warnertvasia.com"),
                    "image": get_logo("warnertvasia.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "AXN",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/axn/chunks.m3u8",
                    "logo": get_logo("axn-asia.com"),
                    "image": get_logo("axn-asia.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "tvN Asia",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/tvn-asia/chunks.m3u8",
                    "logo": get_logo("tvnasia.net"),
                    "image": get_logo("tvnasia.net"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "Lifetime",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/lifetime/chunks.m3u8",
                    "logo": get_logo("mylifetime.com"),
                    "image": get_logo("mylifetime.com"),
                    "userAgent": "Mozilla/5.0",
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
                    "logo": get_logo("cartoonnetworkasia.com"),
                    "image": get_logo("cartoonnetworkasia.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "Nickelodeon",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/nickelodeon/chunks.m3u8",
                    "logo": get_logo("nick.com"),
                    "image": get_logo("nick.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "Nick Jr",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/nickjr/chunks.m3u8",
                    "logo": get_logo("nickjr.com"),
                    "image": get_logo("nickjr.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "DreamWorks",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/dreamworks/chunks.m3u8",
                    "logo": get_logo("dreamworks.com"),
                    "image": get_logo("dreamworks.com"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                },
                {
                    "name": "Boomerang",
                    "url": "https://dij0k9i5q0gvn.cloudfront.net/boomerang/chunks.m3u8",
                    "logo": get_logo("boomerangtv.co.th"),
                    "image": get_logo("boomerangtv.co.th"),
                    "userAgent": "Mozilla/5.0",
                    "playInNatPlayer": True
                }
            ]
        }
    ]
}

with open('playlist.json', 'w', encoding='utf-8') as f:
    json.dump(playlist_data, f, ensure_ascii=False, indent=2)

m3u_lines = ["#EXTM3U"]
for group in playlist_data["groups"]:
    for station in group["stations"]:
        logo_url = station.get("logo", "")
        m3u_lines.append(f'#EXTINF:-1 tvg-id="{station["name"]}" tvg-name="{station["name"]}" tvg-logo="{logo_url}" group-title="{group["name"]}",{station["name"]}')
        m3u_lines.append(station["url"])

with open('playlist.m3u', 'w', encoding='utf-8') as f:
    f.write("\n".join(m3u_lines))

print("สร้างไฟล์ playlist.json และ playlist.m3u สำเร็จ")
