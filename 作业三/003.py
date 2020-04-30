# 导入词云制作库wordcloud和中文分词库jieba，导入imageio库中的imread函数，并用这个函数读取本地图片，作为词云形状图片
import jieba
import wordcloud
import imageio
mk = imageio.imread("E:\\作业\\文本信息处理\\003\\chinamap.png")
w = wordcloud.WordCloud(mask=mk)
# 构建并配置词云对象w，注意要加scale参数，提高清晰度
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc',
                        mask=mk,
                        scale=15)
# 对来自外部文件的文本进行中文分词，得到以空格分隔的分词结果string并输出为文件
f = open('E:\\作业\\文本信息处理\\003\\02.txt',encoding='utf-8')
txt = f.read()
txtlist = jieba.lcut(txt)
string = " ".join(txtlist)
with open("E:\\作业\\文本信息处理\\003\\02-proceed.txt", "w", encoding='utf-8') as f:
    f.write(string)
# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)
# 将词云图片导出到文件夹
w.to_file('E:\\作业\\文本信息处理\\003\\02-chinamap.png')