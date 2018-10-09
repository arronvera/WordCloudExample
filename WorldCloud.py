# -*- coding:utf-8 -*-
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import (WordCloud, STOPWORDS, ImageColorGenerator)
import json


##词云生成算法
class WordGenerate:
    def __init__(self, uid, labels):
        self.uid = uid
        self.labels = labels

    def genderate(self):
        if (self.labels):
            ##背景图片路径
            d = path.dirname(__file__)
            alice_coloring = imread(path.join(d, "./data/mask.jpg"))
            ##字体路径
            font_path = path.join(d, './data/black.ttf')
            wc = WordCloud(
                background_color=None,
                mode="RGBA",
                mask=alice_coloring,  # 设置背景图片
                margin=2,
                stopwords=STOPWORDS.add("said"),
                max_font_size=60,  # 字体最大值
                max_words=30,
                font_path=font_path)
            words = json.loads(self.labels)
            ##生成图片
            image_colors = ImageColorGenerator(alice_coloring)
            wc.generate_from_frequencies(words)
            wc.recolor(None, image_colors)
            wc.to_file(path.join(d, './data/' + self.uid + '.png'))
            ##显示
            plt.figure()
            plt.imshow(wc)
            plt.axis("off")
            plt.show()



if __name__ == '__main__':
    labels = '{"爱玩儿":3,"花式温柔":1,"放荡不羁":1,"幽默感":1,"悟性高":1,"校草":2,"专一":1,"爱跑步":1,"开朗":1,"会吉他":1,"上进心":1,"温柔":1}'
    wordcloud = WordGenerate("100017684", labels)
    wordcloud.genderate()
