import argparse
import sys
from requests import post, get, RequestException
from urllib.parse import quote


def detect_blacklist(url, param_key, method="post", match_content="hack"):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    blacklist_chars = []
    encoded_success_chars = []
    failed_chars = []

    for i in range(32, 127):
        char = chr(i)
        data = {param_key: char}
        try:
            if method.lower() == "post":
                response = post(url, data=data, headers=headers)
            elif method.lower() == "get":
                response = get(url, params=data, headers=headers)
            else:
                raise ValueError("Unsupported method. Use 'post' or 'get'.")

            response.raise_for_status()
            if match_content in response.text:
                blacklist_chars.append(char)
        except RequestException:
            try:
                encoded_char = quote(char)
                data = {param_key: encoded_char}
                if method.lower() == "post":
                    response = post(url, data=data, headers=headers)
                elif method.lower() == "get":
                    response = get(url, params=data, headers=headers)
                response.raise_for_status()
                if match_content in response.text:
                    encoded_success_chars.append(encoded_char)
            except RequestException:
                failed_chars.append(f"{char} ({encoded_char})")

    return blacklist_chars, encoded_success_chars, failed_chars


def main():
    parser = argparse.ArgumentParser(description="RCE 黑名单探测工具")
    parser.add_argument("-u", "--url", required=True, help="目标 URL")
    parser.add_argument("-p", "--param_key", required=True, help="参数键")
    parser.add_argument(
        "-m",
        "--method",
        choices=["get", "post"],
        default="post",
        help="HTTP 方法 (默认: post)",
    )
    parser.add_argument(
        "-c", "--match_content", default="hack", help="匹配内容 (默认: hack)"
    )

    args = parser.parse_args()

    print("欢迎使用 RCE 黑名单探测工具")
    print("\033]8;;https://github.com/Yanxinwu946/RCE-Blacklist-Detector\033\\github.com/Yanxinwu946/RCE-Blacklist-Detector\033]8;;\033\\")
    print(" __     __ ___   ____  _____     __  __")
    print(" \\ \\   / // _ \\ |  _ \\|_   _|___ \\ \\/ /")
    print("  \\ \\ / /| | | || |_) | | | / _ \\ \\  / ")
    print("   \\ V / | |_| ||  _ <  | ||  __/ /  \\ ")
    print("    \\_/   \\___/ |_| \\_\\ |_| \\___|/_/\\_\\")
    print()
    print("正在检测黑名单字符...")

    blacklist_chars, encoded_success_chars, failed_chars = detect_blacklist(
        args.url, args.param_key, args.method, args.match_content
    )

    if blacklist_chars:
        print("\n匹配黑名单的字符:")
        print("".join(blacklist_chars))

    if encoded_success_chars:
        print("\nURL编码后成功的字符:")
        print("".join(encoded_success_chars))

    if failed_chars:
        print("\nURL编码后仍然失败的字符:")
        print("\n".join(failed_chars))


if __name__ == "__main__":
    main()
