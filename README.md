# REV3NANT

**Rev3nant** is a harmless proof-of-concept script designed for use in **USB drop** attack simulations.  
When inserted and interacted with, it collects basic device information from the target computer and displays a message indicating that the user has failed a phishing or security awareness test.

This tool is intended **exclusively** for penetration testers and security teams conducting authorized phishing or attack simulations within their organization.

---

## 📦 Installation

```bash
git clone https://github.com/m3m0rydmp/Rev3nant.git
```

## 💡 Usage Notes
You can disguise the payload to appear as a legitimate file (e.g., .docx, .xlsx, etc.), depending on your testing approach.

### ⚠ Important:
This script requires a USB device with custom firmware such as the [Hak5 Rubber Ducky](https://shop.hak5.org/products/usb-rubber-ducky).
Such devices can emulate a keyboard/mouse, allowing keystroke injection immediately upon insertion.

By default, modern Windows operating systems have disabled the Autorun feature for standard USB storage devices. This means scripts will not execute automatically unless using an HID (Human Interface Device) approach.
Read more in the official Microsoft documentation: [Autoplay and Autorun](https://learn.microsoft.com/en-us/windows/win32/shell/autoplay-reg).