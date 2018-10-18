# encoding=utf-8
from django.test import TestCase

# def test(*args,**kwargs):
#     app = kwargs.pop('key1')
#     print(app)
#     print(kwargs)
#     print(args)
#
# test('asdf',{'name':'zhangsan'},name ='java',key1=1212)


'''
读取文件,对文件进行空格分隔，组装成字典
'''

# with open('C:\\Users\\Sam\Desktop\\test_11.txt','r',encoding='utf-8') as r:
#     #print(r.read())
#     #print(r.readline())
#     #print(type(r.read()))
#     #print(type(r.readlines()[0]))
#     lists = r.readlines()
#     dic ={}
#     for i in lists:
#         line = i.split()
#         dic[line[0]]=line[1]
#
#     print(dic)

with open('C:\\Users\\Sam\Desktop\\test_11.txt', 'w', encoding='utf-8') as r:
    r.writelines(['keke', 'strong', 'finish'])

# str = 'asdfasd'
# str2 =''
# for i in str:
#     if(i=='d'):
#         i='java'
#     str2+=i
# print(str2)
str = '-asdfasd-'
str = str.replace('d', 'java')
print(str)
print(str.count('a'))  # 没找到返回0,统计字符串出现的总数
print(str.find('java'))  # 没找到返回-1，查找字符串，找到了就不会去找了
str1 = str.join({'name': '张三', 'value': 18})
print(str1)
print("   ".isspace())
