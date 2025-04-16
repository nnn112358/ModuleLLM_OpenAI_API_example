# ModuleLLM_OpenAI_API_example_250417

## 環境

 - LLM630 Compute KIT
 - M5_LLM_ubuntu22.04_20250328_AX630C_LITE.axp
( M5_LLM_ubuntu22.04_20250328_AX630C_LITE.axpより古いバージョンではemmcエラーが発生する。)


## ModuleLLM-OpenAI-Plugin

https://github.com/m5stack/ModuleLLM-OpenAI-Plugin


## Install

```
root@m5stack-kit:~# apt install git 
root@m5stack-kit:~# git clone https://github.com/m5stack/ModuleLLM-OpenAI-Plugin
root@m5stack-kit:~# cd ModuleLLM-OpenAI-Plugin
root@m5stack-kit:~# pip install -r requirements.txt 
```

## Start

 LLM630 Compute KITにて、OpenAI互換APIサーバを起動する
```
root@m5stack-kit:~# python3 api_server.py 
```



## Start

```
root@m5stack-kit:~# python vlm_send.py
```

![image](https://github.com/user-attachments/assets/cbe15164-94d4-4c54-b8c6-0f897712f6ec)

https://x.com/nnn112358/status/1912625283339022735
