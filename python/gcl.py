from datetime import datetime

def gcl_init():
	''' GOOD VALUES FOR A, M AND C
		A           M           C
		16807       2147483647  0
		39373       2147483647  0
		742938285   2147483647  0
		950706376   2147483647  0
		1226874159  2147483647  0
		40692       2147483399  0
		40014       2147483563  0
	'''
	global GCL_M,GCL_A,GCL_S,GCL_C,GCL_X
	GCL_M = 2147483647;#valor maximo
	GCL_A = 16807; #0 < a < m
	GCL_S = 13; #0 < s < m
	GCL_C = 1;
	GCL_X = GCL_S;

def gcl_set_seed(seed):
	global GCL_S,GCL_X
	GCL_S = seed;
	GCL_X = GCL_S;

def gcl_randomize():
	global GCL_S,GCL_X
	seed = datetime.now().microsecond
	GCL_S = seed;
	GCL_X = GCL_S;
	
def gcl_r():
	global GCL_M,GCL_A,GCL_S,GCL_C,GCL_X
	GCL_X = (GCL_A*GCL_X+GCL_C) % GCL_M;
	return GCL_X;

def gcl_irandom(x):
	return gcl_r() % (x+1);

def gcl_irandom_range(minimo,maximo):
	return (minimo+gcl_irandom((maximo-minimo)));



gcl_init()
gcl_randomize()
print("Implementação de exibição de 50 números aleatórios: ")
lista = []
for i in range(5):
	temp=[]
	for i in range(10):
		temp.append(gcl_irandom_range(10,50))
	lista.append(temp)
for x in lista:
	print(x)


print("******")
print("******")
print("******")

print("*** Implementação de exemplo de uma  megasena simples: ***")
numeros = []
for i in range(1,61):
	numeros.append(i)
escolhidos = []

for i in range(6):
	escolhidos.append(numeros.pop(gcl_irandom_range(0,len(numeros))))

print("Números escolhidos: ")
print(escolhidos)
