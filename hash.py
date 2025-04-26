import mmh3
import base64

with open('favicon.ico', 'rb') as f:
    favicon = f.read()

hash= mmh3.hash(base64.encodebytes(favicon))
print(hash)
