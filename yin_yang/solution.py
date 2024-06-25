def yin_yang(s: str) :
    s = ' '+s
    concerned = ['[',']','(',')','"',"'"]
    compteur= [0]
    for i in range(len(s)):
        if s[i] in concerned:
            if s[i] == '[':
                compteur.append(']')
            elif s[i] == '(':
                compteur.append(')')
            elif s[i] == '"' or  s[i] == "'":
                if s[i]  == compteur[-1]:
                    compteur = compteur[:-1]
                else:
                    compteur.append(s[i])
            elif s[i] == ']' or  s[i] == ")":
                if s[i]  == compteur[-1]:
                    compteur = compteur[:-1]
                else:
                    return False
    if len(compteur) > 1:
        return False
    else:
        return True
