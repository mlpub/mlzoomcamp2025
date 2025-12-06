# POST request to serverless api

1. Load image and convert to base64
```
from PIL import Image
import base64
from io import BytesIO

# Load the image
with Image.open(IMAGE_NAME) as img:
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
```

2. Call api
```
import requests

url = "http://localhost:9100/2015-03-31/functions/function/invocations"
headers = {"Content-Type": "application/json"}
data = json.dumps({"image": img_base64})

response = requests.post(url, headers=headers, data=data)
print(response.status_code)
print(response.json())
``` 