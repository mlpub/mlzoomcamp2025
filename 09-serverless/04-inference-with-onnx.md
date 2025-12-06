# Inference with onnx

Inference with onnx can do in CPU or GPU. But each requires a different runtime library.

It cannot install onnxruntime (CPU) and onnxruntime-gpu (GPU) in the same Python environment. If you need both, create separate virtual environments.


Install runtime CPU:
```
pip install onnxruntime
```

Install runtime GPU:
```
pip install onnxruntime-gpu
```

Example inference CPU:
```
import onnxruntime as ort

# resize image, convert to tensor and normalize
inference_transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

def predict_image_onnx(img_path, onnx_model_path, transform):
    # Preprocess image
    img = Image.open(img_path).convert('RGB')
    img = transform(img).unsqueeze(0).cpu().numpy()  # shape: (1, 3, 224, 224)

    # Load ONNX model
    ort_session = ort.InferenceSession(onnx_model_path, providers=['CPUExecutionProvider'])

    # Run inference
    ort_inputs = {ort_session.get_inputs()[0].name: img}
    ort_outs = ort_session.run(None, ort_inputs)
    logits = ort_outs[0][0][0]
    prob = 1 / (1 + np.exp(-logits))
    pred = 1 if prob > 0.5 else 0
    return pred, prob

pred1, prob1 = predict_image_onnx(image_filename1, 'model.onnx', inference_transform)
print(f'Predicted label: {pred1}, Probability: {prob1:.4f}')
```

Example inference GPU:
```
import onnxruntime as ort

# resize image, convert to tensor and normalize
inference_transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

def predict_image_onnx_gpu(img_path, onnx_model_path, transform):
    # Preprocess image
    img = Image.open(img_path).convert('RGB')
    img = transform(img).unsqueeze(0).cpu().numpy()  # shape: (1, 3, 224, 224)

    # Try to use GPU, fallback to CPU if not available
    providers = ['CUDAExecutionProvider', 'CPUExecutionProvider']
    ort_session = ort.InferenceSession(onnx_model_path, providers=providers)

    # Run inference
    ort_inputs = {ort_session.get_inputs()[0].name: img}
    ort_outs = ort_session.run(None, ort_inputs)
    logits = ort_outs[0][0][0]
    prob = 1 / (1 + np.exp(-logits))
    pred = 1 if prob > 0.5 else 0
    return pred, prob

pred1, prob1 = predict_image_onnx_gpu(image_filename1, 'model.onnx', inference_transform)
print(f'Predicted label: {pred1}, Probability: {prob1:.4f}')
```

