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
    
def extract_member():
	
	with open("1488236624.fas.1.clstr.sorted", "r" ) as hfile,open("PpD_Cluster_info.txt",'w') as outfile:
		next(hfile,None)
		#pepdict ={}
		writer = csv.writer(outfile,delimiter='\t')
		writer.writerow(["Cluster_Rep.ID","Member_ID"])
		for id_and_linelist in group_by_heading( hfile ):
			#print id_and_linelist
			#x=0
			memlis=[]
			for elem in id_and_linelist:
				
				if '*' in elem:
					seqinfo = elem.split(',')
					seqlen = seqinfo[0][:-2]
					seqid = seqinfo[1].split('*')[0].strip(' ')[:-3][1:]
				elif 'at' in elem:
					meminfo = elem.split(',')
					#print meminfo
					memid = meminfo[1].split('at')[0].strip(' ')[:-3][1:]
					print memid
					memlis.append(memid)
				
			memlis1=",".join(memlis)
			print memlis1
			writer.writerow([seqid,memlis1])
		
extract_member()
