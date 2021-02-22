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
    dist = ((numx)**2+(numy)**2+(numz)**2)**(1/2)
    ponto[0][i] = numx
    ponto[1][i] = numy
    ponto[2][i]= numz
    ponto[3][i] = dist


numbers = [0]*17
volume = [0]*17
densi= [0]*17
eixox = ['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100','100-110','110-120','120-130','130-140','140-150','150-160','160-175']
k = 0
for i in range(0, 17):
    numbers[i] = (sum(j <= i * 10 + 10 for j in ponto[3]))
    volume[i] = (i * 10 + 10) ** 3
    densi[i] = numbers[i] / volume[i] * 1000
    print(numbers[i])

for j in range(0,17):
    if j > 0:
        numbers[j] -= sum(numbers[:j-1])
print(numbers)
df = px.data.iris()

fig = px.scatter_3d(df, x = ponto[0], y = ponto[1], z=ponto[2], color=ponto[3], title='Distribuição de pontos em um Cubo')
for template in ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]:
    fig.update_layout(template='plotly_dark')


fig.update_traces(marker=dict(size=1))
fig.update_layout(scene=dict(xaxis_title="Abscissa", yaxis_title="Ordenada", zaxis_title="Cota"))

fig.show()

plano2 = px.scatter(x=eixox, y=numbers)
plano2.update_layout(xaxis_title="Comprimento", yaxis_title="Quantidade de pontos")
plano2.show()

plano = px.scatter(x=eixox, y=densi)
plano.update_layout(xaxis_title="Comprimento", yaxis_title="Densidade de pontos (10^-3)",yaxis_range=[0,10])
plano.show()

