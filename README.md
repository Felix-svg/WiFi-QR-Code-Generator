# WiFi QR Code Generator

This simple project generates a QR code for connecting to a WiFi network. You can configure your WiFi SSID, password, and encryption type, and the script will generate a QR code that can be scanned to automatically connect to the network.

## Features
- Generates a QR code for WiFi configuration.
- Supports WPA, WEP, or no encryption.
- Saves the QR code as an image.

## Requirements
- Python 3.x
- `qrcode` Python library

## Installation
1. Clone the repository or download the code.
2. Install the required Python library:
   ```bash
   pip install qrcode[pil]

## Usage
1. Open the qr_code_generator.py file.
2. Run the script:
    ```bash
    python qr_code_generator.py
3. Enter the details as required
4. The generated QR code will be saved as ```SSID_Name```.png in the project folder.

## License
This project is licensed under the MIT License.