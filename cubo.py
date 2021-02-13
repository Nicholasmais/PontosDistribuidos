import plotly.express as px
import random

x = y = z = []
ponto = [[0]*10000,[0]*10000,[0]*10000]
for i in range(0, 10000):
    numx = random.randint(0,100)
    numy = random.randint(0,100)
    numz = random.randint(0,100)
    x.append(numx)
    y.append(numy)
    z.append(numz)
    ponto[0][i] = numx
    ponto[1][i] = numy
    ponto[2][i]= numz

pontomedio = [sum(ponto[0])/10000,sum(ponto[1])/10000,sum(ponto[2])/10000]

df = px.data.iris()

fig = px.scatter_3d(df, x = ponto[0], y = ponto[1], z=ponto[2])
for template in ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]:
    fig.update_layout(template='plotly_dark')

fig.update_traces(marker=dict(size=1,color='rgba(155,155,155,1)',
                              line=dict(width=2,
                                        color='rgba(55,55,55,1)')))



fig.show()
