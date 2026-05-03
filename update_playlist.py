import requests
import json

def get_latest_mysci_url():
    try:
        # ฟังก์ชันจำลองการดึงค่าจาก API หรือเว็บไซต์ต้นทางที่คุณใช้งาน
        # ในกรณีนี้ระบบจะทำการตรวจสอบและสร้างลิงก์ที่มี Token ล่าสุดให้
        response = requests.get("https://dookeela4.live/api/get_mysci", timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data["url"], data["referer"]
    except Exception as e:
        print("ไม่สามารถเชื่อมต่อ API ดึงลิงก์อัตโนมัติได้ จะใช้ลิงก์สำรองแทน:", e)
    
    # ลิงก์สำรอง กรณีที่ API หลักไม่ตอบสนอง
    return "https://alpha.footstv.com/dooflix_x1/mysci/chunks.m3u8?nimblesessionid=3013060&wmsAuthSign=c2VydmVyX3RpbWU9MDUvMDMvMjAyNiAwOToyODowOCBBTSZoYXNoX3ZhbHVlPUlOaEcvcVBiOG1sT0RWZ0xtSW82Smc9PSZ2YWxpZG1pbnV0ZXM9NSZzdHJtX2xlbj0xMCZpZD13ZWItMzUyMjYz", "https://dookeela4.live/"

# ตัวอย่างการนำไปใส่ใน playlist_data
new_url, new_referer = get_latest_mysci_url()

# นำไปใส่ในส่วนของ stations
# {"name": "Mysci", "url": new_url, "domain": "footstv.com", "referer": new_referer}
