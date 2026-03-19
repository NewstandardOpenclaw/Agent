import csv
import re
import time
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

companies = [
    ("SOMPOケア", "https://www.sompocare.com/"),
    ("ベネッセスタイルケア", "https://kaigo.benesse-style-care.co.jp/"),
    ("ニチイケアパレス", "https://www.nichii-carepalace.co.jp/"),
    ("ツクイ", "https://corp.tsukui.net/"),
    ("ケア21", "https://www.care21.co.jp/"),
    ("チャーム・ケア・コーポレーション", "https://www.charmcc.jp/"),
    ("木下の介護", "https://www.kinoshita-kaigo.co.jp/"),
    ("学研ココファン", "https://www.cocofump.co.jp/"),
    ("ニチイ学館", "https://www.nichiigakkan.co.jp/"),
    ("セントケア・ホールディング", "https://www.saint-care.com/"),
]

def extract_title(html: str) -> str:
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if not m:
        return ""
    t = re.sub(r"\s+", " ", m.group(1)).strip()
    return t

rows = []
for name, url in companies:
    status = "ok"
    title = ""
    err = ""
    code = ""
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; low-load-test/1.0)"})
        with urlopen(req, timeout=20) as resp:
            code = getattr(resp, "status", 200)
            raw = resp.read(300000)
            html = raw.decode("utf-8", errors="ignore")
            title = extract_title(html)
    except HTTPError as e:
        status = "error"
        code = e.code
        err = f"HTTPError: {e.reason}"
    except URLError as e:
        status = "error"
        err = f"URLError: {e.reason}"
    except Exception as e:
        status = "error"
        err = str(e)

    rows.append({"company": name, "url": url, "status": status, "http_status": code, "title": title, "error": err})
    time.sleep(2.0)

out = "/home/ubuntu/.openclaw/workspace/Webscrsping/output_care_10.csv"
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["company", "url", "status", "http_status", "title", "error"])
    w.writeheader()
    w.writerows(rows)

print(f"saved: {out}")
for r in rows:
    print(f"- {r['company']}: {r['status']} ({r['http_status']}) {r['title'][:60]}")
