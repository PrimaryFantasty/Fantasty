
import os, codecs, random
from math import sqrt

big_num = 999999999
everyarticle_mo_s = {}

def readfile(dirname):
    everyarticle_s = {} 
    for f in os.listdir(dirname):
        e = codecs.open(dirname+f, 'r', encoding = 'utf-8') 
        tw_dict = {}
        mo = 0
        for line in e:
            items=line.split('\t')
            token=items[0].strip()
            
            if len(token)<2:
                continue 
            w=float(items[1].strip())
            mo += w**2
            tw_dict[token] = w
        e.close()

        everyarticle_s[f[:-4]] = tw_dict
        everyarticle_mo_s[f[:-4]] = sqrt(float(mo))
    print(len(everyarticle_s))
    return everyarticle_s

def mo(ve):
    return sqrt(sum([pow(b,2) for a, b in ve.items()]))

def cosine(v1, v1_mo, v2, v2_mo):
    if v1_mo == 0 or v2_mo == 0:
        return 1.0
    div = 0
    
    for k, v in v1.items():
        if k in v2:
            div += v*v2[k]
    return 1.0-div/(v1_mo*v2_mo)

def everyarticle_s_range(everyarticle_s):
    tokens = {}
    for k, tw in everyarticle_s.items():
        for t, w in tw.items():
            if t not in tokens:
                tokens[t] = []
            tokens[t].append(w)
    res = {}
    for t, wl in tokens.items():
        res[t] = (min(wl), max(wl))
    return res

#获取每一类文件夹的随机某10篇组成的列表
def get_random_point_list(dir,k):
    random_point_list = []
    i = -1
    point_list = [[] for i in range(k)]
    for son_dir in os.listdir(dir):
        i += 1
        fullname_son_dir = os.path.join(dir,son_dir)
        for filename in os.listdir(fullname_son_dir):
            new_filename = '[' + son_dir + '] ' + filename[:-4]
            point_list[i].append(new_filename)
    for x in range(k):
        for y in range(10):
            nn = random.choice(point_list[x])
            random_point_list.append(nn)
            point_list[x].remove(nn)
        #random_point_list.append(random.choice(point_list[x]))
    return random_point_list
#计算与各个初始点的最近距离
def nearest_clusters(random_point,clusters):
    dis = big_num
    random_row = everyarticle_s[random_point]
    random_point_mo = everyarticle_mo_s[random_point]
    for a,b in enumerate(clusters):
        d_p = cosine(random_row,random_point_mo,b,mo(b))
        if dis > d_p:
            dis = d_p
    return dis
    

#计算类中心
def get_center(clust, everyarticle_s):
    res = {}
    s=len(clust)
    for c in clust:
        for k, v in everyarticle_s[c].items():
            if not k in res:
                res[k] = 0.0
            res[k] += v
    for k, v in res.items():
        res[k] = v/s
    return res

def kcluster(everyarticle_s,dir,k = 3):
    
    clusters = [0.0 for n in range(k)]
    clusters_mo = [0.0 for h in range(k)]

    random_point_list = get_random_point_list(dir,k)

    clusters[0] = everyarticle_s[random.choice(random_point_list)]
    clusters_mo[0] = mo(clusters[0])

    d = [0.0 for _ in range(len(random_point_list))]
    
    for i in range(1,k):
        thesum = 0
        for j,p in enumerate(random_point_list):
            d[j] = nearest_clusters(p,clusters[:i])
            thesum += d[j]
        thesum *= random.random()
        for j,di in enumerate(d):
            thesum -= di
            if thesum > 0:
                continue
            clusters[i] = everyarticle_s[random_point_list[j]]
            clusters_mo[i] = mo(clusters[i])
            break
    
    finalmatches = None
    for t in range(20):
        print('迭代次数：%d' % t)
        bestmatches = [[] for i in range(k)]

        for j in everyarticle_s.keys():
            row = everyarticle_s[j]
            row_mo = everyarticle_mo_s[j]
            bestmatch = 0
            min_dis = big_num
            for i in range(k):
                d=cosine(row, row_mo, clusters[i],clusters_mo[i])
                if d<min_dis:
                    bestmatch = i
                    min_dis = d
            bestmatches[bestmatch].append(j)

      
        if bestmatches == finalmatches: 
            break
        finalmatches = bestmatches

       

        for i in range(k):
            clusters[i] = get_center(bestmatches[i], everyarticle_s)

    return bestmatches

if __name__ == '__main__':
    corpus_dir = r'/home/fantasty/Desktop/文本聚类/save_tags/'
    dir = r'/home/fantasty/Desktop/文本聚类/source/'
    everyarticle_s = readfile(corpus_dir)
    n = 9
    clust = kcluster(everyarticle_s,dir,k=n)
    with open(r'/home/fantasty/Desktop/文本聚类/cluster2_result.txt', 'wt') as fw:
        i=0
        for c in clust:
            i += 1
            fw.write('label%d:\n%s\n===================================================================\n' % (i,'\n'.join([str(v) for v in c])))
    print('================================2号聚类器运行完毕=============================')
