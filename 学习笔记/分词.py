#jieba导入txt文件，分词并统计出现次数保存为txt

import jieba

文件 = input('同文件夹请输入名称：')
txt = open(文件,'r',encoding='utf-8').read()
words = jieba.lcut(txt) #使用精确模式对文本进行分词
counts = {} #通过键值对的形式存储词语极其出现的次数

for word in words:
    if len(word) == 1: #单个词语不计算在内
        continue
    else:
        counts[word] = counts.get(word,0) + 1 #遍历所有词语，每出现一次对应的值将加1
items = list(counts.items()) #将键值对转换成列表
items.sort(key=lambda x: x[1],reverse=True) #根据词语出现的次数进行从大到小排序

for i in range(len(items)):
    word,count = items[i] #items[i]为元祖
    print("{0:<5}{1:>5}".format(word,count))
    with open(文件[:-4]+'分析.txt','a+',encoding='utf-8') as f:
        f.write(items[i].__str__()) # 元祖.__str__()将元祖按字符串处理
