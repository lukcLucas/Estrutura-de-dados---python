class Nodo:
    #esta classe representa um nodo de uma estrutura duplamente encadeada
    
    def __init__(self, dado=0, proximo_nodo=None):
         self.dado = dado
         self.prox = proximo_nodo
    
    def __repr__(self):
         return '%s -> %s' % (self.dado, self.proximo)
     
class Fila:
#esta classe representa uma fila usando em um estrutura encadeada 
    def __init__(self):
      self.prim = None
      self.ult = None
      
    def __repr__(self):
        return "[" + str(self.prim) + "]"
    
    def insere(self, novo_dado):
        #insere um elemento no final da fila 
        
        # cria um novo nodo com dado a ser armazenados 
        novo_nodo = Nodo(novo_nodo)
        
        #insere em uma fila vazia
        if self.prim == None:
            self.prim = novo_dado
            self.ult = novo_dado
        else:
            #faz com que o novo nodo seja o ultimo da fila 
            self.ult.prox = novo_nodo
            
            #faz com que o ultimo da fila referencie o novo nodo
            self.ult = novo_nodo
        
    def remove(self):
        # remove o ultimo elemento da fila 
        
        assert self.prim !=None, "Impossivel remover elemento de fila vazia"
        
        self.prim = self.primeiro.prox
        
        if self.prim == None:
            self.ult = None
            
            
#cria uma fila vazia

fila = Fila()
print("Fila vazia", fila)

#insere elemento na fila 
for i in range(5):
    fila.insere(i)
    print("Insere o valor {0} final da fila: {1}".format(i, fila))
    
#remove elementos da fila 

while fila.prim != None:
    fila.remove()
    print("Removendo elemento que esta no comeco da fila:", fila)    
            
            
            
