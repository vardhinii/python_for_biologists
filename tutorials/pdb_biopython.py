from Bio.PDB import PDBParser, PDBList
import os

def fetch_and_parse_pdb(pdb_id, output_dir='pdb_data'):
    """
    Fetch a PDB file using a PDB ID, then parse and extract HETATM coordinates and publication information.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    pdbl = PDBList()
    parser = PDBParser()

    # Fetch the PDB file
    pdb_file_path = pdbl.retrieve_pdb_file(pdb_id, file_format='pdb', pdir=output_dir)

    # Parse the PDB file
    structure = parser.get_structure(pdb_id, pdb_file_path)

    hetatm_coords = []
    publications = []

    # Extract HETATM coordinates
    for model in structure:
        for chain in model:
            for residue in chain:
                if residue.id[0].startswith('H_'):  # HETATM records start with 'H_'
                    for atom in residue:
                        hetatm_coords.append(atom.get_coord())

    # The publication information is usually in the header of the PDB file
    if 'journal' in structure.header:
        publications.append(structure.header['journal'])

    # Save HETATM coordinates and publication information into separate files
    hetatm_file_path = os.path.join(output_dir, f'{pdb_id}_hetatm_coords.txt')
    publication_file_path = os.path.join(output_dir, f'{pdb_id}_publications.txt')

    with open(hetatm_file_path, 'w') as f:
        for coord in hetatm_coords:
            f.write(f"{coord}\n")

    with open(publication_file_path, 'w') as f:
        for pub in publications:
            f.write(f"{pub}\n")

    return hetatm_file_path, publication_file_path

# Example usage
pdb_id = '4HHB'  # Replace with the PDB ID you want to fetch
hetatm_file_path, publication_file_path = fetch_and_parse_pdb(pdb_id)

print(f"HETATM coordinates saved in: {hetatm_file_path}")
print(f"Publication information saved in: {publication_file_path}")

