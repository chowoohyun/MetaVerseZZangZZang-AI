import wget

url = 'https://raw.github.com/vito-ai/openapi-grpc/main/protos/vito-stt-client.proto'
wget.download(url, 'vito-stt-client.proto')
