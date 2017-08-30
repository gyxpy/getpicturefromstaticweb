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
def gethtmltxt(url):#获取页面的txt
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''
def getpic(url,name,path):
    try:
        r=requests.get(url)
        r.raise_for_status()
    except:
        return ''
    os.chdir(path)#转到路径
    #获得格式
    pic_cls=re.findall(r'\.\w{2,4}',url)[0]
    if pic_cls in GS:
        name=name+pic_cls#构建完整名称并写入
        with open(name,'wb') as f:
            f.write(r.content)
    else:
        return ''
'''    
def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
 
        print(path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
        return False
'''
def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

#输入页面的URL链接与存储URL链接的列表(页面的链接，图片链接列表，需要的图片格式jpg?)
def getpicurl(url,ult,jpblist):
    for j in jpglist:
        if j in GS:
            continue
        else:
            print(wrong)
    rx=re.compile(r'http。+?')#构建匹配图片URL链接的正则表达式
    ult+=re.findall(rx,gethtmltxt(url))
def main():
    path=''
    mkdir(path)
    os.chdir(path)
    ult=[]
    getpicurl(ult)
    for url in ult:
        
        
    
    
if __name__=='__main__':
    main()