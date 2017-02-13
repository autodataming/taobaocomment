# 说明
由于Github 打包的exe某些文件上传被.gitignore了，所以不提供windows二进制包

弃用！只能手动复制cookie进subcookie!!!!!!!!!!!!!!!废弃！！

<img src='https://raw.githubusercontent.com/hunterhug/taobaocomment/master/seeme0.jpg' />

一个抓取淘宝评论的Python爬虫
---------------------------------------------------------

一个抓取淘宝天猫评论的爬虫,使用python3.4，爬虫程序已经封装好<br />
支持抓取天猫/淘宝的评论<br />


#更多说明参考pdf


# 使用
安装python3 https://www.python.org/downloads/  然后设置环境变量设置 

1.安装模块请使用    
依赖模块有pymysql, xlswriter, bs4 在window下安装可以找其对应的whl文件。   
```
sudo pip3 install pymysql
sudo pip3 install xlsxwriter
```

2.打包windows二进制
从万能仓库 http://www.lfd.uci.edu/~gohlke/pythonlibs/#cx_freeze 下载对应版本的打包库,然后:

```
pip3 install cx_Freeze-4.3.4-cp35-none-win_amd64.whl
```

下载PIL

Pillow‑3.4.2‑cp34‑cp34m‑win32.whl 改名 Pillow‑3.4.2‑cp34‑none‑win32.whl (装不了就改成none)

 转到源代码文件夹

```
python setup.py build
```

3.运行
把exe.win32-3.4移到根目录taobaocomment，任意改名，以下改为exe，文件目录如下：

```
taobaocomment
-------source
-------exe
-------excel
```

先往taobao.txt中按行写入商品链接

```
网址格式有如下几种(#开头的网址直接被忽视):
https://item.taobao.com/item.htm?spm=a1z10.1-c.w4004-7841214359.4.6lp4CP&id=525842199471
https://detail.tmall.com/item.htm?spm=a230r.1.14.6.o11GZI&id=41389303364&cm_id=140105335569ed55e27b&abbucket=3
https://item.taobao.com/item.htm?id=40066362090
https://rate.tmall.com/list_detail_rate.htm?itemId=45789209181&sellerId=2274061169&order=3&currentPage=2
https://item.taobao.com/item.htm?spm=a230r.1.14.37.B4SrL2&id=45804256292&ns=1&abbucket=3#detail
http://a.m.taobao.com/i44628690678.htm?&abtest=16&sid=ceff9ca9adb294b3459844e3640a76d1
```

执行
```
run.bat
或者
python taobaocomment.py
```


#演示
<img src='https://raw.githubusercontent.com/hunterhug/taobaoscrapy/master/seeme1.jpg' />


Do not understand?contact me.<br/>
author:hunterhug<br/>
2015/11

--------------------------------------------------------------

