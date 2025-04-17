# ModuleLLM_OpenAI_API_example

## 概要

ModuleLLM_OpenAI_APIがリリースされたのでお試し。
https://github.com/m5stack/ModuleLLM-OpenAI-Plugin

## 環境

 - LLM630 Compute KIT
 - M5_LLM_ubuntu22.04_20250328_AX630C_LITE.axp
( M5_LLM_ubuntu22.04_20250328_AX630C_LITE.axpより古いバージョンではemmcエラーが発生する。)





## Install

 LLM630 Compute KITでの作業
```
root@m5stack-kit:~# apt install git 
root@m5stack-kit:~# git clone https://github.com/m5stack/ModuleLLM-OpenAI-Plugin
root@m5stack-kit:~# cd ModuleLLM-OpenAI-Plugin
root@m5stack-kit:~# pip install -r requirements.txt 
```

```
root@m5stack-kit:~# apt install llm-model-qwen2.5-0.5b-p256-ax630c
root@m5stack-kit:~# apt install llm-model-internvl2.5-1b-ax630c
```



## Start
 LLM630 Compute KITでの作業
 LLM630 Compute KITにて、OpenAI互換APIサーバを起動する
```
root@m5stack-kit:~# python3 api_server.py 
```

## bash


```
curl -X POST "http://localhost:8000/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_KEY" \
  -d '{
    "model": "internvl2.5-1B-ax630c",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "この画像に何が見えますか？"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "data:image/jpeg;base64,'$(base64 -w 0 test.jpg)'"
            }
          }
        ]
      }
    ],
    "temperature": 0.2
  }'
```

## Python

Ubuntu-PCでの作業。 LLM630 Compute KITでもよい。IPアドレスは書き換えてください。
```
Ubuntu-PC:~# python vlm_send.py
```

![image](https://github.com/user-attachments/assets/cbe15164-94d4-4c54-b8c6-0f897712f6ec)

https://x.com/nnn112358/status/1912625283339022735
