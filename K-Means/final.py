from tkinter import *
import subprocess
import re
import numpy
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import Counter

lab = re.compile(r'^label\d:')
equ = re.compile(r'^=========')
cla = re.compile(r'^\[.+\]\s')

x_plot = ['[ARVR] ','[Fintech] ','[机器人] ','[人工智能] ','[网络安全] ','[未来医疗] ','[物联网] ','[智能驾驶] ','[智能硬件] ']

cluster1 = r'/home/fantasty/Desktop/文本聚类/cluster1_result.txt'
cluster2 = r'/home/fantasty/Desktop/文本聚类/cluster2_result.txt'

def the_y_plot_s(cluster_result):
    y_plot_s = []

    with open(cluster_result,'rt') as f:
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
    for c in l:
        y_plot = []
        m = Counter(c)
        for x in x_plot:
            y_plot.append(m[x])
        y_plot_s.append(y_plot)
    return y_plot_s

def drawbar(tit,heigh1,heigh2):
    #plt.rcParams['font.sans-serif']=['SimHei']
    #plt.figure(figsize=(10, 6))

    x_start1 = numpy.arange(0,180,20)
    x_start2 = [i+6 for i in x_start1]
    
    ax.clear()

    ax.bar(x_start1,heigh1,color='g',width =6,alpha=0.6,label='1号(共'+str(sum(heigh1))+'篇)')
    ax.bar(x_start2,heigh2,color='r',width =6,alpha=0.4,label='2号(共'+str(sum(heigh2))+'篇)')
    ax.set_xlabel('文章标签')
    ax.set_ylabel('该类包含的对应文章数量')
    ax.set_title(tit)
    ax.legend(loc='upper right',fontsize=7)
    ax.set_xticks(x_start1)
    ax.set_xticklabels(x_plot,fontsize=7,ha='left')
    #ax.set_xticks(x_plot)

    canvas.show()


    #plt.show()
def get_text():
    var.set('获取的资源存储在source文件夹中，请验收！')
    status=subprocess.call(["python3", "getsource.py"])

def see_text():
    var.set('已查看文章！')
    status=subprocess.call(["nautilus", "/home/fantasty/Desktop/文本聚类/source"])

def cut_text():
    var.set('已点击 提取关键词 按钮')
    status=subprocess.call(["python3", "key_words.py",e1.get()])

def see_cut():
    var.set('已查看关键词文件！')
    status=subprocess.call(["nautilus", "/home/fantasty/Desktop/文本聚类/save_tags"])

def c1():
    global one_count
    one_count += 1
    var.set('第 %s 次运行1号聚类器' % str(one_count))
    status=subprocess.call(["python3", "cluster1.py"])

def c2():
    global two_count
    two_count += 1
    var.set('第 %s 次运行2号聚类器' % str(two_count))
    status=subprocess.call(["python3", "cluster2.py"])

def l1():
    var.set('聚类器第一类的结果')

    heigh1 = the_y_plot_s(cluster1)[0]
    heigh2 = the_y_plot_s(cluster2)[0]
    drawbar('第1类',heigh1,heigh2)

def l2():
    var.set('聚类器第二类的结果')

    heigh1 = the_y_plot_s(cluster1)[1]
    heigh2 = the_y_plot_s(cluster2)[1]
    drawbar('第2类',heigh1,heigh2)

def l3():
    var.set('聚类器第三类的结果')

    heigh1 = the_y_plot_s(cluster1)[2]
    heigh2 = the_y_plot_s(cluster2)[2]
    drawbar('第3类',heigh1,heigh2)

def l4():
    var.set('聚类器第四类的结果')

    heigh1 = the_y_plot_s(cluster1)[3]
    heigh2 = the_y_plot_s(cluster2)[3]
    drawbar('第4类',heigh1,heigh2)

def l5():
    var.set('聚类器第五类的结果')

    heigh1 = the_y_plot_s(cluster1)[4]
    heigh2 = the_y_plot_s(cluster2)[4]
    drawbar('第5类',heigh1,heigh2)

def l6():
    var.set('聚类器第六类的结果')

    heigh1 = the_y_plot_s(cluster1)[5]
    heigh2 = the_y_plot_s(cluster2)[5]
    drawbar('第6类',heigh1,heigh2)

def l7():
    var.set('聚类器第七类的结果')

    heigh1 = the_y_plot_s(cluster1)[6]
    heigh2 = the_y_plot_s(cluster2)[6]
    drawbar('第7类',heigh1,heigh2)

def l8():
    var.set('聚类器第八类的结果')

    heigh1 = the_y_plot_s(cluster1)[7]
    heigh2 = the_y_plot_s(cluster2)[7]
    drawbar('第8类',heigh1,heigh2)

def l9():
    var.set('聚类器第九类的结果')

    heigh1 = the_y_plot_s(cluster1)[8]
    heigh2 = the_y_plot_s(cluster2)[8]
    drawbar('第9类',heigh1,heigh2)

def r1():
    var.set('查看1号聚类器的结果')
    status=subprocess.call(["gedit", "/home/fantasty/Desktop/文本聚类/cluster1_result.txt"])
def r2():
    var.set('查看2号聚类器的结果')
    status=subprocess.call(["gedit", "/home/fantasty/Desktop/文本聚类/cluster2_result.txt"])

def j1():
    var.set('统计1号聚类器本次聚类情况')
    status=subprocess.call(["python3", "ana1.py"])

def j2():
    var.set('统计2号聚类器本次聚类情况')
    status=subprocess.call(["python3", "ana2.py"])
def fenci():
    var.set('已进行分词！')
    status=subprocess.call(["python3","cut_words.py"])

if __name__ == '__main__':

    app = Tk()
    #app.geometry('960x600')

    one_count = 0
    two_count = 0

    app.title('简单文章聚类工具')

    var = StringVar()
    entry_var = StringVar()
    var.set('点击相应按钮进行工作')

    textLabel = Label(app,textvariable=var)
    textLabel.grid(row=0,column=0,rowspan=2,columnspan=3)

    get_button = Button(app,text='获取文章',command=get_text)
    get_button.grid(row=2,column=0)

    see_button = Button(app,text='查看文章',command=see_text)
    see_button.grid(row=2,column=1)

    Label(app,text='输入关键词数：').grid(row=3,column=0)
    e1 = Entry(app,textvariable=entry_var)
    e1.grid(row=3,column=1,columnspan=2)

    cut_button = Button(app,text='提取关键词',command=cut_text)
    cut_button.grid(row=4,column=0)

    see_cut = Button(app,text='查看关键词',command=see_cut)
    see_cut.grid(row=4,column=1)

    c1_button = Button(app,text='1号聚类器',command=c1)
    c1_button.grid(row=5,column=0)

    c2_button = Button(app,text='2号聚类器',command=c2)
    c2_button.grid(row=5,column=1)

    textlabel = Label(app,text='查看聚类效果：')
    textlabel.grid(row=6,column=0)

    l1_button = Button(app,bg='white',text='第1类',command=l1)
    l1_button.grid(row=7,column=0)

    l2_button = Button(app,bg='white',text='第2类',command=l2)
    l2_button.grid(row=7,column=1)

    l3_button = Button(app,bg='white',text='第3类',command=l3)
    l3_button.grid(row=7,column=2,padx=25)

    l4_button = Button(app,bg='white',text='第4类',command=l4)
    l4_button.grid(row=8,column=0)

    l5_button = Button(app,bg='white',text='第5类',command=l5)
    l5_button.grid(row=8,column=1)
    
    l6_button = Button(app,bg='white',text='第6类',command=l6)
    l6_button.grid(row=8,column=2,padx=25)

    l7_button = Button(app,bg='white',text='第7类',command=l7)
    l7_button.grid(row=9,column=0)

    l8_button = Button(app,bg='white',text='第8类',command=l8)
    l8_button.grid(row=9,column=1)

    l9_button = Button(app,bg='white',text='第9类',command=l9)
    l9_button.grid(row=9,column=2,padx=25)

    Label(app,text='查看统计结果：').grid(row=10,column=0)

    r1_button = Button(app,text='1号聚类器结果',command=r1)
    r1_button.grid(row=11,column=0,padx=10)

    r2_button = Button(app,text='2号聚类器结果',command=r2)
    r2_button.grid(row=11,column=1,padx=10)

    j1_button = Button(app,text='1号聚类器统计',command=j1)
    j1_button.grid(row=12,column=0,sticky=N,padx=10)

    j2_button = Button(app,text='2号聚类器统计',command=j2)
    j2_button.grid(row=12,column=1,sticky=N,padx=10)


    quit_button = Button(app,text='进行分词',command=fenci)
    quit_button.grid(row=2,column=2)

    plt.rcParams['font.sans-serif']=['SimHei']

    fig = Figure(figsize=(7,7), dpi=100)
    ax = fig.add_subplot(111)


    canvas = FigureCanvasTkAgg(fig,app)
    canvas.get_tk_widget().grid(row=0,column=3,rowspan=13,sticky=W,padx=290)
    #canvas._tkcanvas.grid(row=0,column=2)

    app.mainloop()


