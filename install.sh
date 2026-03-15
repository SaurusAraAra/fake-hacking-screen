#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Updating packages..."
pkg update -y && pkg upgrade -y

echo "[*] Installing dependencies..."
pkg install -y python nodejs git

echo "[*] Setup selesai!"
echo "Jalankan tool dengan:"
echo "python hack.py"
