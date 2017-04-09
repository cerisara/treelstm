import codecs 
from collections import Counter
import random

wstrinutts = []
widxinutts = []
wstr=[]
widx=[]
voc=Counter()
corp=0
trainlabs,testlabs,devlabs=[],[],[]

with codecs.open('log','r','utf8') as f:
    for l in f:
        l=l.strip()
        if 'loadutt' in l:
            eschar = l[0]
            pos=[p for p in range(len(l)) if l[p]==eschar]
            for i in range(pos[3],pos[2],-1):
                if l[i]=='m':
                    widxinutt = int(l[i+1:pos[3]])
                    break
            for i in range(pos[5],pos[4],-1):
                if l[i]=='m':
                    nwinutt = int(l[i+1:pos[5]])
                    break
            for i in range(pos[6],pos[7]):
                if l[i]=='m':
                    w=l[i+1:pos[7]]
                    break
            for i in range(pos[9],pos[8],-1):
                if l[i]=='m':
                    widxinvoc=int(l[i+1:pos[9]])
                    break
            wstr.append(w)
            widx.append(widxinvoc)
            if w in voc.keys(): assert voc[w]==widxinvoc
            else: voc[w]=widxinvoc
            if widxinutt==nwinutt:
                wstrinutts.append(wstr)
                widxinutts.append(widx)
                wstr,widx=[],[]
            
        if 'detdataset' in l:
            # for i in range(len(l)): print("OOO",i,l[i])
            n=l[26:30]
            nutts = int(n)
            print(nutts)
            if corp==0: train,labs=widxinutts,trainlabs
            elif corp==1: test,labs=widxinutts,testlabs
            else: dev,labs=widxinutts,devlabs
            corp+=1
            wstrinutts,widxinutts=[],[]

        if 'dety' in l:
            pos=[p for p in range(len(l)) if l[p]==eschar]
            for i in range(pos[3],pos[2],-1):
                if l[i]=='m':
                    y = int(l[i+1:pos[3]])
                    labs.append(y)
                    break

vocinv={}
for k,v in voc.items(): vocinv[v]=k

print("corps",len(train),len(test),len(dev),len(voc))
print("labs",len(trainlabs),len(testlabs),len(devlabs))

print("ll",min(trainlabs),max(trainlabs))
kepttr=[i for i in range(len(trainlabs)) if not trainlabs[i]==3]
nkepttr=len(kepttr)
keptte=[i for i in range(len(testlabs)) if not testlabs[i]==3]
nkeptte=len(keptte)
keptde=[i for i in range(len(devlabs)) if not devlabs[i]==3]
nkeptde=len(keptde)
print("filt",nkepttr,nkeptte,nkeptde)

random.shuffle(kepttr)
m=kepttr
for i in range(20):
    y=trainlabs[m[i]]
    x=' '.join([vocinv[x] for x in train[m[i]]])
    print(str(y)+" "+x)

# lab=1 ou 2 = neg, 4 ou 5 = pos

