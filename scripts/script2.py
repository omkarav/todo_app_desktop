filenames=['1-abc','2-xyz','3-pqr']
filenames=[filename.replace('-','.') +".txt" for filename in filenames] # to convert the filenmaes to 1.abc.txt, 2.xyz.txt,3.pqr.txt
print(filenames)