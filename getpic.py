# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 19:16:27 2017

@author: lenovo
"""
#==============================================================================
#获得一个页面上的所有图片的链接并下载到指定的目录下
#未使用多线程，效率较低
#==============================================================================
import re
import requests
import os
GS=['.jpg','.png']

class MyException(Exception):#异常处理
    def __init__(self,message):
        Exception.__init__(self)
        self.message=message

def gethtmltxt(url):#获取页面的txt
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''

def getpic(url,name):#获得图片并保存，请事先设置路径
    try:
        r=requests.get(url)
        r.raise_for_status()
    except:
        return ''
    #获得格式
    pic_cls=re.findall(r'\.\w{2,4}',url)[-1]
    if pic_cls in GS:
        name=name+pic_cls#构建完整名称并写入
        with open(name,'wb') as f:
            f.write(r.content)
    else:
        return ''

def mkdir(path):#创建目录
    if not os.path.exists(path):
        os.makedirs(path)

def ifOKjpblist(jpblist):#判断输入的图片类型是否符合要求
    for i in jpblist:
        j='.'+i
        if j in GS:
            continue
        else:
            raise MyException('Not in list')
#获得一个页面的所有图片链接
#(页面的链接，图片链接列表，需要的图片格式)
def getpicurl(url,jpblist):
    ult=[]
    ifOKjpblist(jpblist)
    for mt in jpblist:
        rx=re.compile(r'http.+?'+mt)
        ult+=re.findall(rx,gethtmltxt(url))
    return ult

def main():
    path='C:\\Users\\lenovo\\Desktop\\临时文件\\bgirl\\Newwwww'
    rooturl='https://www.bbb960.com/htm/pic8/132034.htm'
    mkdir(path)
    os.chdir(path)
    ult=getpicurl(rooturl,['jpg'])
    count=1
    for url in ult:
        getpic(url,str(count))
        count+=1
    #getpic('https://img.581gg.com/picdata-watermark/a1/247/24792-8.jpg','1')
    #print('OK')
        
    
    
if __name__=='__main__':
    main()