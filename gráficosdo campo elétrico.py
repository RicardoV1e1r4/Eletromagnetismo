import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# range da distância
R = np.linspace(0, 60, 100)

# Valores das cargas (Coulombs)
Qa = 0.002
Qb = 0.004

# Valores iniciais dos raios (metros)
a = 10
b = 30


def densidadecampoeletrico(Q, R, const=False):
    if const == False:
        epsilon0 = 1
    else:
        epsilon0 = 8.854 * 10 ** (-12)
    k = 1 / (4 * np.pi * epsilon0)
    densidade = k * Q / (R ** 2)
    return densidade


# Lista que vai armazenar os valores de densidades
def PreencheDensidade(a, b, const=False):
    Dr = []
    for i in R:
        if a < b:
            if i < a:
                Dr.append(0)
            elif i <= b:
                Dr.append(densidadecampoeletrico(Qa, i, const))
            else:
                Dr.append(densidadecampoeletrico(Qa + Qb, i, const))
        else:
            if i < b:
                Dr.append(0)
            elif i <= a:
                Dr.append(densidadecampoeletrico(Qb, i, const))
            else:
                Dr.append(densidadecampoeletrico(Qa + Qb, i, const))
    return np.array(Dr)


figura, (eixo1, eixo2) = plt.subplots(2, 1, figsize=(7, 7))
plt.subplots_adjust(left=0.2, bottom=0.40, hspace=0.6)  #espaço extra para os botões deslizantes

#configuração do gráfico da densidade
linha1, = eixo1.plot(R, PreencheDensidade(a, b), color='b')
eixo1.set_xlabel('R (m)', size=10)
eixo1.set_ylabel('Dr (C/m)', size=10)
eixo1.set_title('Densidade de carga')
eixo1.set_ylim(0, 5e-6)
eixo1.grid(True)

# Configuração do gráfico do campo elétrico
linha2, = eixo2.plot(R, PreencheDensidade(a, b), color='g')
eixo2.set_xlabel('R (m)', size=10)
eixo2.set_ylabel('E (N/C)', size=10)
eixo2.set_title('Campo elétrico')
eixo2.set_ylim(0, 1e6)
eixo2.grid(True)

###_____BOTÕES DESLIZANTES_____###
#Deslizante 1 - raio da esfera A
eixo1_raioa = plt.axes([0.2, 0.25, 0.65, 0.03])
slider_raioa = Slider(eixo1_raioa, 'Raio A', 0.1, 40, valinit=a)

#Deslizante 2 - raio da esfera B
eixo1_raiob = plt.axes([0.2, 0.18, 0.65, 0.03])
slider_raiob = Slider(eixo1_raiob, 'Raio B', 0.1, 40, valinit=b)


###___Função que vai atualizar o gráfico___###
def atualizar(val):
    raioa = slider_raioa.val
    raiob = slider_raiob.val
    linha1.set_ydata(PreencheDensidade(raioa, raiob))
    linha2.set_ydata(PreencheDensidade(raioa, raiob, True))
    figura.canvas.draw_idle()


# Conecta os slides à função
slider_raioa.on_changed(atualizar)
slider_raiob.on_changed(atualizar)

#plt.tight_layout()
plt.show()
