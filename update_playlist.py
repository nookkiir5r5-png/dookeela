import json

# ค่า User-Agent ที่คุณกำหนด
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"

def get_logo(domain):
    return f"https://s2.googleusercontent.com/s2/favicons?domain={domain}&sz=256"

playlist_data = {
    "name": "Mega Playlist 36 (Updated Monomax Backup Links)",
    "groups": [
        {
            "name": "ฟรีทีวีและข่าว",
            "stations": [
                {"name": "ช่อง 3", "url": "https://dij0k9i5q0gvn.cloudfront.net/ch3hd/chunks.m3u8", "domain": "ch3plus.com", "referer": "https://dookeela4.live/"},
                {"name": "ช่อง 5", "url": "https://dij0k9i5q0gvn.cloudfront.net/ch5hd/chunks.m3u8", "domain": "tv5hd1.com", "referer": "https://dookeela4.live/"},
                {"name": "ช่อง 7", "url": "https://dij0k9i5q0gvn.cloudfront.net/ch7hd/chunks.m3u8", "domain": "ch7.com", "referer": "https://dookeela4.live/"},
                {"name": "MCOT HD", "url": "https://dij0k9i5q0gvn.cloudfront.net/mcothd/chunks.m3u8", "domain": "mcot.net", "referer": "https://dookeela4.live/"},
                {"name": "ไทยรัฐ TV", "url": "https://dij0k9i5q0gvn.cloudfront.net/thairathtv/chunks.m3u8", "domain": "thairath.co.th", "referer": "https://dookeela4.live/"},
                {"name": "อมรินทร์ TV", "url": "https://dij0k9i5q0gvn.cloudfront.net/amarintv/chunks.m3u8", "domain": "amarintv.com", "referer": "https://dookeela4.live/"},
                {"name": "MONO 29", "url": "https://dij0k9i5q0gvn.cloudfront.net/mono29/chunks.m3u8", "domain": "mono29.com", "referer": "https://dookeela4.live/"},
                {"name": "WORKPOINT", "url": "https://workpoint-web.cdn.byteark.com/live/playlist.m3u8", "domain": "workpointtv.com", "referer": "https://www.workpointtv.com/"},
                {"name": "PPTV", "url": "https://dij0k9i5q0gvn.cloudfront.net/pptv/chunks.m3u8", "domain": "pptvhd36.com", "referer": "https://dookeela4.live/"},
                {"name": "TNN16", "url": "https://tnn16-web.cdn.byteark.com/live/playlist.m3u8", "domain": "tnnthailand.com", "referer": "https://www.tnnthailand.com/"},
                {"name": "Nation TV", "url": "https://nation-web.cdn.byteark.com/live/playlist.m3u8", "domain": "nationtv.tv", "referer": "https://www.nationtv.tv/"},
                {"name": "One 31", "url": "https://dij0k9i5q0gvn.cloudfront.net/one31/chunks.m3u8", "domain": "one31.net", "referer": "https://dookeela4.live/"},
                {"name": "Thai PBS", "url": "https://dij0k9i5q0gvn.cloudfront.net/thaipbs/chunks.m3u8", "domain": "thaipbs.or.th", "referer": "https://dookeela4.live/"}
            ]
        },
        {
            "name": "ภาพยนตร์และบันเทิง",
            "stations": [
                {"name": "True Film 1", "url": "https://dij0k9i5q0gvn.cloudfront.net/truefilm1/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "True Film 2", "url": "https://dij0k9i5q0gvn.cloudfront.net/truefilm2/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "True Film Asia", "url": "https://dij0k9i5q0gvn.cloudfront.net/truefilmasia/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "True Movie Hits", "url": "https://dij0k9i5q0gvn.cloudfront.net/truemoviehits/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "True Series", "url": "https://dij0k9i5q0gvn.cloudfront.net/trueseries/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "True Thai Film", "url": "https://dij0k9i5q0gvn.cloudfront.net/truethaifilm/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "True X-zyte", "url": "https://dij0k9i5q0gvn.cloudfront.net/truex-zyte/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "HBO", "url": "https://dij0k9i5q0gvn.cloudfront.net/hbo/chunks.m3u8", "domain": "hbo.com", "referer": "https://dookeela4.live/"},
                {"name": "HBO Family", "url": "https://dij0k9i5q0gvn.cloudfront.net/hbo-family/chunks.m3u8", "domain": "hbo.com", "referer": "https://dookeela4.live/"},
                {"name": "HBO Hits", "url": "https://dij0k9i5q0gvn.cloudfront.net/hbo-hits/chunks.m3u8", "domain": "hbo.com", "referer": "https://dookeela4.live/"},
                {"name": "HBO Signature", "url": "https://dij0k9i5q0gvn.cloudfront.net/hbo-signature/chunks.m3u8", "domain": "hbo.com", "referer": "https://dookeela4.live/"},
                {"name": "Cinemax", "url": "https://dij0k9i5q0gvn.cloudfront.net/cinemax/chunks.m3u8", "domain": "cinemax.com", "referer": "https://dookeela4.live/"},
                {"name": "CCM", "url": "https://dij0k9i5q0gvn.cloudfront.net/ccm/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "Warner TV", "url": "https://dij0k9i5q0gvn.cloudfront.net/warnertv/chunks.m3u8", "domain": "warnertv.com", "referer": "https://dookeela4.live/"},
                {"name": "HITS", "url": "https://dij0k9i5q0gvn.cloudfront.net/hits/chunks.m3u8", "domain": "hitstv.com", "referer": "https://dookeela4.live/"},
                {"name": "HITS Movies", "url": "https://dij0k9i5q0gvn.cloudfront.net/hits-movies/chunks.m3u8", "domain": "hitstv.com", "referer": "https://dookeela4.live/"}
            ]
        },
        {
            "name": "กีฬาและฟุตบอล",
            "stations": [
                {"name": "True Sport 1", "url": "https://dij0k9i5q0gvn.cloudfront.net/tsp1/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "True Sport 2", "url": "https://dij0k9i5q0gvn.cloudfront.net/tsp2/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "True Sport 3", "url": "https://dij0k9i5q0gvn.cloudfront.net/tsp3/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "True Sport 4", "url": "https://dij0k9i5q0gvn.cloudfront.net/tsp4/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "True Sport 5", "url": "https://dij0k9i5q0gvn.cloudfront.net/tsp5/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "True Sport 6", "url": "https://dij0k9i5q0gvn.cloudfront.net/tsp6/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "True Sport 7", "url": "https://dij0k9i5q0gvn.cloudfront.net/tsp7/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "TPF 3", "url": "https://dij0k9i5q0gvn.cloudfront.net/tpf3/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "TPF 4", "url": "https://dij0k9i5q0gvn.cloudfront.net/tpf4/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "TPF 5", "url": "https://dij0k9i5q0gvn.cloudfront.net/tpf5/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "beIN Sports 1", "url": "https://dij0k9i5q0gvn.cloudfront.net/bein1/chunks.m3u8", "domain": "beinsports.com", "referer": "https://dookeela4.live/"},
                {"name": "beIN Sports 2", "url": "https://dij0k9i5q0gvn.cloudfront.net/bein2/chunks.m3u8", "domain": "beinsports.com", "referer": "https://dookeela4.live/"},
                {"name": "beIN Sports 3", "url": "https://dij0k9i5q0gvn.cloudfront.net/bein3/chunks.m3u8", "domain": "beinsports.com", "referer": "https://dookeela4.live/"},
                {"name": "beIN Sports 4", "url": "https://dij0k9i5q0gvn.cloudfront.net/bein4/chunks.m3u8", "domain": "beinsports.com", "referer": "https://dookeela4.live/"},
                {"name": "beIN Sports 5", "url": "https://dij0k9i5q0gvn.cloudfront.net/bein5/chunks.m3u8", "domain": "beinsports.com", "referer": "https://dookeela4.live/"},
                {"name": "beIN Sports 6", "url": "https://dij0k9i5q0gvn.cloudfront.net/bein6/chunks.m3u8", "domain": "beinsports.com", "referer": "https://dookeela4.live/"},
                {"name": "beIN Sports 7", "url": "https://dij0k9i5q0gvn.cloudfront.net/bein7/chunks.m3u8", "domain": "beinsports.com", "referer": "https://dookeela4.live/"},
                {"name": "SPOTV 1", "url": "https://dij0k9i5q0gvn.cloudfront.net/spotv/chunks.m3u8", "domain": "spotv.net", "referer": "https://dookeela4.live/"},
                {"name": "SPOTV 2", "url": "https://dij0k9i5q0gvn.cloudfront.net/spotv2/chunks.m3u8", "domain": "spotv.net", "referer": "https://dookeela4.live/"},
                {"name": "True Tennis", "url": "https://dij0k9i5q0gvn.cloudfront.net/truetennis/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "Play Sports 55", "url": "https://dij0k9i5q0gvn.cloudfront.net/playsports55/chunks.m3u8", "domain": "playsports.com", "referer": "https://dookeela4.live/"},
                {"name": "Play Sports 41", "url": "https://dij0k9i5q0gvn.cloudfront.net/playsports41/chunks.m3u8", "domain": "playsports.com", "referer": "https://dookeela4.live/"}
            ]
        },
        {
            "name": "สำรองmonomax",
            "stations": [
                {"name": "สำรองmonomax1", "url": "https://www.livedoomovies.com:4431/Monomax_PL_1HD/playlist.m3u8", "domain": "monomax.me", "referer": "https://dookeela4.live/"},
                {"name": "สำรองmonomax2", "url": "https://www.livedoomovies.com:4431/Monomax_PL_2HD/playlist.m3u8", "domain": "monomax.me", "referer": "https://dookeela4.live/"},
                {"name": "สำรองmonomax3", "url": "https://www.livedoomovies.com:4431/Monomax_PL_3HD/playlist.m3u8", "domain": "monomax.me", "referer": "https://dookeela4.live/"},
                {"name": "สำรองmonomax4", "url": "https://www.livedoomovies.com:4431/Monomax_PL_4HD/playlist.m3u8", "domain": "monomax.me", "referer": "https://dookeela4.live/"},
                {"name": "สำรองmonomax5", "url": "https://www.livedoomovies.com:4431/Monomax_PL_5HD/playlist.m3u8", "domain": "monomax.me", "referer": "https://dookeela4.live/"},
                {"name": "สำรองmonomax6", "url": "https://www.livedoomovies.com:4431/Monomax_PL_6HD/playlist.m3u8", "domain": "monomax.me", "referer": "https://dookeela4.live/"},
                {"name": "สำรองmonomax7", "url": "https://www.livedoomovies.com:4431/Monomax_PL_7HD/playlist.m3u8", "domain": "monomax.me", "referer": "https://dookeela4.live/"},
                {"name": "สำรองmonomax8", "url": "https://www.livedoomovies.com:4431/Monomax_PL_8HD/playlist.m3u8", "domain": "monomax.me", "referer": "https://dookeela4.live/"},
                {"name": "สำรองmonomax9", "url": "https://live-sport-9.monomax.me/c/index-hls.m3u8", "domain": "monomax.me", "referer": "https://dookeela4.live/"},
                {"name": "สำรองmonomax10", "url": "https://live-sport-10.monomax.me/c/index-hls.m3u8", "domain": "monomax.me", "referer": "https://dookeela4.live/"},
                {"name": "สำรองmonomax11", "url": "https://live-sport-11.monomax.me/c/index-hls.m3u8", "domain": "monomax.me", "referer": "https://dookeela4.live/"},
                {"name": "สำรองmonomax12", "url": "https://live-sport-12.monomax.me/c/index-hls.m3u8", "domain": "monomax.me", "referer": "https://dookeela4.live/"}
            ]
        },
        {
            "name": "สารคดีและอื่นๆ",
            "stations": [
                {"name": "BBC Lifestyle", "url": "https://dij0k9i5q0gvn.cloudfront.net/bbc-lifestyle/chunks.m3u8", "domain": "bbclifestyle.com", "referer": "https://dookeela4.live/"},
                {"name": "Animal Show", "url": "https://dij0k9i5q0gvn.cloudfront.net/animalshow/chunks.m3u8", "domain": "animalplanet.com", "referer": "https://dookeela4.live/"},
                {"name": "สำรวจโลก", "url": "https://dij0k9i5q0gvn.cloudfront.net/samrujlok/chunks.m3u8", "domain": "nextstep.tv", "referer": "https://dookeela4.live/"},
                {"name": "History Channel", "url": "https://dij0k9i5q0gvn.cloudfront.net/history/chunks.m3u8", "domain": "history.com", "referer": "https://dookeela4.live/"},
                {"name": "Discovery Channel", "url": "https://dij0k9i5q0gvn.cloudfront.net/discovery/chunks.m3u8", "domain": "discovery.com", "referer": "https://dookeela4.live/"},
                {"name": "National Geographic", "url": "https://dij0k9i5q0gvn.cloudfront.net/national-geographic/chunks.m3u8", "domain": "nationalgeographic.com", "referer": "https://dookeela4.live/"},
                {"name": "BBC Earth", "url": "https://dij0k9i5q0gvn.cloudfront.net/bbc-earth/chunks.m3u8", "domain": "bbcearth.com", "referer": "https://dookeela4.live/"},
                {"name": "Crime + Investigation", "url": "https://dij0k9i5q0gvn.cloudfront.net/crime-investigation/chunks.m3u8", "domain": "crimeandinvestigation.co.uk", "referer": "https://dookeela4.live/"},
                {"name": "DMAX", "url": "https://dij0k9i5q0gvn.cloudfront.net/dmax/chunks.m3u8", "domain": "dmax.de", "referer": "https://dookeela4.live/"},
                {"name": "Discovery Asia", "url": "https://dij0k9i5q0gvn.cloudfront.net/discovery-asia/chunks.m3u8", "domain": "discovery.com", "referer": "https://dookeela4.live/"},
                {"name": "Foodiez Channel", "url": "https://dij0k9i5q0gvn.cloudfront.net/foodiez-channel/chunks.m3u8", "domain": "foodiez.com", "referer": "https://dookeela4.live/"},
                {"name": "Love Nature 4K", "url": "https://dij0k9i5q0gvn.cloudfront.net/lovenature4k/chunks.m3u8", "domain": "lovenature.com", "referer": "https://dookeela4.live/"},
                {"name": "RT Documentary", "url": "https://dij0k9i5q0gvn.cloudfront.net/rt-documentary/chunks.m3u8", "domain": "rtdoc.tv", "referer": "https://dookeela4.live/"},
                {"name": "True Explore Sci", "url": "https://dij0k9i5q0gvn.cloudfront.net/trueexploresci/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"},
                {"name": "True Explore Wild", "url": "https://dij0k9i5q0gvn.cloudfront.net/trueexplorewild/chunks.m3u8", "domain": "truevisions.co.th", "referer": "https://dookeela4.live/"}
            ]
        }
    ]
}

m3u_lines = ["#EXTM3U"]
for group in playlist_data["groups"]:
    for st in group["stations"]:
        logo = get_logo(st["domain"])
        ref = st.get("referer", "")
        current_url = st["url"]
        
        m3u_lines.append(f'#EXTINF:-1 tvg-id="{st["name"]}" tvg-name="{st["name"]}" tvg-logo="{logo}" group-title="{group["name"]}",{st["name"]}')
        m3u_lines.append(f'#EXTVLCOPT:http-user-agent={USER_AGENT}')
        
        if ref:
            m3u_lines.append(f'#EXTVLCOPT:http-referrer={ref}')
            m3u_lines.append(f'#EXTHTTP:{{"referer":"{ref}", "user-agent":"{USER_AGENT}"}}')
            m3u_lines.append(f'{current_url}|Referer={ref}&User-Agent={USER_AGENT}')
        else:
            m3u_lines.append(f'#EXTHTTP:{{"user-agent":"{USER_AGENT}"}}')
            m3u_lines.append(f'{current_url}|User-Agent={USER_AGENT}')

with open('playlist.m3u', 'w', encoding='utf-8') as f:
    f.write("\n".join(m3u_lines))

with open('playlist.json', 'w', encoding='utf-8') as f:
    json.dump(playlist_data, f, ensure_ascii=False, indent=2)

print("อัปเดตเพลย์ลิสต์พร้อมลิงก์สำรอง Monomax ใหม่สำเร็จ")
