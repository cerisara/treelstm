import codecs 
from collections import Counter

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
            widx.append(widxinutt)
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

print("corps",len(train),len(test),len(dev),len(voc))
print("labs",len(trainlabs),len(testlabs),len(devlabs))

print("ll",min(trainlabs),max(trainlabs))
nkepttr=len([y for y in trainlabs if not y==3])
nkeptte=len([y for y in testlabs if not y==3])
nkeptde=len([y for y in devlabs if not y==3])
print("filt",nkepttr,nkeptte,nkeptde)

