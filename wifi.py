import os

def scan_wifi():
    try:
        result = os.popen('adb shell "dumpsys wifi | grep ^\\*ssid"').read()
        networks = [line.split(":")[1].strip() for line in result.splitlines()]
        return networks
    except Exception as e:
        return str(e)

available_wifi = scan_wifi()
print("Available Wi-Fi Networks:", available_wifi)
