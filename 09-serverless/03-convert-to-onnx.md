# Convert torch model to onnx

1. Install onnx library:
```
pip install onnx onnxscript
```

2. Convert to onnx
```
dummy_input = torch.randn(1, 3, IMAGE_SIZE, IMAGE_SIZE, device=device)
torch.onnx.export(
    model_loaded,              # torch model in eval mode
    dummy_input,               # sample input tensor
    'model.onnx',              # onnx output filename
    input_names=["input"],     # name of onnx graph input
    output_names=["output"],   # name of onnx graph output
    opset_version=18,          # onnx operator standard version, current latest value is 18
    do_constant_folding=True,  # precomputes constant operations to reduce size & improve speed
    dynamo=True,               # Use new exporter, need onnxscript (pip install onnxscript)
)
```

