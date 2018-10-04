# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/2/6--21:18
__author__ = 'Henry'

'''
GUI艺术签名设计工具
爬取签名设计网站:http://www.yishuzi.com/
参考教程:https://www.bilibili.com/video/av19137360/
'''

from tkinter import *
import tkinter.messagebox
import requests


def create():
    key = name.get()
    print(key)
    url = 'http://www.yishuzi.com/a/re.php'
    form = {'id': key, 'id1609': 'jiqie', 'id1608': 'jiqie_com', 'id1': '901', 'id2': '#FFFFFE', 'id3': '',
            'id4': '#FF5CC3', 'idi': 'jiqie', 'id5': '', 'id6': '#FF0000'}
    html = requests.post(url, data=form).text
    req = html[10:-2]
    url_1 = 'http://www.yishuzi.com/' + req
    pic = requests.get(url_1).content
    open('1.png', 'wb').write(pic)  # 关键代码在这里!!!怎么将签名图片显示在窗口中
    photo = PhotoImage(file='1.png', width='560', height='220')
    p = Label(root, image=photo)
    p.image = photo
    p.grid(row=0, column=3)


def warning():
    if name.get() == '':
        tkinter.messagebox._show('提醒', '亲~请先填入您的姓名哦~~')
    else:
        create()


root = Tk()
root.title('艺术签名设计工具')
root.geometry('+780+300')
root.resizable(width=False, height=False)  # 禁止用户放大缩小窗口,固定不动

Label(root, text='姓名:', font=('黑体', 20, 'bold'), bg='blue').grid(row=0, column=0)

name = Entry(root, font=('黑体', 20, 'bold'))
name.grid(row=0, column=1)

sign = Button(root, text='一键设计艺术签名', font=('黑体', 20, 'bold'), bg='red', command=warning).grid(row=1, columnspan=2)

mainloop()
