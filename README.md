

<div align="center">

# 🫁 MODELADO Y CONTROL DEL SISTEMA RESPIRATORIO

### PROYECTO FINAL · MODELADO DE SISTEMAS FISIOLÓGICOS

**INGENIERÍA BIOMÉDICA · TECNM / INSTITUTO TECNOLÓGICO DE TIJUANA**

![MATLAB](https://img.shields.io/badge/MATLAB-Simulink-0076A8?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-Control-3776AB?style=for-the-badge) ![PID](https://img.shields.io/badge/Control-PID-1F2937?style=for-the-badge) ![Status](https://img.shields.io/badge/Proyecto-Académico-64748B?style=for-the-badge)

*Dinámica respiratoria · Analogía eléctrica · Sistemas de cuarto orden · Control retroalimentado*

</div>

---

## 01 / FICHA DEL PROYECTO

| Campo | Información |
|:--|:--|
| **Estudiante(s)** | Ivana Valeria Ibarra Monroy
                      Maria Luisa Michelle Muñoz Meneses
                      Zulema Guadalupe Tirado Manzo|
| **Número(s) de control** | 23210709 
                             23210714
                             23210724|
| **Asignatura** | Modelado de Sistemas Fisiológicos (IBF-1020) |
| **Docente** | Dr. Paul Antonio Valle Trujillo |
| **Institución** | Tecnológico Nacional de México · Instituto Tecnológico de Tijuana |
| **Programa** | Ingeniería Biomédica |
| **Ubicación** | Tijuana, Baja California, México |
| **Proyecto** | Modelado y control del sistema respiratorio |

> **Objetivo central:** representar la dinámica pulmonar mediante un circuito eléctrico RLC equivalente, comparar un pulmón sano con un pulmón con fibrosis y evaluar la compensación mediante un controlador PID.

## 02 / RESUMEN EJECUTIVO

Se desarrolla un modelo dinámico de cuarto orden del sistema respiratorio mediante cuatro resistencias, dos inductancias y dos capacitancias, considerando además la resistencia interna del primer inductor. Se comparan las condiciones **control (pulmón sano)** y **caso (fibrosis pulmonar)** ante una entrada periódica que representa ciclos respiratorios. Se obtienen las funciones de transferencia, las ecuaciones integrodiferenciales y la representación en espacio de estados. Posteriormente se incorpora un controlador PID filtrado para aproximar la respuesta del caso a la referencia sana. Se emplean MATLAB, Simulink, Python y BioRender para documentar el modelo.

**Palabras clave:** sistema respiratorio · fibrosis pulmonar · mecánica pulmonar · analogía eléctrica

## 03 / OBJETIVOS Y ALCANCE

**Objetivo general.** Modelar y comparar la dinámica del pulmón sano y del pulmón con fibrosis, implementando un controlador PID para reducir el error de seguimiento.

**Objetivos específicos**

- Establecer una correspondencia conceptual entre variables fisiológicas y elementos eléctricos.
- Obtener las funciones de transferencia y ecuaciones diferenciales de cuarto orden.
- Analizar estabilidad, respuesta temporal y error estacionario.
- Implementar los modelos en MATLAB/Simulink y Python.
- Comparar las respuestas de entrada, control, caso y tratamiento.
- Documentar la representación anatómica y las evidencias de simulación.

## 04 / ARQUITECTURA FISIOLÓGICA

El sistema respiratorio permite la ventilación pulmonar y el intercambio gaseoso. La fibrosis pulmonar produce cicatrización del tejido y disminución de su distensibilidad, dificultando la expansión pulmonar. En este proyecto se utiliza una analogía eléctrica para estudiar cambios en la respuesta dinámica.

### ESPACIO PARA FIGURA 01 · BIORENDER

<img width="720" height="504" alt="WhatsApp Image 2026-11-26 at 1 53 07 PM" src="https://github.com/user-attachments/assets/7fdbe980-4677-4f30-b7cc-be65ed8bff34" />


*Figura 01. Comparación anatómica entre pulmón sano y pulmón con fibrosis, con identificación de los elementos eléctricos equivalentes.*

**Nota de interpretación:** las capacitancias son parámetros equivalentes de almacenamiento dinámico. Su incremento numérico en el caso no debe interpretarse como un aumento de la distensibilidad fisiológica real. El modelo es académico y no está validado clínicamente.

## 05 / MODELO ELÉCTRICO

| Variable | Interpretación simplificada |
|:--|:--|
| `Ve(t)` | Estímulo ventilatorio de entrada |
| `R1`, `R2`, `R3`, `R4` | Oposición al flujo y pérdidas resistivas equivalentes |
| `L1`, `L2` | Inercia equivalente del aire |
| `C1`, `C2` | Almacenamiento elástico equivalente |
| `Vs(t)` | Respuesta pulmonar normalizada |

### Parámetros de simulación

| Parámetro | CONTROL | CASO |
|:--|--:|--:|
| R₁ (Ω) | 1 | 1 |
| R₂ (Ω) | 1 | 4 |
| R₃ (Ω) | 2 | 2 |
| R₄ (Ω) | 1 | 1 |
| L₁ (H) | 1 | 0.5 |
| L₂ (H) | 0.3 | 0.3 |
| C₁ (F) | 0.2 | 0.5 |
| C₂ (F) | 0.16 | 0.4 |
| Resistencia interna de L₁ (Ω) | 0.5 | 0.5 |

### ESPACIO PARA FIGURA 02 · CIRCUITOS EN SIMULINK



*Figura 02. Circuitos equivalentes de control y caso.*

## 06 / FORMULACIÓN MATEMÁTICA

### Función de transferencia general

$$
G(s)=\frac{V_s(s)}{V_e(s)}=\frac{b_1s+b_0}{a_4s^4+a_3s^3+a_2s^2+a_1s+a_0}
$$

**Condición control:**

$$
G_s(s)=\frac{0.3s+2}{0.0192s^4+0.2968s^3+1.578s^2+3.72s+4.5}
$$

**Condición caso:**

$$
G_f(s)=\frac{0.3s+2}{0.15s^4+1.985s^3+7.305s^2+12.7s+7.5}
$$

### Ecuaciones diferenciales

$$
0.0192V_s^{(4)}+0.2968V_s^{(3)}+1.578\ddot V_s+3.72\dot V_s+4.5V_s=0.3\dot V_e+2V_e
$$

$$
0.15V_s^{(4)}+1.985V_s^{(3)}+7.305\ddot V_s+12.7\dot V_s+7.5V_s=0.3\dot V_e+2V_e
$$

### Ecuaciones integrodiferenciales y espacio de estados

Con una variable auxiliar $x$ y condiciones iniciales nulas:

$$
\dot x_1=x_2,\quad \dot x_2=x_3,\quad \dot x_3=x_4
$$

$$
\dot x_{4,s}=\frac{V_e-0.2968x_4-1.578x_3-3.72x_2-4.5x_1}{0.0192}
$$

$$
\dot x_{4,f}=\frac{V_e-1.985x_4-7.305x_3-12.7x_2-7.5x_1}{0.15}
$$

$$
V_s=0.3x_2+2x_1
$$

Cada modelo utiliza su propio vector de estados.

### ESPACIO PARA FIGURA 03 · ECUACIONES INTEGRODIFERENCIALES

<!-- Pegar captura de los bloques de integradores -->

## 07 / ANÁLISIS DINÁMICO

Para una entrada escalón unitario, la ganancia de continua de cada planta determina su respuesta estacionaria:

$$
V_{s,control}(\infty)=\frac{2}{4.5}=0.44444
$$

$$
V_{s,caso}(\infty)=\frac{2}{7.5}=0.26667
$$

$$
e_{ss,control}=0.55556,\qquad e_{ss,caso}=0.73333
$$

La disminución relativa de la ganancia estacionaria del caso respecto al control es del 40 %. Estos valores corresponden al escalón unitario, no a los máximos de la señal periódica.

### Señal de entrada respiratoria

$$
V_e(t)=0.5-0.5\cos\left(\frac{\pi}{2}t\right)
$$

La frecuencia es de 0.25 Hz, equivalente a 15 respiraciones por minuto, con un periodo de 4 s y tres ciclos durante 12 s de simulación.

## 08 / SIMULACIÓN EN MATLAB Y SIMULINK

**Configuración:** entrada sinusoidal desplazada, intervalo de 0 a 12 s, solver `ode15s` y paso máximo de `1e-3` s.

```matlab
clc; clear; close all;
warning('off','all')
modelo = 'Proyecto1';
open_system(modelo)
parameters.StopTime = '12';
parameters.Solver = 'ode15s';
parameters.MaxStep = '1e-3';
parameters.ReturnWorkspaceOutputs = 'on';
x = sim(modelo,parameters);
```

### ESPACIO PARA FIGURA 04 · SCOPE DE SIMULINK

<!-- Pegar captura de las seis señales del Scope -->

*Figura 04. Comparación de la entrada, los circuitos RLC, las ecuaciones integrodiferenciales y el tratamiento PID.*

### ESPACIO PARA FIGURA 05 · CUADERNILLO MATLAB

<!-- Pegar gráfica de las cuatro señales del cuadernillo -->

*Figura 05. Entrada, control, caso y tratamiento PID.*

## 09 / DISEÑO DEL CONTROLADOR PID

La respuesta del pulmón sano se utiliza como referencia del tratamiento:

$$
e(t)=V_{s,control}(t)-V_{s,PID}(t)
$$

$$
C(s)=K_p+\frac{K_i}{s}+K_d\frac{Ns}{s+N}
$$

| Ganancia | Valor empleado |
|:--|--:|
| Proporcional `Kp` | 100000 |
| Integral `Ki` | 0.0761 |
| Derivativa `Kd` | 99359 |
| Filtro derivativo `N` | 50108 |

La función de transferencia del lazo cerrado respecto a la referencia es:

$$
T(s)=\frac{C(s)G_f(s)}{1+C(s)G_f(s)}
$$

$$
\frac{V_{s,PID}(s)}{V_e(s)}=G_s(s)T(s)
$$

Para una referencia constante y un lazo estable, la acción integral permite obtener un error estacionario teórico nulo. Para la referencia periódica permanece un pequeño error de seguimiento.

### ESPACIO PARA FIGURA 06 · CONTROLADOR PID

<!-- Pegar captura del controlador y lazo cerrado -->

## 10 / VERIFICACIÓN EN PYTHON

Se utilizan las bibliotecas `numpy`, `math`, `control` y `matplotlib`.

```python
import numpy as np
import control as ctrl

sysControl = ctrl.tf([0.3, 2], [0.0192, 0.2968, 1.578, 3.72, 4.5])
sysCaso = ctrl.tf([0.3, 2], [0.15, 1.985, 7.305, 12.7, 7.5])
Kp, Ki, Kd, Nf = 100000, 0.0761, 99359, 50108
s = ctrl.tf('s')
C_pid = Kp + Ki/s + Kd*Nf*s/(s+Nf)
sysTratamiento = ctrl.feedback(ctrl.series(C_pid, sysCaso), 1)
t = np.linspace(0, 12, 12001)
u = 0.5*(1-np.cos(2*np.pi*0.25*t))
_, Control = ctrl.forced_response(sysControl, t, u)
_, Caso = ctrl.forced_response(sysCaso, t, u)
_, Tratamiento = ctrl.forced_response(sysTratamiento, t, Control)
```

### ESPACIO PARA FIGURA 07 · GRÁFICA PYTHON

<!-- Pegar gráfica de Python -->

*Figura 07. Comparación de las cuatro señales: entrada, control, caso y tratamiento.*

## 11 / RESULTADOS Y EVIDENCIA

| Escenario | Resultado del modelo |
|:--|:--|
| Entrada | Tres ciclos de amplitud entre 0 y 1 |
| Control | Respuesta de referencia del pulmón sano |
| Caso | Respuesta de menor amplitud |
| Ecuaciones integrodiferenciales | Superposición visual con los circuitos correspondientes |
| Tratamiento PID | Aproximación visual a la respuesta del control |

### Indicadores de seguimiento reportados en MATLAB

| Indicador | Resultado |
|:--|--:|
| Error máximo absoluto | 1.7889 × 10⁻⁵ |
| RMSE | 1.0703 × 10⁻⁵ |

Los indicadores corresponden a la optimización numérica reportada, no a una medición experimental. Las ganancias elevadas requieren una evaluación adicional de robustez, ruido y saturación antes de considerar una implementación física.

### ESPACIO PARA FIGURA 08 · OSCILOSCOPIO (SI APLICA)

<!-- Pegar evidencia experimental si se dispone de ella -->

*Figura 08. Evidencia de laboratorio, si está disponible.*

## 12 / CONCLUSIONES

El circuito eléctrico equivalente permitió representar la dinámica respiratoria mediante un sistema de cuarto orden. La comparación entre control y caso mostró diferencias en la amplitud y dinámica de la respuesta. Las ecuaciones integrodiferenciales permitieron reproducir visualmente las respuestas de los circuitos en Simulink. El controlador PID aproximó la respuesta del caso a la referencia sana con un error de seguimiento reducido en la optimización numérica. MATLAB, Simulink, Python y BioRender complementan el análisis y su interpretación. Los resultados tienen alcance académico y no constituyen una validación clínica ni una propuesta terapéutica para la fibrosis pulmonar.

## 13 / REFERENCIAS

1. Valle Trujillo, P. A. (2026). *Modelado de Sistemas Fisiológicos (IBF-1020)*. Material de la asignatura, Instituto Tecnológico de Tijuana.
2. [Repositorio académico MSF-IBF1020](https://github.com/DrPaulValle/MSF-IBF1020).
3. [MathWorks — Control System Toolbox](https://www.mathworks.com/products/control.html).
4. [Python Control Systems Library](https://python-control.readthedocs.io/).

---

<div align="center">

**MODELADO DE SISTEMAS FISIOLÓGICOS · PROYECTO FINAL**

*Ingeniería Biomédica · Instituto Tecnológico de Tijuana*

</div>
