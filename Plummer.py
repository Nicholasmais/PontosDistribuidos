import plotly.express as px
import random
import numpy as np

a = 3*3.086*10**(19)

x = y = z = raio = []
ponto = [[0]*100000,[0]*100000,[0]*100000,[0]*100000]
pontos = [[],[],[],[]
]
for i in range (0,100000):
    r = a / np.sqrt(np.random.uniform(0, 1) ** (-2.0 / 3.0) - 1)
    phi = (random.uniform(0,2*np.pi))
    the = np.arccos(np.random.uniform(-1,1))

    x = r*np.cos(phi)*np.sin(the)
    y = r*np.sin(phi)*np.sin(the)
    z = r*np.cos(the)


    ponto[0][i] = x
    ponto[1][i] = y
    ponto[2][i]= z

    raio.append(r)


    ponto[3][i] = raio[i]


media = sum(ponto[3])/100000
for i in range(0,100000):
    if ponto[3][i] < 50*media:
        pontos[0].append(ponto[0][i])
        pontos[1].append(ponto[1][i])
        pontos[2].append(ponto[2][i])
        pontos[3].append(ponto[3][i])

df = px.data.gapminder()
fig = px.scatter_3d(df, x = pontos[0], y = pontos[2], z=pontos[1], color=pontos[3])

for template in ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]:
    fig.update_layout(template='plotly_dark')


fig.update_traces(marker=dict(size=1))

#fig.show()


numbers = [0, 0, 0, 0]
volume = [0,0,0,0]
densi= [0,0,0,0]
eixox = ['10^18', '10^19', '10^20', '10^21']

for i in range(0, 4):
    numbers[i] = (sum(j <= 10**(18+i) for j in ponto[3]))
    volume[i] = 4 / 3 * np.pi * (10**(18+i)) ** 3
    densi[i] = numbers[i] / volume[i] * 10**56

plano = px.scatter(x=eixox, y=densi)
plano.update_layout(xaxis_title="Raio", yaxis_title="Densidade de pontos (10^-3)",yaxis_range=[0,5])
plano.show()
