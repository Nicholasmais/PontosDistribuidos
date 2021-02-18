import plotly.express as px
from random import uniform
from pandas import DataFrame
from numpy import  arccos, sin, cos, pi, arange

x = y = z = raio = []
ponto = [[0]*10000,[0]*10000,[0]*10000,[0]*10000, [0]*10000]

for i in range (0,10000):
    phi = uniform(0, 2*pi)
    costheta = uniform(-1, 1)
    u = uniform(0, 1)

    theta = arccos(costheta)
    r = 100 * (u)**(1/3)

    x = r * sin(theta) * cos(phi)
    y = r * sin(theta) * sin(phi)
    z = r * cos(theta)

    ponto[0][i] = x
    ponto[1][i] = y
    ponto[2][i]= z

    raio.append(r)

    ponto[3][i] = raio[i]
    ponto[4][i] = i

df = px.data.iris()
fig = px.scatter_3d(df, x = ponto[0], y = ponto[1], z=ponto[2], color=ponto[3])
for template in ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]:
    fig.update_layout(template='plotly_dark')

fig.update_traces(marker=dict(size=1))

fig.show()

df = DataFrame(ponto).transpose()
df.columns = ["x",'y','z','raio', 'ponto']


lista = df['raio'].tolist()

lista.sort()

yy = [0]*100

for i in range (0,100):
    for j in range(0,len(lista)):
        if i-10< lista[j] < i:
            yy[i] += 1 

eixox = []
for i in range(0,100):
    eixox.append(i)

plot = [eixox,lista]

densi = px.scatter(x = plot[0], y = yy)
densi.show()

dense = px.scatter(x=ponto[4], y = ponto[3])
dense.show()