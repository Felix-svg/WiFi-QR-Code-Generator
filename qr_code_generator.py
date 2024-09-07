import qrcode

ssid = input("Enter your WiFi SSID: ")
password = input("Enter your WiFi Password: ")
encryption_type = input("Enter your Encryption type e.g (WPA, WEP): ").upper()

wifi_config = f"WIFI:S:{ssid};T:{encryption_type};P:{password};;"

img = qrcode.make(wifi_config)

img.save(f"{ssid}.png")
