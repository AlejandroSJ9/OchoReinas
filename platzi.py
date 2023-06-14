def solveNQueens(self, n: int) -> list[list[str]]:
       res = []
       self.dfs([-1]*n, 0, [], res)
       return res
 
def dfs(self, numeros, apuntador, construccionActual, res):
   if apuntador == len(numeros):
       res.append(construccionActual)
       return
   for i in range(len(numeros)):
       numeros[apuntador] = i
       if self.valid(numeros, apuntador):
           tmp = "."*len(numeros)
           self.dfs(numeros, apuntador+1, construccionActual+[tmp[:i]+"Q"+tmp[i+1:]], res)
 
def valid(self, numeros, apuntador):
   for i in range(apuntador):
       if abs(numeros[i]-numeros[apuntador]) == apuntador - i or numeros[i] == numeros[apuntador]:
           return False
   return True

  