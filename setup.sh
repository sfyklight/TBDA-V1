apt update -y
apt-get update -y
apt install tor -y
service tor start
service tor stop
apt install python3 -y
pip3 install requests[socks]
mv torrc /etc/tor/torrc


