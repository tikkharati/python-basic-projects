import numpy as np

def levenshtein(seq1, seq2):
    size_x=len(seq1)+1
    size_y=len(seq2)+1
    matrix =np.zeros ((size_x,size_y))
    for x in range(size_x):
        matrix[x,0]=x
    for y in range(size_y):
        matrix[0,y]=y
    for x in range(1,size_x):
        for y in range(1, size_y):
            if seq1[x-1]==seq2[y-1]:
                matrix[x,y]=min (
                    matrix[x-1,y]+1,
                    matrix[x-1][y-1],
                matrix[x,y-1]+1
                )
            else:
                matrix[x,y]=min(
                    matrix[x-1,y]+1,
                    matrix[x-1,y-1]+1,
                    matrix[x,y-1]+1
                )
           
    return {matrix[size_x-1,size_y-1]}



f1=open ('hello.txt','r')
data= f1.read().replace('\n','')
str1=data.replace(' ','')
f1.close()


f2=open ('filehello2.txt','r')
data= f2.read().replace('\n','')
str2=data.replace(' ','')
f2.close()

if(len(str1)>len(str2)):
    length=len(str1)

else:
    length=len(str2)

l=levenshtein(str1,str2)
s=100-l


print("\n these two files",s ,"% similarity")