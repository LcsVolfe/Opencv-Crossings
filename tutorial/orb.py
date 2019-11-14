import numpy as np
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors
import cv2
import os




########## começa a funcao de descritores
token = cv2.imread('token.png',0)

#maximo de fetures da instancia 512
orb = cv2.ORB_create(nfeatures=512)

#token_gray = cv2.cvtColor(token, cv2.COLOR_RGB2GRAY)

pontos_chave = orb.detect(token, None)

img_pontos_chave = cv2.drawKeypoints(token, pontos_chave, outImage=np.array([]), flags=0)
pontos_chave, descritores = orb.compute(token, pontos_chave)

# return descritores
#################

descritor = descritores


# cv2.imshow('img', img_pontos_chave)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


class pacoteDePalavras:
    def gerar_dicionario(self, lista_descritores):
        kmeans = KMeans(n_clusters = 12)
        kmeans = kmeans.fit(lista_descritores)
        self.dicionario = kmeans.cluster_centers_

    def histograma_de_frequencia(self, descritor):
        try:            
            algoritmo_knn = NearestNeighbors(n_neighbors = 1)
            algoritmo_knn.fit(self.dicionario)
            mais_proximos = algoritmo_knn.kneighbors(descritor, return_distance=False).flatten()

            histograma_caracteristica = np.histogram(mais_proximos, bins=np.arange(self.dicionario.shape[0]+1))[0]
            return mais_proximos
        except AttributeError:
            print('o dicionario nao existe')

    def salvar_dicionario(self, caminho='', nome_dicionario='dicionario.csv'):
        try:
            np.savetxt(os.path.join(caminho, nome_dicionario), self.dicionario, delimiter=',', fmt='%f')
            print('dicionario salvo')
        except AttributeError:
            print('dicionario vazaio')
    def carregar_dicionario(self, caminho='', nome_dicionario='dicionario.csv'):
        self.dicionario = np.loadtxt(os.join(caminho_dicionario), delimiter=',')

teste_palavras_virtuais = pacoteDePalavras()
teste_palavras_virtuais.gerar_dicionario(descritor)
mais_proximos = teste_palavras_virtuais.histograma_de_frequencia(descritor)

print(mais_proximos)

#cv2.imshow('img', img_pontos_chave)

# cv2.waitKey(0)
# cv2.destroyAllWindows()