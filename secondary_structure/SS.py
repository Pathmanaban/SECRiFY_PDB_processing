import csv
from Bio import SeqIO
from collections import Counter

with open('ScD_G30_PDB_hit.txt','r') as hfile,open('ScD_structure2.txt','w') as outfile:
	pdbdict={}
	HE = ['H','I','G']
	SH= ['E','B']
	CO= ['-','S','T']
	val1=[]
	csvreader = csv.reader(hfile,delimiter='\t')
	writer = csv.writer(outfile,delimiter='\t')
	writer.writerow(['ID','H','E','C'])
	for line in csvreader:
		qid = line[0]
		pdbid = line[1].split('|')
		pdbid=pdbid[3]+pdbid[4]
		start,end= line[5],line[6]
		pident,qcov=line[8],line[10]
		#print qcov,pident
		if float(qcov)==30 and float(pident) ==70:
			if qid not in pdbdict:
				pdbdict[qid]=[pdbid,start,end]
	print (len(pdbdict))
	
	
	for qid,val in pdbdict.items():
		val1.append(val[0])
		
	
	idlis=[]
	for sid,val in pdbdict.items():
		#pdb,ch,st,en
		idlis.append([val[0][:4],val[0][4:],int(val[1]),int(val[2]),sid])
		
	
	seq_record = SeqIO.index('SSedit.txt', "fasta")
	
	
	
	for data in idlis:
		H,C,S=0,0,0
		seqid=data[0]+':'+data[1]+':secstr'
		
		
		if seqid in seq_record:
			seq=seq_record[seqid].seq[data[2]:data[3]]
			sscount = dict(Counter(seq))
			#print sscount
			for elem,cnt in sscount.items():
				if elem in HE:
					H+=cnt
				elif elem in SH:
					S+=cnt
				elif elem in CO:
					C+=cnt
			H=float(H)/len(seq)*100
			S=float(S)/len(seq)*100
			C=float(C)/len(seq)*100
			
		#~ print seqid, 'helix=',H,'Sheet=',S,'Coil=',C
			writer.writerow([data[4],H,S,C])	
			
				
	
