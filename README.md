# dict

[![License](https://img.shields.io/github/license/wufeifei/dict.svg)](https://github.com/wufeifei/dict/blob/master/LICENSE)

命令行下中英文翻译工具（Chinese and English translation tools in the command line），翻译服务基于有道翻译。


## 安装(Install)

## fanyi
[![PyPI](https://img.shields.io/pypi/status/Django.svg)](https://github.com/wufeifei/dict)
[![Wercker](https://img.shields.io/wercker/ci/wercker/docs.svg)](https://github.com/wufeifei/dict)
[![GitHub license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/wufeifei/dict)
[![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)](https://github.com/wufeifei/dict)

linux命令行下翻译工具

我觉得原来的使用方法太麻烦了，修改成了适合我使用习惯的方式，还有安装方法我觉得[dantangfan](https://github.com/dantangfan/fanyi)的也很好用，而且内容相对原版简洁很多，不好取舍，那两个都要吧！

`concise_fanyi.py` 为简洁版本！

## Install
```
# 自己选择fanyi.py or concise_fanyi.py 吧
wget https://raw.githubusercontent.com/Yo-gurts/dict/master/fanyi.py
sudo mv ./fanyi.py /usr/local/bin/fy
sudo chmod +x /usr/local/bin/fy

# 还需要下载使用的`pyperclip`, 用于获取剪贴板内容
sudo pip3 install pyperclip
```

## Usage
### 使用上面设置的文件名`fy`进入
```
[yogurt@ss ~]$ fy 
>>>
```
### 自动翻译剪贴板内的内容
选中内容，复制即可
```
>>>
################################### 
#  自动翻译剪贴板内的内容 The content of the automatic translation in the clipboard

#  Explains None
################################### 
>>>
```
### 自己输入相应单词
```
>>>hello
################################### 
#  hello 你好
#  (U: helˈō E: həˈləʊ)
# 
#  n. 表示问候， 惊奇或唤起注意时的用语
#  int. 喂；哈罗，你好，您好
#  n. (Hello) 人名；（法）埃洛
# 
#  Hello : 你好
#           您好
#           哈啰
#  Hello Kitty : 凯蒂猫
#                 昵称
#                 吉蒂猫
#  Hello Bebe : 哈乐哈乐
#                乐扣乐扣
################################### 
>>>
```
### 也可同时输入多个待查询单词
使用，分隔单词
```
>>>automatic, translation
################################### 
#  automatic 自动
#  (U: ˌɔːtəˈmætɪk E: ˌɔːtəˈmætɪk)
# 
#  n. 自动机械；自动手枪
#  adj. 自动的；无意识的；必然的
# 
#  automatic : 自动的
#               宇多田光
#               机械的
#  automatic warehouse : 自动化仓库
#                         自动仓库
#                         主动化仓库
#  automatic differentiation : 自动微分
#                               自动微分法
#                               结合自动微分
################################### 
################################### 
#  translation 翻译
#  (U: trænzˈleɪʃn,trænsˈleɪʃn E: trænzˈleɪʃn; trænsˈleɪʃn)
# 
#  n. 翻译；译文；转化；调任
# 
#  Translation : 翻译
#                 平移
#                 笔译
#  literal translation : 直译
#                         直译法
#                         文化
#  Translation Exposure : 转换风险
#                          换算风险
#                          外币折算风险暴露
###################################
```
### 若使用空格分隔单词认为是查询短语
```
>>>bearing in mind
###################################
#  bearing in mind 牢记
#
#
#  Explains None
#
#  bearing in mind : 记住
#  bearing in mind that : 牢记
#  Bearing in mind the : 铭记的
###################################
>>>
```



