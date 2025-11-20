# **Problemas de Control PI con Integración Numérica**

---

## **Problema 1: Control PI con integración trapezoidal**

**Sistema:** Control de temperatura en un horno industrial.

**Datos:**
- Temperatura deseada: `T_set = 200 °C`
- Constantes del controlador: `K_p = 2.0`, `K_i = 0.5`
- Intervalo de muestreo: `Δt = 1 s`
- Temperaturas medidas en los primeros 6 segundos:  
  `T = [180, 185, 190, 192, 195, 197] °C`

**Ecuación del controlador:**
```math
u(t) = K_p e(t) + K_i ∫₀ᵗ e(τ) dτ
```
Donde:
```math
e(t) = T_set - T(t)
```

**Tarea:**
Calcular la acción integral usando la **regla trapezoidal** para los errores en cada segundo y determinar la señal de control `u(t)` en el instante `t = 6 s`.

---

## **Problema 2: Control PI con integración de Simpson**

**Sistema:** Control de nivel en un tanque.

**Datos:**
- Nivel deseado: `L_set = 5 m`
- Constantes del controlador: `K_p = 1.5`, `K_i = 0.8`
- Intervalo de muestreo: `Δt = 2 s`
- Niveles medidos en los primeros 6 intervalos (0 a 12 s):  
  `L = [4.2, 4.4, 4.6, 4.7, 4.8, 4.9, 5.0] m`

**Ecuación del controlador:**
```math
u(t) = K_p e(t) + K_i ∫₀ᵗ e(τ) dτ
```
Donde:
```math
e(t) = L_set - L(t)
```

**Tarea:**
Calcular la acción integral usando la **regla de Simpson** para los errores en los intervalos y determinar la señal de control `u(t)` en el instante `t = 12 s`.

---

> **Nota:** No se deben mostrar resultados numéricos, solo el planteamiento y los datos.
