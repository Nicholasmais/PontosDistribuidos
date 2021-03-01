import plotly.express as px
from numpy import random
import plotly.graph_objects as go
from plotly.subplots import make_subplots

x = random.uniform(0,100,10000)
y = random.uniform(0,100,10000)
z = random.uniform(0,100,10000)

yx = [0]*10
yy = [0]*10
yz = [0]*10
eixox = ['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100']

for r in range(0,10):
    tempx = []
    tempy = []
    tempz = []
    for k in range(0,10000):
        
        if x[k] > 10*r and x[k] <= 10*r+10:
            tempx.append(x[k])

        if y[k] > 10*r and y[k] <= 10*r+10:
            tempy.append(y[k])
    
        if z[k] > 10*r and z[k] <= 10*r+10:
            tempz.append(z[k])

    yx[r] = len(tempx)
    yy[r] = len(tempy)
    yz[r] = len(tempz)

df = px.data.iris()

fig = px.scatter_3d(df, x = x, y = y, z=z, title='Distribuição de pontos em um Cubo')
fig.update_traces(marker=dict(size=1))
fig.update_layout(template = 'plotly_dark',scene=dict(xaxis_title="Abscissa", yaxis_title="Ordenada", zaxis_title="Cota"))
fig.show()

plano = make_subplots(specs=[[{"secondary_y": True}]])
plano.update_layout(xaxis_title="Intervalo do eixo", yaxis_title="Quantidade de pontos", yaxis_range = [0,2000])
plano.add_trace(go.Scatter(x=eixox, y=yx, name="Abscissa"),secondary_y=False)
plano.add_trace(go.Scatter(x=eixox, y=yy, name="Ordenada"),secondary_y=False,)
plano.add_trace(go.Scatter(x=eixox, y=yz, name="Cota"),secondary_y=False)
plano.show()

