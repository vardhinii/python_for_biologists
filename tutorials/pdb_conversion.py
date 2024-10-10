'''
Author: Vardhini K
Date: 09-12-2023
Time: 9:30 AM
Aim: To develop a program to convert pdb files from old format to new format and vice versa
'''

#Import Modules
from Bio.PDB import PDBParser
from Bio.PDB.MMCIFParser import MMCIFParser
from Bio.PDB.mmcifio import MMCIFIO
from Bio.PDB.PDBIO import PDBIO

#Set Output directory
output_dir = "C:\\Users\\student\\Documents\\124010142-C"

#Define function to convert to mmCIF Format
def convert_to_cif(pdb_id, pdb_file):

    #Define PDB Parser
    parser = PDBParser()
    #Get Structure
    structure = parser.get_structure(pdb_id, pdb_file)

    #Define MMCIF IO
    io = MMCIFIO()
    #Set and Save structure 
    io.set_structure(structure)
    io.save(f'{pdb_id}-converted.cif')

    #Return Success Message
    return f'File Converted to PDBx/mmCIF Format Successfully!'

#Define function to convert to PDB Format
def convert_to_pdb(cif_id, mmcif_file):

    #Define MMCIF Parser  
    parser = MMCIFParser()
    #Get Structure
    structure = parser.get_structure(structure_id, mmcif_file)

    #Define PDB IO
    io = PDBIO()
    #Set and Save structure 
    io.set_structure(structure)
    io.save(f'{cif_id}-converted.pdb')

    #Return Success Message
    return f'File Converted to PDB Format Successfully'

#Input Data
structure_id = input('Enter Structure ID: ')
convert = input('Enter File format of input file: ')
input_file = input('Enter File: ')

#Conversion to specified formats
if convert.lower() == 'pdb':
    print(convert_to_cif(structure_id, input_file))
        
elif convert.lower() == 'cif':
    print(convert_to_pdb(structure_id, input_file))    
    

