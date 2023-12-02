from picamera2 import Picamera2, Preview
import time
from datetime import datetime


picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(2)
# 使用當前的時間作為檔案名稱
file_name = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
picam2.capture_file(file_name)