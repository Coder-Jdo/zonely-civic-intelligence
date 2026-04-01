import urllib.request
response = urllib.request.urlopen("http://127.0.0.1:8000/download/LS1%201BA")
print("STATUS:", response.status)
print("HEADERS:")
for k, v in response.getheaders():
    print(f"{k}: {v}")
