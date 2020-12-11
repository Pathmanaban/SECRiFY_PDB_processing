#!/bin/sh
#$ -S /bin/bash
#$ -v PATH=/home/oasis/data/webcomp/RAMMCAP-ann/bin:/usr/local/bin:/usr/bin:/bin
#$ -v BLASTMAT=/home/oasis/data/webcomp/RAMMCAP-ann/blast/bin/data
#$ -v LD_LIBRARY_PATH=/home/oasis/data/webcomp/RAMMCAP-ann/gnuplot-install/lib
#$ -v PERL5LIB=/home/hying/programs/Perl_Lib
##$ -q all.q
#$ -pe orte 4
#$ -e /home/oasis/data/webcomp/web-session/1488236684/1488236684.err
#$ -o /home/oasis/data/webcomp/web-session/1488236684/1488236684.out
cd /home/oasis/data/webcomp/web-session/1488236684
faa_stat.pl 1488236684.fas.0

/home/oasis/data/NGS-ann-project/apps/cd-hit/cd-hit -i 1488236684.fas.0 -d 0 -o 1488236684.fas.1 -c 1.0 -n 5  -G 1 -g 1 -b 20 -s 0.0 -aL 0.0 -aS 0.0 -T 4 -M 32000
faa_stat.pl 1488236684.fas.1
/home/oasis/data/NGS-ann-project/apps/cd-hit/clstr_sort_by.pl no < 1488236684.fas.1.clstr > 1488236684.fas.1.clstr.sorted
clstr_list.pl 1488236684.fas.1.clstr 1488236684.clstr.dump
gnuplot1.pl < 1488236684.fas.1.clstr > 1488236684.fas.1.clstr.1; gnuplot2.pl 1488236684.fas.1.clstr.1 1488236684.fas.1.clstr.1.png
clstr_list_sort.pl 1488236684.clstr.dump 1488236684.clstr_no.dump
clstr_list_sort.pl 1488236684.clstr.dump 1488236684.clstr_len.dump len
clstr_list_sort.pl 1488236684.clstr.dump 1488236684.clstr_des.dump des
tar -zcf 1488236684.result.tar.gz * --exclude=*.dump --exclude=*.env
echo hello > 1488236684.ok
