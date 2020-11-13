class Opera:
  def __init__(self,nPartido,NumeroPartidos):
    self.eleitores = []
    self.votos = []
    self.partido = []
    self.nPartido = nPartido
    self.NumeroPartidos = NumeroPartidos

  def checavoto(self,titulo):
    for k in self.eleitores:
      if titulo == k:
        return True
  
  def criaVar(self):
    for k in range(self.nPartido):
      self.partido.append([self.NumeroPartidos[k],0])
    

  def direcionaVoto(self):
    for k in self.votos:
      if k == 45:
        self.partido[0][1] = self.partido[0][1]+1
      elif k == 13:
        self.partido[1][1] = self.partido[1][1]+1
      elif k == 65:
        self.partido[2][1] = self.partido[1][1]+1
      
  def conta_voto(self):
     print("####LEGENDA####VOTOS####")
     for k in range(self.nPartido):
       print("#### ",self.partido[k][0],"  ####",self.partido[k][1])
  


Urna = Opera(3,[45,13,65])
Urna.criaVar()
rodando = True
while(rodando):
  titulo = int(input("Digite seu titulo:\n"))
  if Urna.checavoto(titulo) == True:
    print("Já votou")
    rodando = False
  else:
    voto = int(input("Digite seu voto:\n"))
    Urna.eleitores.append(titulo)
    Urna.votos.append(voto)
    confirma = input("Deseja continuar?\n(S) para Sim (N) para Não\n")
    if confirma != "S":
      rodando = False
Urna.direcionaVoto()
Urna.conta_voto()
