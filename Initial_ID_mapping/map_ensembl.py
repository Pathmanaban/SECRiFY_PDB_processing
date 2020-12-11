import csv
from collections import Counter
def ENSEMBL_map():
	
	with open("Pp_resultstable_depleted.txt", "r" ) as hfile,open("PpD_clusterrep.txt",'r') as infile,open("PpDmap.txt",'w') as outfile:
		next(hfile,None)
		csvreader = csv.reader(hfile,delimiter='\t')
		writer = csv.writer(outfile,delimiter='\t')
		writer.writerow(["ID","Gene ID","Trans.ID"])
		
		pep=[]
		for line in infile:
			line=line.split("_")[1].strip()
			
			pep.append(line)
		print pep	
		for line in csvreader:
			if line[0] in pep:
				seq = ">Seq_"+str(line[0])
				writer.writerow([seq,line[1],line[2]])
				
			
			
	

ENSEMBL_map()()
