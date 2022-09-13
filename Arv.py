class Arv:
    
     def __init__(self, chave=None, esq=None, dir=None):
            self.chave = chave
            self.esq = esq
            self.dir = dir
        
     def __repr__(self):
        return '%s <- %s -> %s' % (self.esq and self.esq.chave,
                                       self.chave,
                                       self.dir and self.dir.chave)
    
     def __init__(self, chave= None):
        if chave != None:
            self.chave = chave
        else:
          self.chave = None
        
        self.esq = None
        self.dir = None   
        
     
    # #caminhamento em ordem
    
     def em_ordem(raiz):
           if not raiz:
                 return
      #visita filho da esquerda
     em_ordem(raiz.esq)
      #visita nodo corrente
     print(raiz.chave)       
      #visita filho da direita 
     em_ordem(raiz.dir)
    
     #inserir
      
     def insert(self, chave):
        if self.chave:
            if chave < self.chave:
               if self.esq is None:
                 self.esq = Arv (chave)
               else:
                 self.esq.insert(chave)
            elif chave > self.chave:
                if self.dir is None:
                   self.dir = Arv(chave)
                else:
                   self.dir.insert(chave)
            else:
              self.chave = chave        
     
     #percorrer a arvore inteira
     
     def printvalues(self):
      if self.esq:
         self.printvalues()  #para percorrer uma arvore binaria e imprimir o conteudo na ordem desejada
                             #devemos usar a travessia em ordem, esse tipo de percurso comeca a imprimir 
                             # os valores da esquerda, depois para centro e finalmente para direita
                             #as funcoes de travessia de arvore tambem devem ser recursivas
                             #aqui nessa funcao para percorrer a arvore existente 
         
         print(self.chave) 
         
         
         if self.dir:
            self.dir.printvalues()      
     
     
     #busca
     
     def busca(raiz, chave):
        #Procura por uma chave em uma árvore binária de pesquisa.
    # Trata o caso em que a chave procurada não está presente.
      if raiz is None:
         return None

    # A chave procurada está na raiz da árvore.
      if raiz.chave == chave:
         return raiz

    # A chave procurada é maior que a da raiz.
      if raiz.chave < chave:
         return busca(raiz.dir, chave)

    # A chave procurada é menor que a da raiz.
         return busca(raiz.esq, chave)   




#cria uma arvore binaria de pesquisa
arv = Arv(40)
##arv.dir  = Arv(1)
#arv.esq = Arv(20)
#arv.dir  = Arv(60)

#arv.dir.esq  = Arv(50)
#arv.dir.dir   = Arv(70)
#arv.esq.esq = Arv(10)
#arv.esq.dir  = Arv(30)
#arv.insert(80)
#print("Árvore: ", arv)
#print(arv.esq.chave)
#print(arv.dir.chave)

for chave in [20, 60, 50, 70, 10, 30]:
      nodo = Arv(chave)
      insert(arv, nodo)
   
# Procura por valores na árvore.
for chave in [-50, 10, 30, 70, 100]:
    resultado = busca(raiz, chave)
    if resultado:
        print("Busca pela chave {}: Sucesso!".format(chave))
    else:
        print("Busca pela chave {}: Falha!".format(chave))
    
    

  
