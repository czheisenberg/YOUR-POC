## WHAT'S THIS?

海康威视综合安防任意文件包含漏洞

影响版本: 不详

来源：公开POC，使用后果一切自负!!!



## HOW TO USE?

```bash
python3 poc-hikvision-LFI.py
```

!["help"](D:\MY-CODE\MyCode\poc\hikvision-lfi\images\3.jpg)

### 批量检测

```bash
python3 poc-hikvision-LFI.py -f urls.txt
```

![](D:\MY-CODE\MyCode\poc\hikvision-lfi\images\1.jpg)

### 单个检测

```bash
python3 poc-hikvision-LFI.py -u https://127.0.0.1/
```

![](D:\MY-CODE\MyCode\poc\hikvision-lfi\images\2.jpg)

## END
