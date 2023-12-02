import io
import time
from datetime import datetime
from picamera import PiCamera
from google.cloud import vision

# 建立 Vision API 客戶端
client = vision.ImageAnnotatorClient()

# 使用 Pi Camera 擷取圖片
camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
# 等待攝影機的自動調整
time.sleep(2)

# 使用當前的時間作為檔案名稱
file_name = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
camera.capture(file_name)
camera.stop_preview()

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

