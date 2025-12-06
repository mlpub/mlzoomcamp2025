# Dockerize

## Configure docker
- Install uv
- Copy dependency (configuration files, onnx, etc)
- Copy lambda_function.py to docker.
- Install dependency lib (torch, onnx, onnxruntime)
- Expose port 8080
- CMD ["lambda_function.lambda_handler"]

# Build docker
docker build -t serverless-app .

# Run docker
docker run -d -p 9100:8080 serverless-app

