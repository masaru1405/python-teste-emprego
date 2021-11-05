#Exercicio que verifica se dada palavra é um palíndromo

def verificaPalindromo(_palavra):
   pilha = []
   palavra = _palavra

   #Empilha as letras da palavra
   for i in palavra:
      pilha.append(i)
   
   #Desempilha e verifica se cada letra desempilhada é igual a palavra[index]
   index = 0
   while pilha:
      letra = pilha.pop()
      if letra == palavra[index]:
         index += 1
         continue
      return False
   
   return True

#Testes
x = verificaPalindromo("ana")
print(x)