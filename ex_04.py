sp : float
rj : float
mg : float
es : float
outros : float
faturamento : float
percentualSP : int
percentualRJ : int
percentualMG : int
percentualES : int
percentualOutros : int

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

faturamento = sp + rj + mg + es + outros

percentualSP = (sp * 100) / faturamento
percentualRJ = (rj * 100) / faturamento
percentualMG = (mg * 100) / faturamento
percentualES = (es * 100) / faturamento
percentualOutros = (outros * 100) / faturamento

print(f"O percentual em São Paulo foi: {percentualSP:.2f}%")
print(f"O percentual no Rio de Janeiro foi: {percentualRJ:.2f}%")
print(f"O percentual em Minas Gerais foi: {percentualMG:.2f}%")
print(f"O percentual no Espírito Santo foi: {percentualES:.2f}%")
print(f"O percentual em outros foi: {percentualOutros:.2f}%")




