import os
import sys
sys.path.append('../')
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

topk = int(sys.argv[1])

dir = r'/home/fantasty/Desktop/文本聚类/save_cuted/'
newdir = r'/home/fantasty/Desktop/文本聚类/save_tags/'
print('开始提取关键词...')
os.mkdir(newdir)

cuted_filename_list = []
corpus = []
for f in os.listdir(dir):
    cuted_filename_list.append(f)
    full_cuted_filename = dir + f
    with open(full_cuted_filename,'rt') as ef:
            cont = ef.read()
    corpus.append(cont)

vectorizer = CountVectorizer()    
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    
word = vectorizer.get_feature_names() #所有文本的关键字
weight = tfidf.toarray()              #对应的tfidf矩阵

cf = 0
for i in weight:#对于tfidf权重矩阵中的每一行（即单个文档的tfidf权重向量）操作

    each_key = []
    each_weight = []

    a = i.tolist()
    #print(a)
    #找tfidf权重最大的n个所对应的词
    for j in range(topk):
        each_weight.append(max(a))
        max_index = a.index(max(a))
        each_key.append(word[max_index])

        #找到一个当前最大值后将其设为0以便找下一个最大的
        a[max_index] = 0
    save_name = newdir + cuted_filename_list[cf]
    with open(save_name,'wt') as pf:
        for i,j in zip(each_key,each_weight):
            print('%s\t%f' % (i,j),file=pf)

    print('提取文章 %s 的关键词' % cuted_filename_list[cf])
    cf += 1
    print('--------------------------------------------------------------------------------')

print('全部关键词已提取完毕')
print('====================================分割线======================================')

