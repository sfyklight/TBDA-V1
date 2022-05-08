import requests
import sys
import os

proxyTor = "socks5://127.0.0.1:" + sys.argv[2]
optionsProxy = {"https":proxyTor,
                 "http":proxyTor}
requests.get(sys.argv[1],proxies=optionsProxy).text

os.system("echo Succes Attacked On "+sys.argv[2])
