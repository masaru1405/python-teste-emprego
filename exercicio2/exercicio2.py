def quadradoMagico(matriz):
   valorFinal = 0

   #Verifica qual o valor da soma de uma linha. Este valor será comparado com outras somas.
   for k in range(len(matriz)):
      valorFinal += matriz[0][k]

   ###Verifica a soma de cada linha###
   for i in range(len(matriz)):
      sumLinha = 0
      for j in range(len(matriz)):
         sumLinha += matriz[i][j]

      if sumLinha != valorFinal:
         print("quadrado não mágico")
         return
      #print("Soma linha: ", sumLinha)
   
   ###Verifica a soma de cada coluna###
   for i in range(len(matriz)):
      sumCol = 0
      for j in range(len(matriz)):
         sumCol += matriz[j][i]
      
      if sumCol != valorFinal:
         print("quadrado não mágico")
         return
      #print("Soma coluna: ", sumCol)

   ###Verifica a soma da diagonal principal###
   sumDiagonalPrincipal = 0
   m = 0
   while m < len(matriz):
      sumDiagonalPrincipal += matriz[m][m]
      m += 1
   #print("Diagonal principal: ", sumDiagonalPrincipal)

   if  sumDiagonalPrincipal != valorFinal:
      print("quadrado não mágico")
      return
   
   ###Verifica a soma da diagonal secundaria###
   sumDiagonalSecundaria = 0
   n = len(matriz) - 1
   k = 0
   while n >= 0:
      sumDiagonalSecundaria += matriz[k][n]
      n -= 1
      k += 1
   
   if  sumDiagonalSecundaria != valorFinal:
      print("quadrado não mágico")
      return
   
   #print("Diagonal secundaria: ", sumDiagonalSecundaria)

   print("quadrado mágico")
  
#Testes
m = [[2,7,6], [9,5,1], [4,3,8]]
n = [[3,5,1],[4,2,2],[5,7,11]]
k = [[5,1],[3,-1]]
quadradoMagico(m)