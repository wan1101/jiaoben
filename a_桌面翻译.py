#-*- coding: utf-8 -*-
# @Time   : 2022-07-27
# @Author : carl_DJ


import re
import html
from urllib import parse
import requests
import PySimpleGUI as sg

'构建爬虫'
#url 为google自动翻译地址
url = 'http://translate.google.cn/m?q=%s&tl=%s&sl=%s'

'构建翻译函数'
#text:需要翻译的内容， to_language:目标语言类型， text_language:当前语言类型。
def translate(text,to_language = 'en',text_language = 'auto'):
    text = parse.quote(text)
    url1 = url % (text,to_language,text_language)
    repsonse = requests.get(url1)
    data = repsonse.text
    print(f'输出内容：{data}')

    expr = r'(?s)class="(?:t0|result-container)">(.*?)<'
    result = re.findall(expr,data)
    print(f'{result}')
    if (len(result) == 0):
        return ""
    return  html.unescape(result[0])

'GUI搭建'
#设置主题
sg.theme('bluepurple')
#设置字体
font = ("fangsong",12)
#菜单栏设置
menu = [["Help",["About","Item","Author"]]]
#语言选择（前端显示），默认只有6种，可以自己添加
value = ['汉语','英语','日语','法语','俄语','自动']
# 语言选择（后端执行时）
var = ['zh','en','ja','fr','ru','auto']
# 语言字典配置
dic = dict(zip(value,var))
#GUI布局
layout = [[sg.Menu(menu,tearoff=False)],
         [sg.Text(text='输入需要翻译内容',size=(26,1)),
          sg.Text(text='将',size=(2,1),justification='center'),
          sg.Combo(values=value,key='from',size=(10,1)),
          sg.Text(text='翻译为',size=(5,1),justification='center'),
          sg.Combo(values=value,key='to',size=(10,1))],
          [sg.Multiline(key='-IN-',size=(60,8),font=font)],
          [sg.Text(text='翻译结果',size=(30,1),font=font)],
          [sg.Multiline(key='-OUT-',size=(60,8),font=font)],
          [sg.Text(text='',size=(36,1)),
           sg.Button("翻译",size=(6,1)),
           sg.Button("清除",size=(6,1)),
           sg.Button("退出",size=(6,1))
           ]
          ]
# 设置窗口名称，窗口布局，以及图标
window = sg.Window("桌面翻译器",layout,icon='CT.ico')

'逻辑语句执行'
while True:
    #定义 事件 event, 返回值 values
    event,values = window.read()
    #点击“X”或者“退出”按钮时才退出
    if event in (None,"退出"):
        break
    #点击 翻译 按钮
    if event == "翻译":
        if values["to"] == '' or values["from"] =='':
            sg.Popup("请选择语言后再重试")
        else:
            tar = translate(values["-IN-"],dic[values["to"]],dic[values["from"]])
            window["-OUT-"].Update(tar)
    #点击 清除 按钮
    if event =="清除":
        window["-IN-"].update("")
        window["-OUT-"].update("")
    if event == "About":
        #Popup 提示弹窗，给出提示信息
        sg.Popup("使用方法：",
                 "'翻译'确认输入，并输出翻译结果",
                 "'清除'清除已有输入，清空翻译的结果",
                 "'退出'取消，并退出App",
                 title='', font = font, auto_close = 1)
    if event == "Item":
        sg.Popup("翻译类型：",
                 "'输入类型' 输入的语言类型",
                 "'输出类型' 输出的语言类型",
                 title = '', font = font, auto_close = 1)
    if event == "Author":
        sg.Popup("作者简介：",
                 "姓名：XXXXXX",
                 "Wechat:XXXXXX",
                 "E-mail:XXXXXX@qq.com", title='', font=font, auto_close=1)
        window.close()

