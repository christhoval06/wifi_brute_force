export BSSID="60:38:e0:a4:94:49"
export CHANNEL=36
export DEVICE="en0"
# sudo airport $DEVICE sniff $CHANNEL --help
aircrack-ng -w passwords.txt -b $BSSID airportSniff81wKhR.cap