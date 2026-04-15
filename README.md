# Easy Data Sharing with Raspberry Pi

Turn any USB hard drive into a wireless file server using a Raspberry Pi. Connect the drive, join the Pi's hotspot, and download files from any device via a web interface.

**Won 3rd prize at IIT Guwahati's Techniche (Tech Expo 2018).**

## The Problem

You have 30GB of files to share with 60 people. Passing a pen drive around takes hours. Google Drive caps at 15GB. This device solves it — plug in a drive, and everyone downloads simultaneously over Wi-Fi.

## How It Works

1. Raspberry Pi creates a Wi-Fi hotspot
2. An OwnCloud instance runs on Apache2
3. Any connected USB drive is auto-detected and served via the web interface
4. Users connect to the hotspot and browse files at `http://10.10.0.1/owncloud/`

## Setup

```bash
git clone https://github.com/harsh52/Easy_data_sharing_using_raspberry_pi.git
cd Easy_data_sharing_using_raspberry_pi
sudo python config.py
```

Follow the prompts to configure MariaDB and OwnCloud. Full setup details in the script.

## Tech

Raspberry Pi, Python, Apache2, OwnCloud, MariaDB, DHCP
