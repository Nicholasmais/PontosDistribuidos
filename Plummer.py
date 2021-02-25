import plotly.express as px
from numpy import  sin, cos, pi, random, arccos, sqrt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

a = 3*3.086*10**(19)

phi = random.uniform(0, 2 * pi,10000)
theta = arccos(random.uniform(-1,1, 10000))
r = a / (sqrt((random.uniform(0, 1,10000)**(-2.0 / 3.0) - 1)))

x = ( r * sin(theta) * cos(phi))
y = ( r * sin(theta) * sin(phi))
z = (r * cos(theta))

df = px.data.gapminder()
fig = px.scatter_3d(df, x = x, y = y, z=z)

fig.update_layout(template='plotly_dark')
fig.update_traces(marker=dict(size=1))

fig.show()

plano = make_subplots(specs=[[{"secondary_y": True}]])

plano.update_layout(xaxis_title="Porcentagem do raio", yaxis_title="Quantidade de pontos")

yy = [0]*10
eixox = ['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100']
R = max(r)

for ra in range(0, 10):
     temp = []
     for k in range(0, 10000):
          if ra/100 * R + .1*R >= r[k] > ra/100 * R:
               temp.append(x[k])

     yy[ra] = len(temp)


func = [0,0,0,0,0,0,0,0,0,0]

for i in range(0,10):
     func[i] = (i/a)**3 / ((1+(r/a)**2 )**3/2) * 10**5

plano.add_trace(go.Scatter(x=eixox, y=yy, name="Pontos"),secondary_y=False)
plano.add_trace(go.Scatter(x=eixox, y=func, name="Função"),secondary_y=False,)

plano.show()
