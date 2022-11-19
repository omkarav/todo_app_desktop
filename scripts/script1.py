contents=["contents of file 1",'contents of file 2','contents of file3']
files=['file1.txt','file2.txt','file3.txt']
for content,file in zip(contents,files):
    abc=open(fr"C:\Users\omkarav\Downloads\python_learn\files\{file}",'w')
    abc.write(content)
    abc.close()