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

HwProfileGuid = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001"), "HwProfileGuid")[0].replace("{", "").replace("}", "").replace("-", "")

print(f"HwProfileGuid: {HwProfileGuid}")
SystemManufacturer = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\SystemInformation"), "SystemManufacturer")[0]

print(f"SystemManufacturer: {SystemManufacturer}")
HWID = HwProfileGuid + hashlib.md5(SystemManufacturer.encode()).hexdigest()

print(f"HWID: {HWID}\n")
print("Starting checkpoints...")

for url in checkpoints:

    r = session.get(checkpoints[url], headers={
        "Referer": "https://linkvertise.com/"
    }, params = {
    "HWID": HWID
    }) 

    print(f"checkpoint {url} | " + str(r.status_code))
    if url == 3:
        html = bs(r.text, "html.parser")
        key = html.body.find("code", attrs={"style":"background:#29464A;color:#F0F0F0; font-size: 13px;font-family: 'Open Sans';"}).text.strip()
        print("\nkey: " + key)
        break
    
input()
