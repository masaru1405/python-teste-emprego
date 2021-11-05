def contaLetras(nomeArquivo):
   f = open(nomeArquivo, 'r')
   palavras = []
   palavras_apenasLetras = []
   letras = []
   alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
   porcentagens = []

   #Adiciona cada palavra na lista 'palavras', sem o '\n'
   for line in f:
      palavras.extend(line.split())

   #Para cada elemento da 'lista palavras', retira a pontuação, se houver, e 
   #adiciona na lista 'palavras_apenasLetras'
   for i in palavras:
      palavras_apenasLetras.append(''.join(filter(str.isalpha, i)))

   #Adiciona as letras de cada elemento da lista 'palavras_apenasLetras' na lista
   #'letras'
   for i in palavras_apenasLetras:
      letras.extend(list(i))


   total = len(letras)
   for i in alfabeto:
      count = 0
      for j in letras:
         if i == j.lower():
            count += 1
      result = (count / total) * 100
      porcentagens.append(result)


   print(palavras)
   print(palavras_apenasLetras)
   print(letras)
   print("size: ", len(letras))
   print("alfabeto: ", len(alfabeto))

   soma = 0
   #Imprimindo o resultado
   for i in range(len(porcentagens)):
      soma += porcentagens[i]
      print("{}: {:.2f}%".format(alfabeto[i], porcentagens[i]))

   print("Total: ", soma)


contaLetras('teste.txt')