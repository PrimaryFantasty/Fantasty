
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


def random_firstcenter(res):
    new_res = {}
    for k, v in res.items():
        new_res[k] = random.random()*(v[1]-v[0])+v[0]
    return new_res


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

def kcluster(everyarticle_s,k = 3):
   
    ranges = everyarticle_s_range(everyarticle_s)
    
    clusters = []
    for i in range(k):
        clusters.append(random_firstcenter(ranges))

    clusteres_mo = []
    for i in range(k):
        clusteres_mo.append(mo(clusters[i]))
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
                d=cosine(row, row_mo, clusters[i],clusteres_mo[i])
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
    everyarticle_s = readfile(corpus_dir)
    n = 9
    clust = kcluster(everyarticle_s,k=n)
    with open(r'/home/fantasty/Desktop/文本聚类/cluster1_result.txt', 'wt') as fw:
        i=0
        for c in clust:
            i += 1
            fw.write('label%d:\n%s\n===================================================================\n' % (i,'\n'.join([str(v) for v in c])))
    print('================================1号聚类器运行完毕=============================')
