import random
import time

def countSort(B):
	"""Countsort algorithm. needs checks for negative numbers and 0 values"""
	A=B
	k = A[0] #Set k to the first element in the array
	for i in range(1, len(A)): #traverse the array and set K to the largest value
		if A[i]>k:
			k=A[i]
	C=[0 for i in range(k)] #Initialize an array C of length K containing 0's
	for i in range(1,len(A)+1): #Set values of index C[i] equal to the number of times i appears in array A
		C[A[i-1]-1]+=1 #Adjusting for the 0 index problem
	for i in range(k): #Set values of C[i] equal to the sum of C[i] and C[i-1] 
		if i == 0:
			continue
		else:
			C[i]+=C[i-1]
	B = [0 for i in range(len(A))] #Initialize an array B of the same length as A containing 0's
	for i in range(len(A)-1,-1, -1): #Starting at the last value in A, sort it into B
		B[C[A[i]-1]-1]=A[i]
		C[A[i]-1]-=1
	return B


def merge(A,p,q,r):
	n1=q-p+1 #number of elements in the L sub array
	n2=r-q #number of elements in the R sub array
	L=[0 for i in range(n1+1)] #generate a new array with n1+1 elements
	R=[0 for i in range(n2+1)] #generate a new array with n2+1 elements
	for i in range(n1): #populate the L sub array with values from A
		L[i]=A[p+i]
	for j in range(n2): #populate the R sub array with values from A
		R[j]=A[q+j+1]
	L[n1]=float("inf") #set last value in L and R to infinity
	R[n2]=float("inf")
	i=j=0
	for k in range(p,r+1): #compare values in the sorted subarrays & add them smallest first back into A
		if L[i]<=R[j]:
			A[k]=L[i]
			i+=1
		else:
			A[k]=R[j]
			j+=1

def mergeSort(B,p,r):
	A=B
	if p<r: #if the array has 1 element, back out
		q=(p+r)//2
		mergeSort(A,p,q) #MS L SA
		mergeSort(A,q+1,r) #MS R SA
		merge(A,p,q,r) #Merge the subarrays

def countRunTimes(testLists):
	f = open("countruntimes.txt", "w")
	for i in range(len(testLists)):
		first=time.time() #start CPU time
		countSort(testLists[i])
		second=time.time() #stop CPU time
		runtime=str(round(second-first, 4))
		f.write(runtime + '\n') #write the string of the difference to a file
	f.close()

def mergeRunTimes(testLists):
	b = open("mergeruntimes.txt", "w")
	for i in range(len(testLists)):
		first = time.time()
		mergeSort(testLists[i],0,len(testLists[i])-1)
		second=time.time()
		runtime=str(round(second-first, 4))
		b.write(runtime + '\n')
	b.close()

x=[100,1000,10000,100000] #orders of magnitude
for i in x:
		testLists=[9,8,7,6,5,4,3,2,1,i] #This list will contain the other lists
		mergeRunTimes(testLists)
		countRunTimes(testLists)

