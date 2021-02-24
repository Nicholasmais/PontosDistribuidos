import plotly.express as px
from numpy import  sin, cos, pi, random, array

phi = random.uniform(0, 2 * pi,5000)
theta = random.uniform(0,pi,5000)
u = random.uniform(0, 1,5000)

r = array([0]*5000)
x = array([0]*5000)
y = array([0]*5000)
z = array([0]*5000)

for i in range(0,5000):
     r[i] = ( 100 * (u[i]) ** (1 / 3))

     x[i] = ( r[i] * sin(theta[i]) * cos(phi[i]))
     y[i] = ( r[i] * sin(theta[i]) * sin(phi[i]))
     z[i] = (r[i] * cos(theta[i]))

yy = [0]*10
eixox = ['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100']


for ra in range(0, 10):
     temp = []
     for k in range(0, 5000):
          if 10 * ra + 10 >= r[k] > 10 * ra:
               temp.append(x[k])
     yy[ra] = len(temp)

df = px.data.iris()

fig = px.scatter_3d(df, x = x, y = y, z=z, title='Distribuição de pontos em um esfera')
fig.update_traces(marker=dict(size=1))
fig.update_layout(template = 'plotly_dark',scene=dict(xaxis_title="Abscissa", yaxis_title="Ordenada", zaxis_title="Cota"))
fig.show()


plano = px.line(x=eixox, y=yy, title="Esfera")
plano.update_layout(xaxis_title="Raio", yaxis_title="Quantidade de pontos", yaxis_range = [0,3000])
plano.show()

print(sum(yy))