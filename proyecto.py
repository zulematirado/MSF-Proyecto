"""
Práctica: Sistema Respiratorio

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Ibarra Monroy Ivana Valeria
Número de control: 23210709
Correo institucional: l23210709@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""

import numpy as np
import math as m
import control as ctrl
import matplotlib.pyplot as plt

x0, t0, tend, dt, w, h = 0, 0, 12, 1E-3, 10, 5
N_sim = round(tend/dt) + 1
t = np.linspace(t0, tend, N_sim)
f = 0.25
u = 0.5 * (1 - np.cos(2 * m.pi * f * t))

numControl = [0.3, 2]
denControl = [0.0192, 0.2968, 1.578, 3.72, 4.5]
sysControl = ctrl.tf(numControl, denControl)
print(f"Función de transferencia Control: {sysControl}\n")

numCaso = [0.3, 2]
denCaso = [0.15, 1.985, 7.305, 12.7, 7.5]
sysCaso = ctrl.tf(numCaso, denCaso)
print(f"Función de transferencia Caso: {sysCaso}\n")

polosControl = ctrl.poles(sysControl)
cerosControl = ctrl.zeros(sysControl)

polosCaso = ctrl.poles(sysCaso)
cerosCaso = ctrl.zeros(sysCaso)

print("--- POLOS Y CEROS: CONTROL (PULMÓN SANO) ---")
for i, p in enumerate(polosControl, start=1):
    print(f"  Polo {i}: {p.real:.4f} {p.imag:+.4f}j")
for i, z in enumerate(cerosControl, start=1):
    print(f"  Cero {i}: {z.real:.4f} {z.imag:+.4f}j")
print()

print("--- POLOS Y CEROS: CASO (PULMÓN FIBROSIS) ---")
for i, p in enumerate(polosCaso, start=1):
    print(f"  Polo {i}: {p.real:.4f} {p.imag:+.4f}j")
for i, z in enumerate(cerosCaso, start=1):
    print(f"  Cero {i}: {z.real:.4f} {z.imag:+.4f}j")
print()

Kp, Ki, Kd, Nf = 100000, 0.0761, 99359, 50108
s = ctrl.tf('s')
C_pid = Kp + Ki/s + Kd * (Nf / (1 + Nf/s))
sysTratamiento = ctrl.feedback(ctrl.series(C_pid, sysCaso), 1)

clr1 = np.array([(31, 119, 180)])/255
clr2 = np.array([(237, 177, 32)])/255
clr3 = np.array([(162, 20, 47)])/255
clr4 = np.array([(119, 172, 48)])/255

def openloop(t, sys, u):
    _, Vs = ctrl.forced_response(sys, t, u, x0)
    return Vs

Control = openloop(t, sysControl, u)
Caso = openloop(t, sysCaso, u)
Tratamiento = openloop(t, sysTratamiento, Control)

fg = plt.figure()
fg.set_size_inches(w, h)
fg.set_facecolor('white')

plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.plot(t, u, '-', linewidth=1.5, color=clr1, label='Vs(t)')
plt.plot(t, Control, '-', linewidth=1.5, color=clr2, label='Control (pulmón sano)')
plt.plot(t, Caso, '-', linewidth=1.5, color=clr3, label='Caso (pulmón fibrosis)')
plt.plot(t, Tratamiento, '--', linewidth=1.8, color=clr4, label='Tratamiento (PID)')
plt.xlim(-0.09, 12); plt.xticks(np.arange(0, 13, 2))
plt.grid(True)
plt.xlabel('t [s]')
plt.ylabel('Amplitud')
plt.legend(bbox_to_anchor=(0.5, 1.02), loc='lower center', ncol=2, frameon=True)
fg.savefig('graficaRespiratorio.pdf', bbox_inches='tight')
plt.show()