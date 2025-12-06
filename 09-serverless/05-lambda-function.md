# Serverless with Lambda AWS

## Create lambda function, lambda_function.py
```
# load onnx
session = ort.InferenceSession("hair_classifier_empty.onnx", providers=["CPUExecutionProvider"])

def preprocess_image(img):
    # resize and normalize
    img = img.resize((IMAGE_SIZE, IMAGE_SIZE))
    img = np.array(img).astype(np.float32)  # HWC
    img = img / 255.0
    mean = np.array([0.485, 0.456, 0.406]).reshape(1, 1, 3)
    std = np.array([0.229, 0.224, 0.225]).reshape(1, 1, 3)
    img = (img - mean) / std
    img = img.transpose(2, 0, 1)  # CHW
    img = np.expand_dims(img, axis=0)  # NCHW
    return img.astype(np.float32)

def predict_from_b64(image_base64):
    # convert from base64 to image
    img_bytes = base64.b64decode(image_base64)
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB")

    x = preprocess_image(img)
    ort_inputs = {session.get_inputs()[0].name: x}
    ort_outs = session.run(None, ort_inputs)
    logit = ort_outs[0][0][0].round(2)
    return {"logit": float(logit)}

def lambda_handler(event, context):
    # get json body
    body = json.loads(event["body"]) if "body" in event else event
    img_b64 = body["image"]  # input image in base64 format

    # call prediction function
    result = predict_from_b64(img_b64)

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }
```


