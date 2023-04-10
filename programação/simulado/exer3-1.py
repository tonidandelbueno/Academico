from operator import truediv


cand1=0
cand2=0
cand3=0
cand4=0
cand5=0
nulo=0
maior=0

lup = True

while (lup):
    voto=int(input('Para quem é seu voto? '))

    if voto == 1:
        cand1=cand1+1
    if voto ==2:
        cand2=cand2+1
    if voto ==3:
        cand3=cand3+1
    if voto ==4:
        cand4=cand4+1
    if voto==5:
        cand5=cand5+1
    if voto >5:
        nulo=nulo+1
    if voto ==0:
        lup = False

print('candidato 1:', cand1,'voto(s)')
print('candidato 2:', cand2,'voto(s)')
print('candidato 3:', cand3,'voto(s)')
print('candidato 4:', cand4,'voto(s)')
print('Total de votos em branco:', cand5)
print('Total de votos nulos:', nulo)

if cand1> maior:
    print('candidato 1 ')
elif cand2> maior:
    print('candidato 2 ')
elif cand3> maior:
    print('candidato 3 ')
elif cand4> maior:
    print('candidato 4 ')