import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho médio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input(f"Digite o texto {i} (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input(f"Digite o texto {i} (aperte enter para sair): ")

    return textos

def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    return frase.split()

def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas

def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)

def compara_assinatura(as_a, as_b):
    soma_diferencas = sum(abs(as_a[i] - as_b[i]) for i in range(len(as_a)))
    return soma_diferencas / len(as_a)

def calcula_assinatura(texto):
    sentencas = separa_sentencas(texto)
    frases = [frase for sentenca in sentencas for frase in separa_frases(sentenca)]
    palavras = [palavra for frase in frases for palavra in separa_palavras(frase)]

    tam_medio_palavra = sum(len(palavra) for palavra in palavras) / len(palavras)
    rel_type_token = n_palavras_diferentes(palavras) / len(palavras)
    razao_hapax_legomana = n_palavras_unicas(palavras) / len(palavras)
    tam_medio_sentenca = sum(len(sentenca) for sentenca in sentencas) / len(sentencas)
    comp_sentenca = len(frases) / len(sentencas)
    tam_medio_frase = sum(len(frase) for frase in frases) / len(frases)

    return [tam_medio_palavra, rel_type_token, razao_hapax_legomana,
            tam_medio_sentenca, comp_sentenca, tam_medio_frase]

def avalia_textos(textos, ass_cp):
    assinaturas = [calcula_assinatura(texto) for texto in textos]
    similaridades = [compara_assinatura(assinatura, ass_cp) for assinatura in assinaturas]
    return similaridades.index(min(similaridades)) + 1

assinatura = le_assinatura()
textos = le_textos()
infectado = avalia_textos(textos, assinatura)
print(f"O autor do texto {infectado} está infectado com COH-PIAH.")
