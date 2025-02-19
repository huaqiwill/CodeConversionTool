'''
@File: Encode64.py
@Describe: 
@Create Time: 2020/05/27 15:07:10
@Author: Lookback
@Version: 1.0
'''

import base64
import urllib.parse
import binascii


message = "你好"
base64_message = 'wULrMv6t'
url_message = '%E4%BD%A0%E5%A5%BD'
hex_message = 'e4bda0e5a5bd'

# base64 encode


def base64_encode(message):
    message_bytes = message.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('utf-8')
    print('\nbase64 encode result:', base64_message)

# base64 decode


def if_base64(base64_message):
    alpha_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
    for items in base64_message:
        if items not in alpha_set:
            return False
    return True


def base64_decode(base64_message):
    base64_message = base64_message.rstrip('=')
    if not if_base64(base64_message):
        print('[ERROR]base64 decode result:', 'Not base64\n')
        return False
    for i in range(len(base64_message) % 4):
        base64_message = base64_message+'='
    base64_bytes = base64_message.encode('utf-8')
    message = ''
    try:
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('utf-8')
        print('base64 decode result:', message, '\n')
        return message
    except Exception as e:
        print('[ERROR]base64 decode result:', e, '\n')
        return False


# url decode
def url_encode(message):
    print('url encode result:', urllib.parse.quote(message))

# url encode


def url_decode(url_message):
    print('url decode result:', urllib.parse.unquote(url_message), '\n')

# hex encode


def hex_encode(message):
    print('hex encode result:', binascii.hexlify(message.encode()))


def hex_decode(hex_message):
    print('hex decode result:', binascii.unhexlify(hex_message))


def try_base64(base64_message):
    string = []
    for i in range(0, len(base64_message)-1):
        result = base64_decode(base64_message[i:-1])
        if result:
            string.append(result)
    print(string)


if __name__ == "__main__":
    base64_encode(message)
    base64_decode(base64_message)
    url_encode(message)
    url_decode(url_message)
    hex_encode(message)
    hex_decode(hex_message)
    # try_base64(base64_message)
