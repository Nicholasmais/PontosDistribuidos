import plotly.express as px
import random
from pandas import DataFrame

r = 100
x = y = z = []
num = []
ponto = [[0]*10000,[0]*10000,[0]*10000, [0]*10000]
for i in range(0, 10000):
    numx = random.randint(-100,100)
    numy = random.randint(-100,100)
    numz = random.randint(-100,100)
   
    dist = ((numx)**2+(numy)**2+(numz)**2)**(1/2)
    if dist <= r:
        ponto[0][i] = numx
        ponto[1][i] = numy
        ponto[2][i]= numz
        ponto[3][i] = dist
    

df = px.data.iris()

fig = px.scatter_3d(df, x = ponto[0], y = ponto[1], z=ponto[2], color=ponto[3], title='Distribuição de pontos em um Cubo')
for template in ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]:
    fig.update_layout(template='plotly_dark')


fig.update_traces(marker=dict(size=1))
fig.update_layout(scene=dict(xaxis_title="Abscissa", yaxis_title="Ordenada", zaxis_title="Cota"))

fig.show()
'''
df = DataFrame(ponto).transpose()
df.columns = ["x",'y','z','raio']


lista = df['raio'].tolist()

lista.sort()

yy = [0]*100

for i in range (0,100):
    for j in range(0,len(lista)):
        if 0.9*i < lista[j] < i:
            yy[i] += 1 

eixox = []
for i in range(0,100):
    eixox.append(i)
yyround = [round(num) for num in lista]


asd = []
for i in    range(1,101):
    asd.append(yyround.count(i))

print(lista)

plot = [eixox,lista]

densi = px.scatter(x = num, y = ponto[3])
densi.show()'''
