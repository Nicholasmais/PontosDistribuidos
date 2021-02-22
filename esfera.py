import plotly.express as px
from random import uniform
from numpy import arccos, sin, cos, pi

x = y = z = raio = []
ponto = [[0] * 10000, [0] * 10000, [0] * 10000, [0] * 10000]

for i in range(0, 10000):
    phi = uniform(0, 2 * pi)
    costheta = uniform(-1, 1)
    u = uniform(0, 1)

    theta = arccos(costheta)
    r = 100 * (u) ** (1 / 3)

    x = r * sin(theta) * cos(phi)
    y = r * sin(theta) * sin(phi)
    z = r * cos(theta)

    ponto[0][i] = x
    ponto[1][i] = y
    ponto[2][i] = z

    raio.append(r)

    ponto[3][i] = raio[i]

df = px.data.iris()
fig = px.scatter_3d(df, x=ponto[0], y=ponto[1], z=ponto[2], color=ponto[3])
for template in ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]:
    fig.update_layout(template='plotly_dark')

fig.update_traces(marker=dict(size=1))

# fig.show()


numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
volume = [0,0,0,0,0,0,0,0,0,0,0]
densi= [0,0,0,0,0,0,0,0,0,0]
eixox = ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100']

for i in range(0, 10):
    numbers[i] = (sum(j <= i * 10 + 10 for j in ponto[3]))
    volume[i] = 4 / 3 * pi * (i * 10 + 10) ** 3
    densi[i] = numbers[i] / volume[i] * 1000

print(numbers)
print(volume)
print(densi)

plano = px.scatter(x=eixox, y=densi)
plano.update_layout(xaxis_title="Raio", yaxis_title="Densidade de pontos (10^-3)",yaxis_range=[0,5])
plano.show()
