# md文件图片自动转换url

自动脚本：

指定文件夹内的所有md都被打开，1. 能够对获取所有文件名（包含嵌套子目录下）并进行循环，判断文件类型是否为md

输入，判断格式为![的找到括号，将括号内的内容改成网络url，写出到指定位置。



```python
# coding:utf-8
import argparse
import os
import re

'''
可以将指定路径的次级文件夹下所有md文件图来源转换为指定url
'''
new_url = 'http://127.0.0.1:8800/' #附加的url前缀
current_dir = '' #当前文件夹名字

def newpat_func(matched):
    global current_dir
    # 打印matched.group 即匹配出来的字符串
    print(matched.group())
    match_result = matched.group()
    # 根据序求改字符串
    i = match_result.find('(')
    pic_name = match_result[i+1:len(match_result)-1]
    new_patt = match_result[:i+1]+new_url+current_dir+'/'+pic_name+')'  #新格式
    print(new_patt)
    return new_patt


def re_match_sub(lines):
    # 正则表达式，需要的格式如下 ![...](...)
    patt = r'!\[.*\]\(.*\)'
    pattern = re.compile(patt)
    # 正则表达式找到![]()并进行替换
    lines = re.sub(pattern, newpat_func, lines)
    return lines


def change_url(path):
    global current_dir
    for dirName in os.listdir(path):
        if os.path.isdir(dirName):
            for filename in os.listdir(dirName):
                if filename.endswith('.md'):
                    print(filename)
                    loc = path+'\\'+dirName+'\\'+filename
                    # print(loc)
                    with open(loc, 'r', encoding='utf-8') as f:
                        lines = f.read()
                        current_dir = dirName
                        lines = re_match_sub(lines)
					# 将替换好的内容写回原文件
                    with open(loc, 'w', encoding='utf-8') as f:
                        f.write(lines)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", help="the path of your md file")

    args = ap.parse_args()
    if args.path:
        path_md = args.path
    else:
        path_md = os.getcwd()
    # 默认路径为当前路径，
    print(path_md)
    change_url(path_md)
```