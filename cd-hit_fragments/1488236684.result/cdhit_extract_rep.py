import csv
from collections import Counter

def group_by_heading(infile):
    matchid = []
    for line in infile:
        if line.startswith( ">Cluster" ):
			line = line
			if matchid: 
				yield matchid
			matchid= [line.strip('\n')]
        elif not line.startswith('>Cluster'):
			line = line.strip('\n').split('\t')
			line = line[1]
			matchid.append(line)
    yield matchid
    
def extract_rep():
	
	with open("1488236624.fas.1.clstr.sorted", "r" ) as hfile,open("PdD_clusterrep.fa",'w') as outfile:
		next(hfile,None)
		#pepdict ={}
		#writer = csv.writer(outfile,delimiter='\t')
		#~ writer.writerow(["Prot.ID","Prot.Len","No.Of.seq"])
		for id_and_linelist in group_by_heading( hfile ):
			#print id_and_linelist
			#x=0
			
			for elem in id_and_linelist:
				if '*' in elem:
					seqinfo = elem.split(',')
					seqlen = seqinfo[0][:-2]
					seqid = seqinfo[1].split('*')[0].strip(' ')[:-3][1:]
					outfile.write(seqid+'\n')
				
			
		
				
extract_rep()
