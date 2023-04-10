fulano=1.50
beltrano=1.10
ano=0
while beltrano<fulano:
    beltrano=beltrano+0.03
    fulano=fulano+0.02
    ano=ano+1
print('depois de',ano,'anos beltrano é maior de fulano.')
print('beltrano mede',round(beltrano,2),'e fulano mede',round(fulano,2))
