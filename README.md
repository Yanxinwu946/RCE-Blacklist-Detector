# RCE-Blacklist-Detector

**RCE-Blacklist-Detector** 是一个专为 CTF RCE 场景设计的黑名单字符探测工具，旨在帮助用户检测目标 URL 中的单字符过滤规则，并协助用户编写绕过 payload。

## 功能特点

- **支持多种请求方法**：可选择 GET 和 POST 请求
- **自定义匹配内容**：指定特定内容以提高检测精准度
- **快速探测黑名单字符**：帮助用户更快地分析目标过滤规则

## 使用说明

执行以下命令以运行工具：

```sh
python rce_blacklist_detector.py -u <目标URL> -p <参数键> [-m <请求方法>] [-c <匹配内容>]
```

**示例**：

```sh
python rce_blacklist_detector.py -u http://example.com -p param -m post -c hack
```

## 参数说明

- `-u`：指定目标 URL
- `-p`：指定测试参数，可通过抓包查看
- `-m`：指定请求方法（GET 或 POST，可选，默认为 POST）
- `-c`：自定义匹配规则关键字，如 "Hacking attempt detected"。
