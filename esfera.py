import plotly.express as px
from numpy import arccos, sin, cos, pi, random, array, append



phi = random.uniform(0, 2 * pi,10000)
costheta = random.uniform(-1, 1,10000)
u = random.uniform(0, 1,10000)

theta = array([0]*10000)
r = array([0]*10000)
x = array([0]*10000)
y = array([0]*10000)
z = array([0]*10000)

for i in range(0,10000):  
     theta[i] = arccos(costheta[i])
     r[i] = ( 100 * (u[i]) ** (1 / 3))

     x[i] = ( r[i] * sin(theta[i]) * cos(phi[i]))
     y[i] = ( r[i] * sin(theta[i]) * sin(phi[i]))
     z[i] = (r[i] * cos(theta[i]))
print(theta)
print(costheta)
print(x)

df = px.data.iris()

fig = px.scatter_3d(df, x = x, y = y, z=z, title='Distribuição de pontos em um esfera')
fig.update_traces(marker=dict(size=1))
fig.update_layout(template = 'plotly_dark',scene=dict(xaxis_title="Abscissa", yaxis_title="Ordenada", zaxis_title="Cota"))
fig.show()

