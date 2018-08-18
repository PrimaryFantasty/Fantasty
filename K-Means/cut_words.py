
import os
import os.path
import sys
sys.path.append('../')

import stopwords

import jieba

dir = r'/home/fantasty/Desktop/文本聚类/source'
save_tags = os.mkdir(r'/home/fantasty/Desktop/文本聚类/save_cuted')
filename_dict = {}

for dirpath,dirnames,filenames in os.walk(dir):
	for filename in filenames:
		#filename_dict[filename] = os.path.join(dirpath,filename)
                new_filename = '[' + dirpath[35:] + '] ' + filename
                filename_dict[new_filename] = os.path.join(dirpath,filename)

#print(list(filename_dict.items()))

i = 0

for key,value in filename_dict.items():
	i += 1
	f = open(value,'rb')
	content = f.read()
	f.close()
	segs = jieba.cut(content, cut_all=False)
	print('正在对文章: %s 进行分词...' % key[:-4])
	final_list = []
	for seg in segs:
		if seg not in stopwords.stop_words_set:
			final_list.append(seg)
	final = ' '.join(final_list)
	file_cuted = r'/home/fantasty/Desktop/文本聚类/save_cuted/' + key
	with open(file_cuted,'wt') as fi:
		fi.write(final)
	print('====================================================================')
print('分词成功，总计有%s篇文章,相关结果已保存到save_cuted文件夹中。' % i)
    



    
    
    


 
