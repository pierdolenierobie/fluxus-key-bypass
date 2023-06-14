import os, requests, winreg, hashlib
from bs4 import BeautifulSoup as bs

checkpoints = {
    0: "https://flux.li/windows/start.php?updated_browser=true",
    1: "https://fluxteam.net/windows/checkpoint/check1.php",
    2: "https://fluxteam.net/windows/checkpoint/check2.php",
    3: "https://fluxteam.net/windows/checkpoint/main.php",
}

session = requests.Session()
os.system("cls")
print("Key bypass ty\n")

HwProfileGuid = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001"), "HwProfileGuid")[0].replace("{", "").replace("}", "").replace("-", "")
print(f"HwProfileGuid: {HwProfileGuid}")

SystemManufacturer = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\SystemInformation"), "SystemManufacturer")[0]
print(f"SystemManufacturer: {SystemManufacturer}")

HWID = HwProfileGuid + hashlib.md5(SystemManufacturer.encode()).hexdigest()
print(f"HWID: {HWID}\n")

print("Starting checkpoints...")

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:113.0) Gecko/20100101 Firefox/113.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Referer": "https://linkvertise.com/"
}

params = {
    "HWID": HWID   
}

for url in checkpoints:

    if url == 0:
        headers["Referer"] = "https://flux.li/windows/start.php"
    else:
        headers["Referer"] = "https://linkvertise.com/"
  
    r = session.get(checkpoints[url], headers=headers, params=params)
    print(f"checkpoint {url} | " + str(r.status_code))
    
    if url == 3:
        html = bs(r.text, "html.parser")
        key = html.body.find("code", attrs={"style":"background:#29464A;color:#F0F0F0; font-size: 13px;font-family: 'Open Sans';"}).text.strip()
        print("\nkey: " + key)
        break
    
