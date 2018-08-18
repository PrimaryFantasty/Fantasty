import re
from collections import Counter

lab = re.compile(r'^label\d:')
equ = re.compile(r'^=========')
cla = re.compile(r'^\[.+\]\s')
x_plot = ['[ARVR] ','[Fintech] ','[机器人] ','[人工智能] ','[网络安全] ','[未来医疗] ','[物联网] ','[智能驾驶] ','[智能硬件] ']
y_plot_s = []
with open(r'/home/fantasty/Desktop/文本聚类/cluster1_result.txt','rt') as f:
    l = [0,0,0,0,0,0,0,0,0]
    i = 0
    for line in f:
        a = lab.match(line)
        b = cla.match(line)
        c = equ.match(line)
        if a:
            l[i] = []
        if b:
            l[i].append(b.group())
        if c:
            i += 1
print('--------------------------------------------------------------------------------')
print('                         cluster1')
k = 0
for c in l:
    sum_list = []
    k += 1
    #print('第%d类:' % k)
    m = Counter(c)
    for x in x_plot:
        sum_list.append(m[x])
    print('第%d类（共%d篇）：' % (k,sum(sum_list)))
    for x in x_plot:
        print('   %s：%d篇(占该类比重：%.4f%%)' % (x,m[x],m[x]/sum(sum_list)*100))
    print('--------------------------------------------------------------------------------')
print('================================================================================')        
        
