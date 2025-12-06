# Save Torch model

## Save torch model
To save torch model:
```
torch.save(model.state_dict(), 'model_name.pth')
```

## Load torch model
- To load model
```
model_loaded = CatDogModel()
model_loaded = model_loaded.to(device)

model_loaded.load_state_dict(torch.load('model_name.pth', map_location=device, weights_only=True))
```







