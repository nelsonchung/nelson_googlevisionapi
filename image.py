import io
from google.cloud import vision

# 建立 Vision API 客戶端
client = vision.ImageAnnotatorClient()

# 讀取圖片
with io.open("IMG_8895.JPG", "rb") as image_file:
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

