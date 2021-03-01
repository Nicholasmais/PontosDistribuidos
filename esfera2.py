import plotly.express as px
from numpy import sin, cos, pi, random, arccos, sqrt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

a = 7.7 * 10 ** 20

ani = [i for i in range(10000)]
phi = random.uniform(0, 2 * pi, 10000)
theta = arccos(random.uniform(-1, 1, 10000))
r = a / (sqrt((random.uniform(0, 1, 10000) ** (-2.0 / 3.0) - 1)))

x = (r * sin(theta) * cos(phi))
y = (r * sin(theta) * sin(phi))
z = (r * cos(theta))
R = max(r)

raio = [10 * i for i in range(11)]
mr = [10000 * ((i * .001 * R / a) ** 3 / ((1 + (i * .001 * R / a) ** 2) ** (3 / 2))) for i in range(0, 101)]

yy = [0] * 101
eixox = [f'{i*0.01:.2}%' for i in range (0,101)]

for ra in range(0, 101):
    temp = []
    for k in range(0, 10000):
        if 0.001 * ra * R >= r[k]:
            temp.append(x[k])
    yy[ra] = len(temp)

df = px.data.gapminder()
fig = px.scatter_3d(df, x=x, y=y, z=z, animation_frame=ani, range_x=[0,R], range_y=[0,R], range_z=[0,R])
fig.update_layout(template='plotly_dark')
fig.update_traces(marker=dict(size=1))
fig.show()

