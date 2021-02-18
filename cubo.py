import plotly.express as px
import random

x = y = z = []
ponto = [[0]*10000,[0]*10000,[0]*10000, [0]*10000]
for i in range(0, 10000):
    numx = random.randint(0,100)
    numy = random.randint(0,100)
    numz = random.randint(0,100)
    x.append(numx)
    y.append(numy)
    z.append(numz)
    dist = ((numx)**2+(numy)**2+(numz)**2)**(1/2)
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


plano = px.scatter(x = ponto[0],y = ponto[1])
plano.update_layout(xaxis_title="Abscissa", yaxis_title="Ordenada")
plano.show()

planoz = px.scatter(x=ponto[0], y = ponto[2])
planoz.update_layout(xaxis_title="Abscissa", yaxis_title="Cota")
planoz.show()

planor = px.scatter(x=ponto[0], y = ponto[3])
planor.update_layout(xaxis_title="Abscissa", yaxis_title="Distância ao centro")
planor.show()