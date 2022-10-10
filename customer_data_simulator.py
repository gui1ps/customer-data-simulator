import random

listanomemasc=['Miguel','Fábio','Guilherme','Leandro','Cesar','Gustavo','David','Antonio','Pedro']
listanomefem=['Isabelly','Isadora','Elisa','Claudia','Leticícia','Aurora','Morgana','Julia','Gabrielly','Laura','Luara']
listaescolhidos=[]
dados={}

for vezes in range(0,21):
    escolha= random.randint(0,1)
    if escolha==0:
        elemento=random.choice(listanomemasc)
        if elemento not in listaescolhidos:
            listaescolhidos.append(elemento)     
    else:
        elemento=random.choice(listanomefem)
        if elemento not in listaescolhidos:
            listaescolhidos.append(elemento)
        
for name in listaescolhidos:
    if name in listanomemasc:
        dados.update({name:('MASCULINO',(random.randint(16,30)))})
    elif name in listanomefem:
        dados.update({name:('FEMININO',(random.randint(16,30)))})

for nam,dad in dados.items():
    if dad[0]=='MASCULINO' and dad[1]>21:
        print(nam)
    


