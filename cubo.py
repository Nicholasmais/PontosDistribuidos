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
    dist = ((numx-50)**2+(numy-50)**2+(50-numz)**2)**(1/2)
    ponto[0][i] = numx
    ponto[1][i] = numy
    ponto[2][i]= numz
    ponto[3][i] = dist


df = px.data.iris()

fig = px.scatter_3d(df, x = ponto[0], y = ponto[1], z=ponto[2], color=ponto[3])
for template in ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]:
    fig.update_layout(template='plotly_dark')

fig.update_traces(marker=dict(size=1))


fig.show()
