TEXT = "ABRACADABRA"
text = "a dead dad ceded a bad babe a beaded abaca bed"

def table_frequences(texte):
    table = {}
    for caractere in texte:
        if caractere in table:
            table[caractere] += 1
        else:
            table[caractere] = 1
    return table

def arbre_huffman(occurrence : dict):
    # Construction d'un tas avec les lettres sous forme de feuilles
    tas = sorted(occurrence.items(), key = lambda t: t[1])
    tas.reverse()
    # Création de l'arbre
    while len(tas) >= 2:
        noeud1, occ1 = tas.pop() # noeud de plus petit poids occ1
        noeud2, occ2 = tas.pop() # noeud de deuxième plus petit poids occ2
        tas.append(({0: noeud1, 1: noeud2}, occ1 + occ2))
        tas = sorted(tas, key = lambda t: t[1])
        tas.reverse()
        # ajoute au tas le noeud de poids occ1+occ2 et avec les fils noeud1 et noeud2

    return tas.pop()[0]

def code_huffman_parcours(arbre,prefixe,code):
    for noeud in arbre:
        if len(arbre[noeud]) == 1:
            code[prefixe+f"{noeud}"] = arbre[noeud]
        else:
            code_huffman_parcours(arbre[noeud],prefixe+f"{noeud}",code)

def code_huffman(arbre):
    code = {}
    code_huffman_parcours(arbre,'',code)
    return code


def encodage(texte,code):
    code_inv = dict((code[bits], bits) for bits in code)
    # construit le dictionnaire inverse
    texte_binaire = ''
    for c in texte:
        texte_binaire = texte_binaire + code_inv[c]
    return texte_binaire

def decodage(code,texte_binaire):
    texte = ''
    tampon = ''
    for b in texte_binaire:
        tampon = tampon+b
        if tampon in code:
            texte = texte+code[tampon]
            tampon = ''
    return texte



class TreeBuilder:
    
    def __init__(self, text):
        self.text = text
        
    def tree(self):
        return arbre_huffman(table_frequences(self.text))


class Codec:

    def __init__(self, tree):
        self.tree = tree

    def encode(self, text):
        code = code_huffman(self.tree)
        return encodage(text, code)

    def decode(self, encoded):
        code = code_huffman(self.tree)
        return decodage(code, encoded)



builder = TreeBuilder(text)
binary_tree = builder.tree()
codec = Codec(binary_tree)
encoded = codec.encode(text)
decoded = codec.decode(encoded)
assert text == decoded

print(f"{text}\n{encoded}")
if decoded != text:
    print("OOPS")
