import plotly.express as px
from numpy import random

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

#cor = sorted(x)
df = px.data.iris()

fig = px.scatter_3d(df, x = x, y = y, z=z, title='Distribuição de pontos em um Cubo')
fig.update_traces(marker=dict(size=1))
fig.update_layout(template = 'plotly_dark',scene=dict(xaxis_title="Abscissa", yaxis_title="Ordenada", zaxis_title="Cota"))
fig.show()

planox = px.line(x=eixox, y=yx, title="Cubo")
planox.update_layout(xaxis_title="Abscissa", yaxis_title="Quantidade de pontos", yaxis_range = [0,2000])
planox.show()

planoy = px.line(x=eixox, y=yy, title="Cubo")
planoy.update_layout(xaxis_title="Ordenada", yaxis_title="Quantidade de pontos", yaxis_range = [0,2000])
planoy.show()

planoz = px.line(x=eixox, y=yz, title="Cubo")
planoz.update_layout(xaxis_title="Cota", yaxis_title="Quantidade de pontos", yaxis_range = [0,2000])
planoz.show()