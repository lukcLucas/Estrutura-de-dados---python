class NodoLista:
    #Esta classe representa um nodo de uma lista encadeada 
    
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.prox = proximo_nodo
        
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.prox)
    
    
class ListaEncadeada:
    #esta classe representa uma lista encadeada
    
    def __init__(self):
        self.cabeca = None
        
    def __repr__(self):
        return "[" + str(self.cabeca) + "]"
    
    
    #insercao
    
    def insere_no_inicio(lista, novo_dado):
        #1) cria um novo nodo com dados a ser armazenado
        novo_nodo = NodoLista(novo_dado)
        
        #2) faz com que o novo nodo seja a cabeca da lista
        novo_nodo.proximo = lista.cabeca
        
        # 3) Faz com que a cabeça da lista referencie o novo nodo.
        lista.cabeca = novo_nodo
        
    def insere_depois(lista, nodo_anterior, novo_dado):
        assert nodo_anterior, "Nodo anterior precisa existir na lista."

       # Cria um novo nodo com o dado desejado.
        novo_nodo = NodoLista(novo_dado)

      # Faz o próximo do novo nodo ser o próximo do nodo anterior.
        novo_nodo.proximo = nodo_anterior.prox

      # Faz com que o novo nodo seja o próximo do nodo anterior.
        nodo_anterior.prox = novo_nodo




lista = ListaEncadeada()
print("Lista vazia:", lista)
insere_no_inicio(lista, 5)
print("Lista contém um único elemento:", lista)

nodo_anterior = lista.cabeca
insere_depois(lista, nodo_anterior, 10)
print("Inserindo um novo elemento depois de um outro:", lista)
        
        
        
        
