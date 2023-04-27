
type = input("Type of genetic code : (d/r)")
if(type == "d"):
    yn = input("Do you want the proteins list as well? (y/n) ")
code = input("Enter the Genetic sequence")
codeD = {"A": "T", "T": "A", "G": "C", "C": "G"}
codeR = {"A": "U", "U": "A", "G": "C", "C": "G"}
acidD = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
        }

def corcode(codes,dicts):
    codedr = []
    vc = True
    for el in codes:
        if(el not in dicts):
            vc = False
    if(vc == True):
        for el in codes:
            codedr.append(dicts[f"{el}"])

    else:
        print("Enter a valid code")

    return codedr

def proteins(codes,acidD,codeD):
    proteins = ""
    vc = True
    for el in codes:
        if (el not in codeD):
            vc = False

        if (vc == True):
            if len(codes) % 3 == 0:
                for i in range(0, len(codes), 3):
                    codon = codes[i:i + 3]
                    proteins += acidD[codon]
    return proteins
if type == "d":
    string = ' '.join([str(elem) for i,elem in enumerate(corcode(code,codeD))])
    print(string)
    if yn == "y":
        stringD = ' '.join([str(elem) for i, elem in enumerate(proteins(code, acidD, codeD))])
        print("proteins: "+stringD)
elif type == "r":
    stringr = ' '.join([str(elem) for i, elem in enumerate(corcode(code, codeR))])
    print(stringr)






