import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

# res = requests.get("http://127.0.0.1:8000/books/",headers=headers)
# res = requests.post("http://127.0.0.1:8000/books/",headers=headers,data={"title":"鹿鼎记"})
res = requests.delete("http://127.0.0.1:8000/books/4/",headers=headers)
print(res.status_code)
print(res.json())