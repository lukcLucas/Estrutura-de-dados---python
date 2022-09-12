class Nodo:
    #esta classe representa um nodo de uma estrutura encadeada
    
    def __init__(self, dado=0, nodo_anterior=None):
         self.dado = dado
         self.anterior = nodo_anterior
    
    
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)
     
class Pilha:
#esta classe representa uma pilha usando em um estrutura encadeada 
    def __init__(self):
      self.topo = None
      
    def __repr__(self):
        return "[" + str(self.topo) + "]"
    
    def insere(self, novo_nodo):
        # insere um elemento no final da pilha
        
    # cria um novo nodo com o dado a ser armazenado
     novo_nodo = Nodo(novo_nodo)
    
    #faz com que o novo nodo seja o topo da pilha
     novo_nodo.anterior = self.topo
    
    #faz com que a cabeca da lista referencie o novo nodo
    
     self.topo = novo_nodo
     
    
    def remove(self):
        #remove o elemento que esta no topo da pilha.
    
      assert self.topo, "Impossivel remover vslor de pilha vazia"
      
      self.topo = self.topo.amterior
      


#cria uma pilha vazia
pilha = Pilha()
print("Pilha vazia:", pilha)

#insere elemento na pilha

for i in range(5):
    pilha.insere(i)
    print("Insere o valor{0} no topo da pilha:{1}".format(i, pilha))
    
#remove elemento na pilha

while pilha.topo != None:
    pilha.remove()
    print("Removendo elemento que esta no topo da pilha", pilha)
    

