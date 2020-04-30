"""
author: tianhao fu

"""
import jieba
from collections import Counter

def way(path):
    data = open(path, encoding="utf-8").read()
    msg = jieba.lcut(data)
    result = Counter(msg)
    print(result)
if __name__=='__main__':
    way("text1.txt")
    print("\n")
    way("text2.txt")




