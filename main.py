from concurrent.futures import ThreadPoolExecutor
from httpx_socks import SyncProxyTransport
from string import ascii_letters
from random import choice
from httpx import Client
import time
import requests
import os

out_file = "proxies.txt"
proxies = open(out_file).readlines()

from hcapt import bypass

O = 1
_0 = 0
__0 = 10000
print("╔╦╗╦╔═╗╔═╗╔═╗╦═╗╔╦╗  ╔═╗╔═╗╔╗╔")
print(" ║║║╚═╗║  ║ ║╠╦╝ ║║  ║ ╦║╣ ║║║")
print("═╩╝╩╚═╝╚═╝╚═╝╩╚══╩╝  ╚═╝╚═╝╝╚╝")
___0 = str(input("\nEnter Invite Code: "))
print("RUNING...")
____0 = open("tokens.txt", "a")
_____0 = ThreadPoolExecutor(max_workers=int(__0))
______0 = open(out_file, encoding='utf-8').readlines()


def _O():
    global _0, ______0
    try:
        _ = ______0[_0]
        _0 += 1
    except:
        _, _0 = ______0[0], 0
    return _.replace('\n', '')


def __O(_0):
    return ''.join(choice(ascii_letters) for _ in range(_0))


while True:
    try:
        with Client(transport=SyncProxyTransport.from_url(
                f'socks4://{_O()}')) as _00:
            _X0 = _00.get("https://discord.com/register"
                          ).headers['set-cookie'].split(";")
        __X0, __X1 = _X0[0].split("=")[1], _X0[6].split(",")[1].split("=")[1]
        break
    except Exception as O0O:
        pass


def ___O(X):
    global __X0, __X1
    X_ = bypass()
    while True:
        try:
            with Client(transport=SyncProxyTransport.from_url(
                    f'socks4://{_O()}')) as _00:
                _ = _00.post(
                    "https://discord.com/api/v9/auth/register",
                    headers={
                        "Host": "discord.com",
                        "Connection": "keep-alive",
                        "sec-ch-ua":
                        '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                        "X-Super-Properties":
                        "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkzLjAuNDU3Ny42MyBTYWZhcmkvNTM3LjM2IEVkZy85My4wLjk2MS40NyIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAuNDU3Ny42MyIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS9jaGFubmVscy81NTQxMjU3Nzc4MTg2MTU4NDQvODcwODgxOTEyMzQyODUxNTk1IiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
                        "X-Fingerprint": "",
                        "Accept-Language": "en-US",
                        "sec-ch-ua-mobile": "?0",
                        "User-Agent":
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47",
                        "Content-Type": "application/json",
                        "Authorization": "undefined",
                        "Accept": "*/*",
                        "Origin": "https://discord.com",
                        "Sec-Fetch-Site": "same-origin",
                        "Sec-Fetch-Mode": "cors",
                        "Sec-Fetch-Dest": "empty",
                        "Referer": "https://discord.com/register",
                        "X-Debug-Options": "bugReporterEnabled",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Cookie": "OptanonConsent=version=6.17.0; locale=th"
                    },
                    json={
                        "fingerprint": "",
                        "username": f"ggboblol | {__O(8)}",
                        "invite": X,
                        "consent": True,
                        "gift_code_sku_id": "",
                        "captcha_key": X_
                    }).json()
            ____0.write("%s\n" % _["token"])
            ____0.flush()
            return _["token"]
        except Exception as O0O:
            pass


def ____O():
    print(___O(___0))


for _ in range(__0):
    _____0.submit(____O)
    O += 1
