# Inference torch model

1. Recreate the model architecture
```
model_loaded = CatDogModel()
model_loaded = model_loaded.to(device)
```

2. Load the saved state dict
```
model_loaded.load_state_dict(torch.load('model_name.pth', map_location=device))
model_loaded.eval()  # Set to evaluation mode
```

3. Inference function
```
# resize image, convert to tensor and normalize
inference_transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

def predict_image(img_path, model, transform, device):
    img = Image.open(img_path).convert('RGB')
    img = transform(img).unsqueeze(0).to(device)  # Add batch dimension
    with torch.no_grad():
        output = model(img)
        prob = torch.sigmoid(output).item()
        pred = 1 if prob > 0.5 else 0
    return pred, prob
```

4. Run inference
```
pred1, prob1 = predict_image('file1.jpg', model_loaded, inference_transform, device)
print(f'Predicted label: {pred1}, Probability: {prob1:.4f}')
```


