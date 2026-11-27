[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/)

# Proyecto final: Modelado y control del sistema respiratorio

## Información de las estudiantes

[Agregar nombres, números de control y correos institucionales]

Modelado de Sistemas Fisiológicos (IBF-1020)

Ingeniería Biomédica

## Docente

Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

Se desarrolla un modelo dinámico de cuarto orden del sistema respiratorio mediante cuatro resistencias, dos inductancias y dos capacitancias, considerando además la resistencia interna del primer inductor. Se comparan las condiciones **control (pulmón sano)** y **caso (fibrosis pulmonar)** ante una entrada periódica que representa ciclos respiratorios. Se obtienen las funciones de transferencia, las ecuaciones integrodiferenciales y la representación en espacio de estados. Posteriormente se incorpora un controlador PID filtrado para aproximar la respuesta del caso a la referencia sana. Se emplean MATLAB, Simulink, Python y BioRender para documentar el modelo.

**Palabras clave:** sistema respiratorio · fibrosis pulmonar · mecánica pulmonar · analogía eléctrica · circuito RLC · cuarto orden · resistencia · inductancia · capacitancia · función de transferencia · ecuaciones integrodiferenciales · espacio de estados · control PID · MATLAB · Simulink · Python · BioRender.

## Objetivos

**Objetivo general.** Modelar y comparar la dinámica del pulmón sano y del pulmón con fibrosis, implementando un controlador PID para reducir el error de seguimiento.

**Objetivos específicos**

- Establecer una correspondencia conceptual entre variables fisiológicas y elementos eléctricos.
- Obtener las funciones de transferencia y ecuaciones diferenciales de cuarto orden.
- Analizar estabilidad, respuesta temporal y error estacionario.
- Implementar los modelos en MATLAB/Simulink y Python.
- Comparar las respuestas de entrada, control, caso y tratamiento.
- Documentar la representación anatómica y las evidencias de simulación.

## Descripción detallada del sistema

El sistema respiratorio permite la ventilación pulmonar y el intercambio gaseoso. La fibrosis pulmonar produce cicatrización del tejido y disminución de su distensibilidad, dificultando la expansión pulmonar. En este proyecto se utiliza una analogía eléctrica para estudiar cambios en la respuesta dinámica.

### Figura 1. Biorender

<!-- Pegar aquí la imagen de BioRender -->
<!-- ![Modelo fisiológico](biorender.png) -->

*Figura 01. Comparación anatómica entre pulmón sano y pulmón con fibrosis, con identificación de los elementos eléctricos equivalentes.*

**Nota de interpretación:** las capacitancias son parámetros equivalentes de almacenamiento dinámico. Su incremento numérico en el caso no debe interpretarse como un aumento de la distensibilidad fisiológica real. El modelo es académico y no está validado clínicamente.

## Modelo eléctrico

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

### Figura 2. Circuitos en simulink

<!-- Pegar captura de los circuitos RLC -->

*Figura 02. Circuitos equivalentes de control y caso.*

## Análisis matemático completo

### 1. Variables, nodos y condiciones iniciales

Se considera la topología equivalente utilizada para obtener los coeficientes corregidos: fuente Ve, resistencia R1 y L1 con resistencia interna en serie hasta el nodo Va; C1 entre Va y tierra; R2 entre Va y Vb; rama L2–R3 entre Vb y tierra; R4 entre Vb y Vs; C2 entre Vs y tierra. La salida se mide sobre C2. Se define Ra = R1 + rL1 = 1.5 Ω. Las corrientes i1, i2 e i3 corresponden a las ramas de L1, L2 y R4, respectivamente. Los voltajes iniciales de los capacitores y las corrientes iniciales de los inductores son nulos.

### 2. Leyes de Kirchhoff y ecuaciones integrodiferenciales físicas

$$
 i_1=C_1\dot V_a+i_2+i_3,\qquad i_3=C_2\dot V_s
$$

$$
 V_e=R_ai_1+L_1\dot i_1+V_a
$$

$$
 V_a-V_b=R_2(i_2+i_3),\qquad V_b=L_2\dot i_2+R_3i_2=R_4i_3+V_s
$$

Con condiciones iniciales nulas:

$$
 V_a(t)=\frac1{C_1}\int_0^t(i_1-i_2-i_3)\,d\tau,\qquad V_s(t)=\frac1{C_2}\int_0^t i_3\,d\tau
$$

$$
 i_1(t)=\frac1{L_1}\int_0^t(V_e-R_ai_1-V_a)\,d\tau,\qquad i_2(t)=\frac1{L_2}\int_0^t(V_b-R_3i_2)\,d\tau
$$

El nodo intermedio se obtiene eliminando i3:

$$
 V_b=\frac{R_4V_a-R_2R_4i_2+R_2V_s}{R_2+R_4},\qquad i_3=\frac{V_a-V_s-R_2i_2}{R_2+R_4}
$$

### 3. Transformada de Laplace

$$
 Z_1=R_a+L_1s,\quad Z_2=R_3+L_2s,\quad Z_3=R_4+\frac1{C_2s}
$$

$$
 \frac{V_e-V_a}{Z_1}=C_1sV_a+\frac{V_a-V_b}{R_2}
$$

$$
 \frac{V_a-V_b}{R_2}=V_b\left(\frac1{Z_2}+\frac1{Z_3}\right)=V_bY
$$

Despejando y sustituyendo:

$$
 V_a=V_b(1+R_2Y)
$$

$$
 V_e=V_b[(1+Z_1C_1s)(1+R_2Y)+Z_1Y]
$$

Por divisor de voltaje, Vs = Vb/(C2 s Z3). Por tanto:

$$
 G(s)=\frac{V_s}{V_e}=\frac{1/(C_2sZ_3)}{(1+Z_1C_1s)(1+R_2Y)+Z_1Y}
$$

### 4. Desarrollo de la función de transferencia general

Se define:

$$
 Q(s)=Z_2(1+R_4C_2s)+R_2[1+C_2s(Z_2+R_4)]
$$

$$
 Q(s)=q_2s^2+q_1s+q_0
$$

$$
 q_0=R_3+R_2,\quad q_1=L_2+C_2(R_3R_4+R_2R_3+R_2R_4),\quad q_2=L_2C_2(R_4+R_2)
$$

Multiplicando numerador y denominador por Z2(1+R4 C2 s):

$$
 G(s)=\frac{L_2s+R_3}{(1+Z_1C_1s)Q(s)+Z_1[1+C_2s(Z_2+R_4)]}
$$

Expandiendo y agrupando potencias:

$$
 \boxed{G(s)=\frac{b_1s+b_0}{a_4s^4+a_3s^3+a_2s^2+a_1s+a_0}}
$$

$$
 \begin{aligned}
 a_4&=L_1C_1q_2\\
 a_3&=R_aC_1q_2+L_1C_1q_1+L_1L_2C_2\\
 a_2&=q_2+R_aC_1q_1+L_1C_1q_0+R_aL_2C_2+L_1C_2(R_3+R_4)\\
 a_1&=q_1+R_aC_1q_0+R_aC_2(R_3+R_4)+L_1\\
 a_0&=q_0+R_a\\
 b_1&=L_2,\qquad b_0=R_3
 \end{aligned}
$$

### 5. Función de transferencia del control (pulmón sano)

$$
 q_0=2+1=3,\quad q_1=0.3+0.16(2+2+1)=1.1,\quad q_2=0.3(0.16)(1+1)=0.096
$$

$$
 \begin{aligned}
 a_4&=1(0.2)(0.096)=0.0192\\
 a_3&=0.0288+0.22+0.048=0.2968\\
 a_2&=0.096+0.33+0.6+0.072+0.48=1.578\\
 a_1&=1.1+0.9+0.72+1=3.72\\
 a_0&=3+1.5=4.5
 \end{aligned}
$$

$$
 \boxed{G_s(s)=\frac{0.3s+2}{0.0192s^4+0.2968s^3+1.578s^2+3.72s+4.5}}
$$

### 6. Función de transferencia del caso (fibrosis)

$$
 q_0=2+4=6,\quad q_1=0.3+0.4(2+8+4)=5.9,\quad q_2=0.3(0.4)(1+4)=0.6
$$

$$
 \begin{aligned}
 a_4&=0.5(0.5)(0.6)=0.15\\
 a_3&=0.45+1.475+0.06=1.985\\
 a_2&=0.6+4.425+1.5+0.18+0.6=7.305\\
 a_1&=5.9+4.5+1.8+0.5=12.7\\
 a_0&=6+1.5=7.5
 \end{aligned}
$$

$$
 \boxed{G_f(s)=\frac{0.3s+2}{0.15s^4+1.985s^3+7.305s^2+12.7s+7.5}}
$$

### 7. Ecuaciones diferenciales de cuarto orden

Multiplicando en cruz la función general y aplicando Laplace inversa:

$$
 a_4V_s^{(4)}+a_3V_s^{(3)}+a_2\ddot V_s+a_1\dot V_s+a_0V_s=b_1\dot V_e+b_0V_e
$$

**Control:**

$$
 0.0192V_s^{(4)}+0.2968V_s^{(3)}+1.578\ddot V_s+3.72\dot V_s+4.5V_s=0.3\dot V_e+2V_e
$$

**Caso:**

$$
 0.15V_s^{(4)}+1.985V_s^{(3)}+7.305\ddot V_s+12.7\dot V_s+7.5V_s=0.3\dot V_e+2V_e
$$

### 8. Realización mediante integradores y espacio de estados

Para evitar derivar la entrada se define X(s)=Ve(s)/D(s), donde D(s) es el denominador de cada planta. Entonces Vs(s)=(0.3s+2)X(s). Sean x1=x, x2=dx/dt, x3=d²x/dt² y x4=d³x/dt³.

$$
 \dot x_4=\frac{V_e-a_3x_4-a_2x_3-a_1x_2-a_0x_1}{a_4}
$$

$$
 x_4=\int_0^t\dot x_4\,d\tau,\quad x_3=\int_0^t x_4\,d\tau,\quad x_2=\int_0^t x_3\,d\tau,\quad x_1=\int_0^t x_2\,d\tau
$$

$$
 \boxed{V_s=0.3x_2+2x_1}
$$

**Control:**

$$
 \dot x_4=\frac{V_e-0.2968x_4-1.578x_3-3.72x_2-4.5x_1}{0.0192}
$$

**Caso:**

$$
 \dot x_4=\frac{V_e-1.985x_4-7.305x_3-12.7x_2-7.5x_1}{0.15}
$$

Cada planta tiene estados independientes. La representación matricial es:

$$
 \dot{\mathbf x}=A\mathbf x+BV_e,\qquad V_s=C\mathbf x+DV_e
$$

$$
 A_s=\begin{bmatrix}0&1&0&0\\0&0&1&0\\0&0&0&1\\-234.375&-193.75&-82.1875&-15.458333\end{bmatrix},\quad B_s=\begin{bmatrix}0\\0\\0\\52.083333\end{bmatrix}
$$

$$
 A_f=\begin{bmatrix}0&1&0&0\\0&0&1&0\\0&0&0&1\\-50&-84.666667&-48.7&-13.233333\end{bmatrix},\quad B_f=\begin{bmatrix}0\\0\\0\\6.666667\end{bmatrix}
$$

$$
 C_s=C_f=\begin{bmatrix}2&0.3&0&0\end{bmatrix},\qquad D_s=D_f=0
$$

### Figura 3. Ecuaciones integrodiferenciales

<!-- ![Bloques de integradores](integradores.png) -->

## Análisis dinámico y error en estado estacionario

### 9. Error en lazo abierto ante escalón unitario

$$
 V_e(s)=\frac1s,\qquad V_s(s)=G(s)V_e(s)
$$

$$
 E(s)=V_e(s)-V_s(s)=\frac{1-G(s)}s
$$

Por el teorema del valor final, para plantas estables:

$$
 e_{ss}=\lim_{s\to0}sE(s)=1-G(0)=1-\frac{R_3}{R_a+R_2+R_3}
$$

**Control:**

$$
 V_{s,sano}(\infty)=\frac2{4.5}=\frac{4}{9}\approx0.444444
$$

$$
 \boxed{e_{ss,sano}=1-\frac{4}{9}=\frac{5}{9}\approx0.555556}
$$

El error del control equivale al 55.5556 % de la entrada.

**Caso:**

$$
 V_{s,fibrosis}(\infty)=\frac2{7.5}=\frac{4}{15}\approx0.266667
$$

$$
 \boxed{e_{ss,fibrosis}=1-\frac{4}{15}=\frac{11}{15}\approx0.733333}
$$

El error del caso equivale al 73.3333 % de la entrada.

**Diferencia entre control y caso:**

$$
 e_{ref}(\infty)=\frac{4}{9}-\frac{4}{15}=\frac{8}{45}\approx0.177778
$$

$$
 \frac{8/45}{4/9}(100)=\boxed{40\%}
$$

El 40 % es la reducción de ganancia estática respecto al pulmón sano, no el error porcentual respecto a la entrada ni la reducción de amplitud de la señal periódica.

### 10. Polos, ceros y estabilidad

Los polos son las raíces del denominador de cuarto orden. El cero común es:

$$
 0.3s+2=0\quad\Rightarrow\quad z=-6.666667
$$

**Control:**

| Polo | Valor (s⁻¹) |
|:--|--:|
| p1 | -6.921898+0.000000j |
| p2 | -5.431294+0.000000j |
| p3 | -1.552571+1.955442j |
| p4 | -1.552571-1.955442j |

Constante de tiempo dominante aproximada: 0.644093 s.

**Caso:**

| Polo | Valor (s⁻¹) |
|:--|--:|
| p1 | -8.662984+0.000000j |
| p2 | -1.743871+1.513340j |
| p3 | -1.743871-1.513340j |
| p4 | -1.082607+0.000000j |

Constante de tiempo dominante aproximada: 0.923697 s.

Todos los polos tienen parte real negativa; las dos plantas son asintóticamente estables. La presencia de polos complejos impide clasificarlas simplemente como sistemas sobreamortiguados de segundo orden.

### 11. Señal de entrada y respuesta periódica

$$
 T=4\ \mathrm{s},\qquad f=1/T=0.25\ \mathrm{Hz},\qquad \omega=2\pi f=\pi/2
$$

$$
 V_e(t)=0.5-0.5\cos(\pi t/2)
$$

$$
 V_e(s)=\frac{0.5}{s}-\frac{0.5s}{s^2+\pi^2/4}=\frac{\pi^2}{2s(4s^2+\pi^2)}
$$

La frecuencia equivalente es 15 respiraciones/min y se simulan tres ciclos en 12 s. Para una planta estable, la respuesta periódica después del transitorio es:

$$
 V_s(t)\approx0.5G(0)-0.5|G(j\omega)|\cos(\omega t+\arg G(j\omega))
$$

- **Control:** magnitud 0.432724, fase -67.980°, componente continua 0.222222.
- **Caso:** magnitud 0.131928, fase -114.846°, componente continua 0.133333.

La respuesta periódica no converge a un valor constante; por eso el error estacionario de escalón y el error de seguimiento periódico se analizan por separado.

## Simulación en MATLAB y Simulink

**Configuración:** entrada sinusoidal desplazada, intervalo de 0 a 12 s, solver `ode15s` y paso máximo de `1e-3` s.

### Figura 4. Scope de simulink

<!-- Pegar captura de las seis señales del Scope -->

*Figura 04. Comparación de la entrada, los circuitos RLC, las ecuaciones integrodiferenciales y el tratamiento PID.*

### Figura 5. Cuadernillo matlab

<!-- Pegar gráfica de las cuatro señales del cuadernillo -->

*Figura 05. Entrada, control, caso y tratamiento PID.*

## Controlador PID

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

### Desarrollo algebraico del controlador y del error

$$
 C(s)=\frac{(K_p+K_dN)s^2+(K_pN+K_i)s+K_iN}{s(s+N)}
$$

Con las ganancias redondeadas:

$$
 P(s)=4978780772s^2+5010800000.0761s+3813.2188
$$

$$
 Q_{PID}(s)=s^2+50108s,\qquad C(s)=P(s)/Q_{PID}(s)
$$

Definiendo F(s)=0.15s⁴+1.985s³+7.305s²+12.7s+7.5:

$$
 T(s)=\frac{P(s)(0.3s+2)}{Q_{PID}(s)F(s)+P(s)(0.3s+2)}
$$

La referencia R(s)=Gs(s)Ve(s) se compara con la salida tratada. Por retroalimentación negativa unitaria:

$$
 E(s)=R(s)-V_{s,PID}(s)=\frac{R(s)}{1+C(s)G_f(s)}
$$

Para una entrada escalón unitaria al sistema completo, R(s)=Gs(s)/s:

$$
 e_{ss,PID}=\lim_{s\to0}\frac{G_s(s)}{1+C(s)G_f(s)}=0
$$

El resultado es válido para el lazo estable porque Ki es distinto de cero y Gf(0) es finita y no nula. No implica error cero para una referencia sinusoidal.

Para la simulación periódica se utilizan:

$$
 e_{max}=\max_i|V_{s,sano}(t_i)-V_{s,PID}(t_i)|
$$

$$
 RMSE=\sqrt{\frac1n\sum_{i=1}^n[V_{s,sano}(t_i)-V_{s,PID}(t_i)]^2}
$$

Los resultados reportados por la optimización son 0.000017889 y 0.000010703, respectivamente. Frente al error máximo previo de 0.0039:

$$
 \%\text{reducción}=\frac{0.0039-0.000017889}{0.0039}(100)\approx99.54\%
$$

Los errores reportados proceden de la sintonización previa a redondear las ganancias; pueden variar ligeramente con el paso de simulación.

### Figura 6. Controlador pid

<!-- Pegar captura del controlador y lazo cerrado -->

## Verificación en Python

Se utilizan las bibliotecas `numpy`, `math`, `control` y `matplotlib`.

### Figura 7. Gráfica python

<!-- Pegar gráfica de Python -->

*Figura 07. Comparación de las cuatro señales: entrada, control, caso y tratamiento.*

## Resultados y evidencia

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

### Figura 8. Osciloscopio (si aplica)

<!-- Pegar evidencia experimental si se dispone de ella -->

*Figura 08. Evidencia de laboratorio, si está disponible.*

## Conclusión

El circuito eléctrico equivalente permitió representar la dinámica respiratoria mediante un sistema de cuarto orden. La comparación entre control y caso mostró diferencias en la amplitud y dinámica de la respuesta. Las ecuaciones integrodiferenciales permitieron reproducir visualmente las respuestas de los circuitos en Simulink. El controlador PID aproximó la respuesta del caso a la referencia sana con un error de seguimiento reducido en la optimización numérica. MATLAB, Simulink, Python y BioRender complementan el análisis y su interpretación. Los resultados tienen alcance académico y no constituyen una validación clínica ni una propuesta terapéutica para la fibrosis pulmonar.

## Referencias

1. Valle Trujillo, P. A. (2026). *Modelado de Sistemas Fisiológicos (IBF-1020)*. Material de la asignatura, Instituto Tecnológico de Tijuana.
2. [Repositorio académico MSF-IBF1020](https://github.com/DrPaulValle/MSF-IBF1020).
3. [MathWorks — Control System Toolbox](https://www.mathworks.com/products/control.html).
4. [Python Control Systems Library](https://python-control.readthedocs.io/).
