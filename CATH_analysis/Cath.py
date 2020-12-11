import csv
with open("PP_common_CATHG3D_pdb.xls", "r" ) as hfile,open("PP_common_CATHG3D_pdb_A.xls","w") as outfile:
	
	Arch={'1.10': 'Orthogonal Bundle','1.20': 'Up-down Bundle','1.25': 'Alpha Horseshoe',
	'1.40': 'Alpha solenoid','1.50': 'Alpha/alpha barrel','2.10': 'Ribbon','2.20': 'Single Sheet',
	'2.30': 'Roll','2.40' : 'Beta Barrel','2.50' : 'Clam','2.60' : 'Sandwich','2.70' : 'Distorted Sandwich',
	'2.80' : 'Trefoil','2.90' : 'Orthogonal Prism','2.100' : 'Aligned Prism','2.102' : '3-layer Sandwich',
	'2.105' : '3 Propellor','2.110' : '4 Propellor','2.115' : '5 Propellor','2.120' : '6 Propellor',
	'2.130' : '7 Propellor','2.140' : '8 Propellor','2.150' : '2 Solenoid','2.160' : '3 Solenoid','2.170' : 'Beta Complex',
	'3.10' : 'Roll','3.15' : 'Super Roll','3.20' : 'Alpha-Beta Barrel','3.30' : '2-Layer Sandwich',
	'3.40' : '3-Layer(aba) Sandwich','3.50' : '3-Layer(bba) Sandwich','3.55' : '3-Layer(bab) Sandwich',
	'3.60' : '4-Layer Sandwich','3.65' : 'Alpha-beta prism','3.70' : 'Box','3.75' : '5-stranded Propeller',
	'3.80' : 'Alpha-Beta Horseshoe','3.90' : 'Alpha-Beta Complex',
	'3.100' : 'Ribosomal Protein L15; Chain: K; domain 2','4.10': 'Irregular'}

	next(hfile,None)
	csvreader = csv.reader(hfile,delimiter='\t')
	writer = csv.writer(outfile,delimiter='\t')
	writer.writerow(['CID','Dom_Name','Name','Frac.of.Enri','Frac.of.Depl','Freq.enri','Freq.depl','Boolean','Class','Architecture'])
	for line in csvreader:
		id1 = line[0]
		id2=id1.split('.')
		id2=str(id2[0]+'.'+id2[1])
		if id2 in Arch:
			vall= Arch[id2]
			writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],vall])
		

