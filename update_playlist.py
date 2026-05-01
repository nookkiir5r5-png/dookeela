import urllib.request
import re

print("กำลังดึงลิงก์ฟรีทีวีไทยจากเซิร์ฟเวอร์เฉพาะของไทย (Akkradet)...")
try:
    # ดึงไฟล์ m3u จากนักพัฒนาคนไทยที่มีการอัปเดต Token อัตโนมัติ
    req = urllib.request.Request("https://akkradet.github.io/IPTV-THAI/FREETV.m3u")
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')
    response = urllib.request.urlopen(req)
    th_m3u_raw = response.read().decode('utf-8').splitlines()
except Exception as e:
    print("ไม่สามารถดึงข้อมูลได้:", e)
    th_m3u_raw = []

m3u_lines = ["#EXTM3U"]

# 1. กรองข้อมูลฟรีทีวีและจัดหมวดหมู่ใหม่เป็น Dookeela
for line in th_m3u_raw:
    if line.startswith("#EXTM3U"):
        continue
    if line.startswith("#EXTINF"):
        # เปลี่ยนหมวดหมู่เดิมให้เป็นของเรา
        if 'group-title=' in line:
            line = re.sub(r'group-title="[^"]+"', 'group-title="dookeela [ฟรีทีวี อัปเดตอัตโนมัติ]"', line)
        else:
            line = line.replace(',', ' group-title="dookeela [ฟรีทีวี อัปเดตอัตโนมัติ]",')
        m3u_lines.append(line)
    elif line.startswith("http"):
        m3u_lines.append(line)

# ==========================================
# 2. เพิ่มช่อง กีฬา หนัง สารคดี และการ์ตูน ของคุณ
# ==========================================
def get_logo(domain):
    return f"https://s2.googleusercontent.com/s2/favicons?domain={domain}&sz=256"

custom_groups = [
    {
        "name": "dookeela [กีฬาและฟุตบอล]",
        "stations": [
            {"name": "beIN Sports 1", "url": "https://dij0k9i5q0gvn.cloudfront.net/bein1/chunks.m3u8", "domain": "beinsports.com"},
            {"name": "beIN Sports 2", "url": "https://dij0k9i5q0gvn.cloudfront.net/bein2/chunks.m3u8", "domain": "beinsports.com"},
            {"name": "beIN Sports 3", "url": "https://dij0k9i5q0gvn.cloudfront.net/bein3/chunks.m3u8", "domain": "beinsports.com"},
            {"name": "True Sport 2", "url": "https://dij0k9i5q0gvn.cloudfront.net/tsp2/chunks.m3u8", "domain": "truevisions.co.th"},
            {"name": "Premier Football 1", "url": "https://dij0k9i5q0gvn.cloudfront.net/tpf1/chunks.m3u8", "domain": "trueid.net"},
            {"name": "SPOTV 1", "url": "https://dij0k9i5q0gvn.cloudfront.net/spotv/chunks.m3u8", "domain": "spotv.net"},
        ]
    },
    {
        "name": "dookeela [ภาพยนตร์และสารคดี]",
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
        "name": "dookeela [การ์ตูนและเด็ก]",
        "stations": [
            {"name": "Cartoon Network", "url": "https://dij0k9i5q0gvn.cloudfront.net/cartoon-network/chunks.m3u8", "domain": "cartoonnetworkasia.com"},
            {"name": "Nickelodeon", "url": "https://dij0k9i5q0gvn.cloudfront.net/nickelodeon/chunks.m3u8", "domain": "nick.com"},
            {"name": "Nick Jr", "url": "https://dij0k9i5q0gvn.cloudfront.net/nickjr/chunks.m3u8", "domain": "nickjr.com"},
            {"name": "DreamWorks", "url": "https://dij0k9i5q0gvn.cloudfront.net/dreamworks/chunks.m3u8", "domain": "dreamworks.com"},
            {"name": "Boomerang", "url": "https://dij0k9i5q0gvn.cloudfront.net/boomerang/chunks.m3u8", "domain": "boomerangtv.co.th"}
        ]
    }
]

for group in custom_groups:
    for st in group["stations"]:
        logo = get_logo(st["domain"])
        m3u_lines.append(f'#EXTINF:-1 tvg-id="{st["name"]}" tvg-name="{st["name"]}" tvg-logo="{logo}" group-title="{group["name"]}",{st["name"]}')
        m3u_lines.append(st["url"])

# ==========================================
# 3. สร้างไฟล์ M3U 
# ==========================================
with open('playlist.m3u', 'w', encoding='utf-8') as f:
    f.write("\n".join(m3u_lines))

print("สร้างไฟล์ playlist.m3u และดึงช่องฟรีทีวีไทยสำเร็จ!")
