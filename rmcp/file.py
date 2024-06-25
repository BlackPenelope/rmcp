# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 16:38:10 2021

@author: Morita-T1700
"""

import os

def remove_comment(line):
        
    try:
        n = line.index('!')        
    except ValueError:
        return line
    
    return line[0:n]

class File(object):
    def __init__(self, path):

        self.case_name = ''
        self.file_path = path
        self.dir_path = ''
        
        self.expt_path = ''
        self.pfq_path = ''
        self.pek_path = ''
        self.ppcf_path = ''
        self.psq_path = ''
        
        self.nmol_types = 0
        self.npar = 0
        
        # number of plot list
        self.ncgr = []  
        self.ncsq = []
        self.ncfq = []
        self.ncfg = []
        self.ncek = []
        
        # CONST-SUBTRACT
        self.const_sq = [] 
        self.const_fq = []
        
        self.expt_data = None
        self.gr_data = None
        self.sq_data = None
        self.fq_data = None
        self.ek_data = None
        self.fit_data = None
        
    def open(self):
        
        f = open(self.file_path, 'r')
                
        line = f.readline()        
        while not 'MAX-MOVES' in line:
            line = f.readline()
                            
        line = remove_comment(line)        
        
        moves = line.split('=')
        self.nmol_types = len(moves[1].split())
        self.npar = int(self.nmol_types*(self.nmol_types+1)/2)    
        
        f.close()
        
        with open(self.file_path) as f:            
            line = f.readline()            
            while line:
                                
                if '[ EXP ]' in line:
                    
                    line = f.readline()                    
                    if 'GR' in line:
                        
                        line = remove_comment(f.readline())                         
                        while len(line.split()) > 0:                            
                            if 'POINT-RANGE' in line:
                                ns = line.split('=')[1].split()
                                self.ncgr.append(int(ns[1])-int(ns[0])+1)
                                                                                        
                            line = remove_comment(f.readline())   
                            
                        '''
                        f.readline(); f.readline(); f.readline()
                        line = f.readline() # POINT-RANGE                        
                        ns = line.split('=')[1].split()
                        self.ncgr.append(int(ns[1])-int(ns[0])+1)
                        '''
                        
                    elif 'ND' in line:
                        
                        line = remove_comment(f.readline()) 
                        c = 1
                        while len(line.split()) > 0:                            
                            if 'POINT-RANGE' in line:
                                ns = line.split('=')[1].split()
                                self.ncsq.append(int(ns[1])-int(ns[0])+1)
                                                            
                            if 'CONST-SUBTRACT' in line:                                
                                c = int(line.split('=')[1].split()[0])
                            
                            line = remove_comment(f.readline())                        
                                                
                        self.const_sq.append(c)
                        
                        '''
                        f.readline()
                        line = f.readline()
                        ns = line.split('=')[1].split()
                        self.ncsq.append(int(ns[1])-int(ns[0])+1)
                        line = f.readline() # CONST-SUBTRACT
                        
                        c = -1
                        if 'CONST-SUBTRACT' in line:
                            c = int(line.split('=')[1]) - 1
                        self.const_sq.append(c)
                        '''
                    elif 'XRD' in line:     
                                                
                        line = remove_comment(f.readline()) 
                        c = 1
                        while len(line.split()) > 0:
                                                                                    
                            if 'POINT-RANGE' in line:
                                ns = line.split('=')[1].split()
                                self.ncfq.append(int(ns[1])-int(ns[0])+1)
                                                            
                            if 'CONST-SUBTRACT' in line:                                
                                c = int(line.split('=')[1].split()[0])
                            
                            line = remove_comment(f.readline())                        
                                                                       
                        self.const_fq.append(c)
                        
                        '''
                        f.readline()
                        line = f.readline() # POINT-RANGE
                        ns = line.split('=')[1].split()
                        self.ncfq.append(int(ns[1])-int(ns[0])+1)
                        line = f.readline() # CONST-SUBTRACT
                        
                        c = 1
                        if 'CONST-SUBTRACT' in line:
                            c = int(line.split('=')[1]) 
                        self.const_fq.append(c)
                        '''
                    elif 'EXAFS' in line:
                        
                        line = remove_comment(f.readline())                         
                        while len(line.split()) > 0:
                            if 'POINT-RANGE' in line:
                                ns = line.split('=')[1].split()
                                self.ncek.append(int(ns[1])-int(ns[0])+1)
                                                                                        
                            line = remove_comment(f.readline())   

                        '''
                        f.readline()
                        line = f.readline()
                        ns = line.split('=')[1].split()
                        self.ncek.append(int(ns[1])-int(ns[0])+1)
                        '''
                    else:
                        pass
                                                        
                line = f.readline()
                    
        
        self.dir_path = os.path.dirname(self.file_path)
        self.case_name = os.path.splitext(os.path.basename(self.file_path))[0]
        
        self.expt_path = self.dir_path + '/' + self.case_name + '.expt'
        self.pgr_path = self.dir_path + '/' + self.case_name + '.pgr'
        self.pfq_path = self.dir_path + '/' + self.case_name + '.pfq'
        self.pek_path = self.dir_path + '/' + self.case_name + '.pek'
        self.ppcf_path = self.dir_path + '/' + self.case_name + '.ppcf'
        self.psq_path = self.dir_path + '/' + self.case_name + '.psq'
        self.fit_path = self.dir_path + '/' + self.case_name + '.fit'
        