# SECRiFY_PDB_processing

	All the data used for downstream processing can be found here. please navigate the 
	subdirectories for associated data and python scripts used (if any)) for processing
    

### Sub directories

##### 	Initial_ID_mapping	
		contains the data and python script used for mapping between fragments IDs,
		ENSEMBL gene and protein IDs
	
#####	cd-hit_fragments
		contains cluster information from CD-HIT suite: cluster representatives, cluster members, 
		fastA sequences and python scripts used for processing the clusters
			
	    CD-HIT suite: http://weizhong-lab.ucsd.edu/cdhit-web-server/cgi-bin/index.cgi?cmd=cd-hit
	                     
#####	PDB_best3_hits
		contains the filtered PDB hits per fragemnts obtained from blast+ program
			
	    blast+: https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/
	                     
#####	Interproscan
		contains information on protein domains (Pfam,Gene3D), other meta data 
		with the python scripts used for processing the data and the interproscan used
                         
    
    
#####	CATH_analysis
		information on Class, Architecture, families and the fraction of fragments in each class 
		files and the python script used for processing
    
    
#####	secondary structure
		Secondary stcutural information obtained from DSSP and the python script used for 
		processing the same
    
		**sub-dir: Mann–Whitney-U**
		contains the jupyter notebook used for making plots and mann hwitney U statistics
                         
                       
#####	compiled_report_files
		contains a short summary of data porcessing used and some supplimentary plots 
	
	
 
