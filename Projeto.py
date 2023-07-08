import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from wordcloud import WordCloud
import string

#PROBLEMAS
terremoto=["terremoto","tremor","abalo ","sismico","placas", "tectonicas"]
errohumano=["humana","falha","humano","catadores","piloto","trabalhadores"]
tsunami=["tsunami","maremoto","ondas"]
falta_energia=["falta ","energia","queda"]
falha_segurança=["segurança","controle","refrigeração"]
vazamento=["vazamento","liberação","liberar","violada","expor","expondo","expostos","liberados","nuvem"]
super_aquecimento=["superaquecimento","aquecimento" ,"sobreaquecimento","sobreaqueceu","arrefecimento","explosão","incêndio"]


#SOLUÇÕES
evacuacao=["evacuação","evacuamento","evacuados","evacuadas"]
isolamento=["isolamento","isolar","isolados"]
sarcofago=["sarcófago"]
descontaminacao=["descontaminação","descontaminar","depósito"]
limpeza=["limpeza"]
manutencao=["manutenção","reativando","drenando","selados","escavado"]


class Acidente():
    def __init__(self,nome,descricao,solucao):
        self.nome=nome
        self.erro_humano=0
        self.terremoto=0
        self.tsunami=0
        self.falta_energia=0
        self.falha_segurança=0
        self.vazamento=0
        self.super_aquecimento=0
        self.descricao=descricao
        self.solucao=solucao
        self.evacuacao=0
        self.isolamento=0
        self.sarcofago=0
        self.descontaminacao=0
        self.limpeza=0
        self.manutencao=0




    def descricaoAcidente(self):
        x=len(self.descricao)
        for i in range (x):
            if(self.descricao[i] in terremoto):
                self.terremoto=1
            if (self.descricao[i] in errohumano):
                self.erro_humano = 1
            if (self.descricao[i] in tsunami):
                self.tsunami = 1
            if (self.descricao[i] in falta_energia):
                self.falta_energia = 1
            if (self.descricao[i] in falha_segurança):
                self.falha_segurança = 1
            if(self.descricao[i] in vazamento):
                self.vazamento=1
            if (self.descricao[i] in super_aquecimento):
                self.super_aquecimento = 1

        print("-----",self.nome,"------")
        print("Terremoto:",self.terremoto)
        print("Erro humano:",self.erro_humano)
        print("Tsunami:",self.tsunami)
        print("Falta de energia:",self.falta_energia)
        print("Falha de segurança:",self.falha_segurança)
        print("Vazamento:",self.vazamento)
        print("Super Aquecimento:",self.super_aquecimento)

    def descricaoSolucao(self):
        print("\n-----SOLUÇÕES APLICADAS-----\n")
        x = len(self.solucao)
        for i in range(x):
            if(self.solucao[i] in evacuacao):
                self.evacuacao=1
            if (self.solucao[i] in limpeza):
                self.limpeza = 1
            if (self.solucao[i] in isolamento):
                self.isolamento = 1
            if(self.solucao[i] in descontaminacao):
                self.descontaminacao=1
            if(self.solucao[i] in sarcofago):
                self.sarcofago=1
            if (self.solucao[i] in manutencao):
                self.manutencao = 1
        print("Evacuação:",self.evacuacao)
        print("Limpeza:",self.limpeza)
        print("Isolamento humano:",self.isolamento)
        print("Descontaminação:",self.descontaminacao)
        print("Sarcófago:",self.sarcofago)
        print("Manutenção:", self.manutencao)

    def aplicaRBC(self, acidentes):
        x=len(acidentes)
        vetor=[]
        for i in range (x):
            vetor.append(0)
        for i in range (x):
            vetor[i]=self.comparaAcidentes(acidentes[i])
        print(vetor)
        maximo=max(vetor)
        indice=vetor.index(maximo)
        print()
        print("O acidente com a maior similiaridade foi o acidente de",acidentes[indice].nome)
        self.solucao=acidentes[indice].solucao
        self.descricaoSolucao()
        acidentes.append(self)
        print()

    def comparaAcidentes(self,acidente):
        similaridade=0
        if(self.terremoto==acidente.terremoto and self.terremoto==1):
            similaridade=similaridade+1
        if (self.terremoto != acidente.terremoto ):
            similaridade = similaridade - 1
        if (self.erro_humano == acidente.erro_humano and self.erro_humano==1):
            similaridade = similaridade + 1
        if (self.erro_humano != acidente.erro_humano):
            similaridade = similaridade - 1
        if (self.tsunami == acidente.tsunami and self.tsunami==1):
            similaridade = similaridade + 1
        if (self.tsunami != acidente.tsunami):
            similaridade = similaridade - 1
        if (self.falta_energia == acidente.falta_energia and self.falta_energia==1):
            similaridade = similaridade + 1
        if (self.falta_energia != acidente.falta_energia):
            similaridade = similaridade - 1
        if (self.falha_segurança == acidente.falha_segurança and self.falha_segurança==1):
            similaridade = similaridade + 1
        if (self.falha_segurança != acidente.falha_segurança):
            similaridade = similaridade - 1
        if (self.vazamento == acidente.vazamento and self.vazamento==1):
            similaridade = similaridade + 1
        if (self.vazamento != acidente.vazamento):
            similaridade = similaridade - 1
        if (self.super_aquecimento==acidente.super_aquecimento and self.super_aquecimento==1):
            similaridade = similaridade + 1
        if (self.super_aquecimento != acidente.super_aquecimento):
            similaridade = similaridade - 1
        return similaridade


def main():
    fukushima=open("Fukushima.txt",mode='r',encoding='utf-8').read()
    fukushimaSolucao=open("FukushimaSolucao.txt",mode='r',encoding='utf-8').read()
    fukushima=fukushima.lower()
    fukushimaSolucao=fukushimaSolucao.lower()
    fukushima=nltk.wordpunct_tokenize(fukushima)
    fukushimaSolucao=nltk.wordpunct_tokenize(fukushimaSolucao)
    fukushima=Acidente("Fukushima",fukushima,fukushimaSolucao)
    print()
    chernobyl = open("Chernobyl.txt", mode='r', encoding='utf-8').read()
    chernobylSolucao = open("ChernobylSolucao.txt", mode='r', encoding='utf-8').read()
    chernobyl = chernobyl.lower()
    chernobylSolucao = chernobylSolucao.lower()
    chernobyl = nltk.wordpunct_tokenize(chernobyl)
    chernobylSolucao = nltk.wordpunct_tokenize(chernobylSolucao)
    chernobyl = Acidente("Chernobyl", chernobyl, chernobylSolucao)
    print()
    cesio137 = open("Cesio.txt", mode='r', encoding='utf-8').read()
    cesio137Solucao = open("CesioSolucao.txt", mode='r', encoding='utf-8').read()
    cesio137 = cesio137.lower()
    cesio137Solucao = cesio137Solucao.lower()
    cesio137 = nltk.wordpunct_tokenize(cesio137)
    cesio137Solucao = nltk.wordpunct_tokenize(cesio137Solucao)
    cesio137 = Acidente("Cesio137", cesio137, cesio137Solucao)
    print()
    threemileisland = open("ThreeMileIsland.txt", mode='r', encoding='utf-8').read()
    threemileislandSolucao = open("ThreeMileIslandSolucao.txt", mode='r', encoding='utf-8').read()
    threemileisland = threemileisland.lower()
    threemileislandSolucao = threemileislandSolucao.lower()
    threemileisland = nltk.wordpunct_tokenize(threemileisland)
    threemileislandSolucao = nltk.wordpunct_tokenize(threemileislandSolucao)
    threemileisland = Acidente("ThreeMileIsland", threemileisland, threemileislandSolucao)
    print()
    tokaimura1999 = open("Tokaimura1999.txt", mode='r', encoding='utf-8').read()
    tokaimuraSolucao1999 = open("TokaimuraSolucao1999.txt", mode='r', encoding='utf-8').read()
    tokaimura1999 = tokaimura1999.lower()
    tokaimuraSolucao1999 = tokaimuraSolucao1999.lower()
    tokaimura1999 = nltk.wordpunct_tokenize(tokaimura1999)
    tokaimuraSolucao1999 = nltk.wordpunct_tokenize(tokaimuraSolucao1999)
    tokaimura1999 = Acidente("Tokaimura1999", tokaimura1999, tokaimuraSolucao1999)
    print()
    windscale = open("Windscale.txt", mode='r', encoding='utf-8').read()
    windscaleSolucao = open("WindscaleSolucao.txt", mode='r', encoding='utf-8').read()
    windscale = windscale.lower()
    windscaleSolucao = windscaleSolucao.lower()
    windscale = nltk.wordpunct_tokenize(windscale)
    windscaleSolucao = nltk.wordpunct_tokenize(windscaleSolucao)
    windscale = Acidente("Windscale", windscale, windscaleSolucao)
    print()
    kyshtym = open("Kyshtym.txt", mode='r', encoding='utf-8').read()
    kyshtymSolucao = open("kyshtymSolucao.txt", mode='r', encoding='utf-8').read()
    kyshtym = kyshtym.lower()
    kyshtymSolucao = kyshtymSolucao.lower()
    kyshtym = nltk.wordpunct_tokenize(kyshtym)
    kyshtymSolucao = nltk.wordpunct_tokenize(kyshtymSolucao)
    kyshtym = Acidente("Kyshtym", kyshtym, kyshtymSolucao)
    print()
    acidentes=[fukushima,chernobyl,cesio137,threemileisland,tokaimura1999,windscale,kyshtym]
    opc=0
    for i in range(7):
        acidentes[i].descricaoAcidente()
        acidentes[i].descricaoSolucao()
        print()
    while(opc!=3):
        print("1-Listar os acidentes na base de dados")
        print("2-Aplicar o RBC em um novo acidente")
        print("3-Encerrar o programa")
        opc=int(input())
        if(opc==1):
            x=len(acidentes)
            for i in range (x):
                acidentes[i].descricaoAcidente()
                acidentes[i].descricaoSolucao()
                print()
        if(opc==2):
            nome=input("Nome do acidente:")
            descricao=input("Descreva o acidente:")
            descricao=descricao.lower()
            descricao=nltk.wordpunct_tokenize(descricao)
            acidente=Acidente(nome,descricao,"")
            acidente.descricaoAcidente()
            acidente.aplicaRBC(acidentes)
        if(opc==3):
            print("Programa encerrado")

if __name__=="__main__":
    main()