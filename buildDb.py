#============================================================
# File:   buildDb.py
# Author: Benny Saxen
# Date:   2019-10-12
#============================================================
import sys,os
import random
import math
import numpy
import numpy as np
import time

#============================================================
def convertFiles2Triples(fname,gname):
#============================================================
    f_in = open(fname,'r')
    f_out = open(gname,'w')
 
    for line in f_in:
        print line
        line = line.strip()
        line = line.replace('triples/','')
        line = line.replace('.tpl','')
        tpl = line.split(':')
        n = len(tpl)
        print n
        sub = tpl[0]
        if n > 1:
            pre = tpl[1]
        uri_s = '<http://rdf.simuino.com/res/'+str(sub)+'>'
        uri_p = '<http://rdf.simuino.com/pre/'+str(pre)+'>'
        
        if n > 2:
            obj = tpl[2]
            uri_o = '<http://rdf.simuino.com/res/'+str(obj)+'> .\n'
        else:
            obj = sub + '_'+pre+ '_hash_of_filecontent'
            uri_o = '<http://rdf.simuino.com/res/'+str(obj)+'> .\n'
        stemp = uri_s + uri_p + uri_o
        f_out.write(stemp)
        print stemp
    f_in.close()
    f_out.close()
    return

run = "ls triples/*.tpl > work.txt"
os.system(run)
convertFiles2Triples("work.txt","triples.nt")