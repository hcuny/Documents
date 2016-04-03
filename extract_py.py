import urllib.request
file=open("F:\\IQ_py.txt","r")
s=file.read()
#print(s)
print(len(s))
#print(s.split())
print(len(s.split()))
l=s.lower()

keep={'a','q','w','e','r','t','y','u','i','o','p','b','s','d','f','g','h','j','k','l','z','x','c','v','n','m',' '}

def norm(s):
 result=''
 for c in s:
  if c in keep:
   result += c
 return result

#print(norm(l))

n=norm(l)

def make_dict(s):
 s=s.lower()
 word=s.split()
 d={}
 for w in word:
  if w in d:
   d[w] +=1
  else:
   d[w]=1
 return d

d=make_dict(n)
num=sum(d[w] for w in d)
print(num)
lst=[(d[w],w) for w in d]
lst.sort()
lst.reverse()
#print(lst[:50])

def file_stats(fname):

 s=open(fname,'r').read()
 s=norm(s)
 num_chars=len(s)
 d=make_dict(s)
 num_words=sum(d[w] for w in d)
 lst=[(d[w],w) for w in d]
 lst.sort()
 lst.reverse()
 j=1
 for count,word in lst[0:300]:
  print('%2d. %4d %s' % (j,count,word))
  j +=1
  

#file_stats("F:\\IQ_py.txt")

#file_stats("F:\\1984.txt")

file_stats("F:\\Animal_Farm.txt")






