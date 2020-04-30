"""
author: tianhao fu

"""
import math
def getTxt(path):
    a = open(path,encoding="utf-8",)
    text = ""
    for line in a.readlines():
        text += line
    return text
def relativeFrequency(text):
    dist = {}
    for character in text:
        if character not in dist:
            dist[character] = 1
        else:
            dist[character] += 1
    for character in dist:
        dist[character] = dist[character]/len(text)
    return dist
def getEntropy(dist):
    entropy = 0
    for key in dist:
        entropy += dist[key]*math.log(dist[key],2)
    return -entropy
def getKL(a,b):
    infinity = 10000000
    dis = infinity
    D = 0
    for key in a:
        if key in b:
            dis = a[key]*math.log(a[key]/b[key],2)
        D += dis
        dis = infinity
    return D
paragraph_1 = getTxt("text1.txt")
paragraph_2 = getTxt("text2.txt")
dist_1 = relativeFrequency(paragraph_1)
dist_2 = relativeFrequency(paragraph_2)
entropy_1 = getEntropy(dist_1)
entropy_2 = getEntropy(dist_2)
Distance_1 = getKL(dist_1,dist_2)
Distance_2 = getKL(dist_2,dist_1)
print(dist_1)
print(dist_2)
print(entropy_1)
print(entropy_2)
print(Distance_2)
print(Distance_1)