import plotly.express as px
from numpy import sin, cos, pi, random, arccos
import plotly.graph_objects as go
from plotly.subplots import make_subplots

phi = random.uniform(0, 2 * pi, 10000)
costheta = random.uniform(-1, 1, 10000)
theta = arccos(costheta)
u = random.uniform(0, 1, 10000)

R = 100
r = (R * (u) ** (1 / 3))
x = (r * sin(theta) * cos(phi))
y = (r * sin(theta) * sin(phi))
z = (r * cos(theta))

raio = [10 * i for i in range(11)]
mr = [10000 * (raio[i] / R) ** 3 for i in range(0, 11)]

yy = [0] * 11
eixox = ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100']

for ra in range(0, 11):
    temp = []
    for k in range(0, 10000):
        if 10 * ra >= r[k]:
            temp.append(x[k])
    yy[ra] = len(temp)

df = px.data.iris()

fig = px.scatter_3d(df, x=x, y=y, z=z, title='Distribuição de pontos em um esfera')
fig.update_traces(marker=dict(size=1))
fig.update_layout(template='plotly_dark',
                  scene=dict(xaxis_title="Abscissa", yaxis_title="Ordenada", zaxis_title="Cota"))
fig.show()

plano = make_subplots(specs=[[{"secondary_y": True}]])
plano.update_layout(title='Esfera', xaxis_title="Raio", yaxis_title="Quantidade de pontos")
plano.add_trace(go.Scatter(x=eixox, y=yy, name="Pontos"), secondary_y=False)
plano.add_trace(go.Scatter(x=eixox, y=mr, name="Função"), secondary_y=False, )
plano.show()
