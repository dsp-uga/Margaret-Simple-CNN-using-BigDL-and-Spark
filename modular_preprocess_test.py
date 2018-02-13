import numpy as np
import cv2
import os
def convert_to_img(file,number):
	counterx=0	
	x=[]
	temp=[]
	import cv2
	file=file.split(".")[0]
	with open(file+".txt")as f:
		
		for line in f:
			counterx=counterx+1

			values=line.split(" ")
			values=values[1:]
			flag=0
			for j in range(0,len(values)):
				if(values[j]=="??"or values[j]=="??\r\n"):
					flag=1
					break
							
				values[j]=int(values[j],16)
			if(flag==0):
				temp=temp+values
				#print(temp)
			if(len(temp)==16):
				x.append(temp)
				temp=[]
	#for i in range(0,(16-len(temp))/16):
	#	temp=temp+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	#for i in range(counterx,963585):
	#	temp=temp+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]




	x=np.array(x)
	cv2.imwrite("visualize_test/X_test"+str(number)+".png",x) 
	#x=x/x.max()
	#x=x/255

	#print(x.shape)
	#cv2.imwrite("test/X_test"+str(number)+".png",x)
	#return(number)
a=[]
with open("X_test_hash.txt")as ff:
	
	for line in ff:
		a.append(str(line))

counter=0
for ii in range(0,len(a)):
	#print(a[ii])
	print(ii)

	#xx=(str("wget https://storage.googleapis.com/uga-dsp/project2/data/bytes/"+str(a[ii])+".bytes -O txt_X_train/"+str(counter)+".txt"))
	#print((str("wget https://storage.googleapis.com/uga-dsp/project2/data/bytes/"+str(a[ii])+".bytes -O txt_X_train/"+str(counter)+".txt")))
	#os.system((("wget https://storage.googleapis.com/uga-dsp/project2/data/bytes/"+str(a[ii].strip())+".bytes -O txt_X_test/"+str(counter)+".txt")))
	convert_to_img("txt_X_test/"+str(counter)+".txt",counter)
    #print(hi)
	counter=counter+1


















