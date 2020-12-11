import csv
from collections import Counter
def extract_transcript():
	
	with open("Sc_resultstable_enriched.txt", "r" ) as hfile,open("ScE_TID.txt",'w') as outfile:
		next(hfile,None)
		Tid=[]
		csvreader = csv.reader(hfile,delimiter='\t')
		x,y=0,0
		
		for line in csvreader:
			x+=1
			
			if line[2] not in Tid:
				Tid.append(line[2])
		for elem in Tid:
			outfile.write(elem+'\n')
		
		
		print x, len(Tid)

extract_transcript()
