import plotly.express as px
from numpy import random

x = random.uniform(0,100,10000)
y = random.uniform(0,100,10000)
z = random.uniform(0,100,10000)

yy = [0]*10
eixox = ['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100']

for r in range(0,10):
    temp = []

    for k in range(0,10000):
        
        if x[k] <= 10*r+10 and x[k] > 10*r:
            temp.append(x[k])

    yy[r] = len(temp)

#cor = sorted(x)
df = px.data.iris()

fig = px.scatter_3d(df, x = x, y = y, z=z, title='Distribuição de pontos em um Cubo')
fig.update_traces(marker=dict(size=1))
fig.update_layout(template = 'plotly_dark',scene=dict(xaxis_title="Abscissa", yaxis_title="Ordenada", zaxis_title="Cota"))
fig.show()

plano = px.line(x=eixox, y=yy, title="Cubo")
plano.update_layout(xaxis_title="Abscissa", yaxis_title="Quantidade de pontos", yaxis_range = [0,2000])
plano.show()

