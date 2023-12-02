import io
import time
from datetime import datetime
from picamera2 import Picamera2, Preview
from google.cloud import vision


picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(2)
# 使用當前的時間作為檔案名稱
file_name = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
picam2.capture_file(file_name)

# 讀取擷取的圖片
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

# 創建一個圖像對象
image = vision.Image(content=content)

# 呼叫 LABEL_DETECTION 功能
response = client.label_detection(image=image)

# 列印結果
labels = response.label_annotations
print('Labels:')
for label in labels:
    print(label.description)

