# Reglas de Asociación - Algoritmo Apriori

## Instrucciones

Considere el siguiente conjunto de elementos:

**I = {Adidas, Jordan, New Balance, Nike, Puma, Reebok, Under Armour}**

**Nota:** Los nombres de los productos deben estar ordenados ascendentemente para la identificación de patrones frecuentes (join).

Generar las reglas de asociación usando el **ALGORITMO APRIORI** y la evaluación de estas considerando los siguientes criterios:

- **Fi = 2**
- **min.sup = 2**
- **min.conf = 75%**

---

## Índice

1. [Datos de Transacciones](#datos-de-transacciones)
2. [Matriz Binaria de Transacciones](#matriz-binaria-de-transacciones)
3. [Algoritmo Apriori](#algoritmo-apriori)
   - [Primera iteración (L1)](#primera-iteración-l1---itemsets-de-1-elemento)
   - [Segunda iteración (L2)](#segunda-iteración-c2---candidatos-de-2-elementos)
   - [Tercera iteración (L3)](#tercera-iteración-c3---candidatos-de-3-elementos)
   - [Cuarta iteración (L4)](#cuarta-iteración-c4---candidatos-de-4-elementos)
   - [Quinta iteración (L5)](#quinta-iteración-c5---candidatos-de-5-elementos)
   - [Resumen de Itemsets Frecuentes](#resumen-de-itemsets-frecuentes)
4. [Generación de Reglas de Asociación](#generación-de-reglas-de-asociación)
   - [Reglas de Itemsets de 2 elementos (L2)](#reglas-de-itemsets-de-2-elementos-l2)
   - [Reglas de Itemsets de 3 elementos (L3)](#reglas-de-itemsets-de-3-elementos-l3)
   - [Reglas de Itemsets de 4 elementos (L4)](#reglas-de-itemsets-de-4-elementos-l4)
5. [Resumen Final de Reglas de Asociación Fuertes](#resumen-final-de-reglas-de-asociación-fuertes)

---

## Datos de Transacciones

| No. | Productos |
| --- | --------- |
| 1 | {Adidas, Jordan, Reebok, Under Armour} |
| 2 | {Nike, Puma, Reebok, Under Armour} |
| 3 | {Adidas, Jordan, New Balance, Nike} |
| 4 | {Adidas, Jordan, Nike, Puma, Under Armour} |
| 5 | {Jordan, Nike, Reebok, Under Armour} |
| 6 | {New Balance, Puma} |
| 7 | {Reebok, Under Armour} |
| 8 | {New Balance, Puma, Reebok, Under Armour} |
| 9 | {Jordan, New Balance, Nike, Puma, Reebok, Under Armour} |
| 10 | {New Balance, Nike, Puma} |

## Matriz Binaria de Transacciones

| Transacción | Adidas | Jordan | Reebok | Under Armour | Nike | Puma | New Balance |
| ----------- | ------ | ------ | ------ | ------------ | ---- | ---- | ----------- |
| 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 2 | 0 | 0 | 1 | 1 | 1 | 1 | 0 |
| 3 | 1 | 1 | 0 | 0 | 1 | 0 | 1 |
| 4 | 1 | 1 | 0 | 1 | 1 | 1 | 0 |
| 5 | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| 6 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 7 | 0 | 0 | 1 | 1 | 0 | 0 | 0 |
| 8 | 0 | 0 | 1 | 1 | 0 | 1 | 1 |
| 9 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |
| 10 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
| **Suma** | **3** | **5** | **6** | **7** | **7** | **6** | **5** |

## Algoritmo Apriori

**Parámetros:**
- min.sup = 2
- min.conf = 75%
- Fi = 2 (soporte mínimo de 2 transacciones)

### Primera iteración (L1 - Itemsets de 1 elemento)

| Producto | Frecuencia | ¿Cumple min.sup? |
| -------- | ---------- | ---------------- |
| Adidas | 3 | ✓ |
| Jordan | 5 | ✓ |
| New Balance | 5 | ✓ |
| Nike | 7 | ✓ |
| Puma | 6 | ✓ |
| Reebok | 6 | ✓ |
| Under Armour | 7 | ✓ |

**Todos los productos cumplen con el soporte mínimo de 2**, por lo que pasan a la siguiente iteración.

### Segunda iteración (C2 - Candidatos de 2 elementos)

Generamos todas las combinaciones de 2 elementos en orden alfabético:

| Itemset | Transacciones | Frecuencia | ¿Cumple min.sup? |
| ------- | ------------- | ---------- | ---------------- |
| {Adidas, Jordan} | 1, 3, 4 | 3 | ✓ |
| {Adidas, New Balance} | 3 | 1 | ✗ |
| {Adidas, Nike} | 3, 4 | 2 | ✓ |
| {Adidas, Puma} | 4 | 1 | ✗ |
| {Adidas, Reebok} | 1 | 1 | ✗ |
| {Adidas, Under Armour} | 1, 4 | 2 | ✓ |
| {Jordan, New Balance} | 3, 9 | 2 | ✓ |
| {Jordan, Nike} | 3, 4, 5, 9 | 4 | ✓ |
| {Jordan, Puma} | 4, 9 | 2 | ✓ |
| {Jordan, Reebok} | 1, 5, 9 | 3 | ✓ |
| {Jordan, Under Armour} | 1, 4, 5, 9 | 4 | ✓ |
| {New Balance, Nike} | 3, 9, 10 | 3 | ✓ |
| {New Balance, Puma} | 6, 8, 9, 10 | 4 | ✓ |
| {New Balance, Reebok} | 8, 9 | 2 | ✓ |
| {New Balance, Under Armour} | 8, 9 | 2 | ✓ |
| {Nike, Puma} | 2, 4, 9, 10 | 4 | ✓ |
| {Nike, Reebok} | 2, 5, 9 | 3 | ✓ |
| {Nike, Under Armour} | 2, 4, 5, 9 | 4 | ✓ |
| {Puma, Reebok} | 2, 8, 9 | 3 | ✓ |
| {Puma, Under Armour} | 2, 4, 8, 9 | 4 | ✓ |
| {Reebok, Under Armour} | 1, 2, 5, 7, 8, 9 | 6 | ✓ |

### L2 - Itemsets frecuentes de 2 elementos

Los siguientes 18 itemsets cumplen con min.sup = 2:

| Itemset | Frecuencia |
| ------- | ---------- |
| {Adidas, Jordan} | 3 |
| {Adidas, Nike} | 2 |
| {Adidas, Under Armour} | 2 |
| {Jordan, New Balance} | 2 |
| {Jordan, Nike} | 4 |
| {Jordan, Puma} | 2 |
| {Jordan, Reebok} | 3 |
| {Jordan, Under Armour} | 4 |
| {New Balance, Nike} | 3 |
| {New Balance, Puma} | 4 |
| {New Balance, Reebok} | 2 |
| {New Balance, Under Armour} | 2 |
| {Nike, Puma} | 4 |
| {Nike, Reebok} | 3 |
| {Nike, Under Armour} | 4 |
| {Puma, Reebok} | 3 |
| {Puma, Under Armour} | 4 |
| {Reebok, Under Armour} | 6 |

### Tercera iteración (C3 - Candidatos de 3 elementos)

Generamos candidatos combinando pares que comparten un elemento común (join):

| Itemset | Transacciones | Frecuencia | ¿Cumple min.sup? |
| ------- | ------------- | ---------- | ---------------- |
| {Adidas, Jordan, Nike} | 3, 4 | 2 | ✓ |
| {Adidas, Jordan, Under Armour} | 1, 4 | 2 | ✓ |
| {Adidas, Nike, Under Armour} | 4 | 1 | ✗ |
| {Jordan, New Balance, Nike} | 3, 9 | 2 | ✓ |
| {Jordan, New Balance, Puma} | 9 | 1 | ✗ |
| {Jordan, New Balance, Reebok} | 9 | 1 | ✗ |
| {Jordan, New Balance, Under Armour} | 9 | 1 | ✗ |
| {Jordan, Nike, Puma} | 4, 9 | 2 | ✓ |
| {Jordan, Nike, Reebok} | 5, 9 | 2 | ✓ |
| {Jordan, Nike, Under Armour} | 4, 5, 9 | 3 | ✓ |
| {Jordan, Puma, Reebok} | 9 | 1 | ✗ |
| {Jordan, Puma, Under Armour} | 4, 9 | 2 | ✓ |
| {Jordan, Reebok, Under Armour} | 1, 5, 9 | 3 | ✓ |
| {New Balance, Nike, Puma} | 9, 10 | 2 | ✓ |
| {New Balance, Nike, Reebok} | 9 | 1 | ✗ |
| {New Balance, Nike, Under Armour} | 9 | 1 | ✗ |
| {New Balance, Puma, Reebok} | 8, 9 | 2 | ✓ |
| {New Balance, Puma, Under Armour} | 8, 9 | 2 | ✓ |
| {New Balance, Reebok, Under Armour} | 8, 9 | 2 | ✓ |
| {Nike, Puma, Reebok} | 2, 9 | 2 | ✓ |
| {Nike, Puma, Under Armour} | 2, 4, 9 | 3 | ✓ |
| {Nike, Reebok, Under Armour} | 2, 5, 9 | 3 | ✓ |
| {Puma, Reebok, Under Armour} | 2, 8, 9 | 3 | ✓ |

### L3 - Itemsets frecuentes de 3 elementos

Los siguientes 16 itemsets cumplen con min.sup = 2:

| Itemset | Frecuencia |
| ------- | ---------- |
| {Adidas, Jordan, Nike} | 2 |
| {Adidas, Jordan, Under Armour} | 2 |
| {Jordan, New Balance, Nike} | 2 |
| {Jordan, Nike, Puma} | 2 |
| {Jordan, Nike, Reebok} | 2 |
| {Jordan, Nike, Under Armour} | 3 |
| {Jordan, Puma, Under Armour} | 2 |
| {Jordan, Reebok, Under Armour} | 3 |
| {New Balance, Nike, Puma} | 2 |
| {New Balance, Puma, Reebok} | 2 |
| {New Balance, Puma, Under Armour} | 2 |
| {New Balance, Reebok, Under Armour} | 2 |
| {Nike, Puma, Reebok} | 2 |
| {Nike, Puma, Under Armour} | 3 |
| {Nike, Reebok, Under Armour} | 3 |
| {Puma, Reebok, Under Armour} | 3 |

### Cuarta iteración (C4 - Candidatos de 4 elementos)

Generamos candidatos combinando tripletas que comparten dos elementos comunes:

| Itemset | Transacciones | Frecuencia | ¿Cumple min.sup? |
| ------- | ------------- | ---------- | ---------------- |
| {Adidas, Jordan, Nike, Under Armour} | 4 | 1 | ✗ |
| {Jordan, Nike, Puma, Under Armour} | 4, 9 | 2 | ✓ |
| {Jordan, Nike, Reebok, Under Armour} | 5, 9 | 2 | ✓ |
| {Jordan, Puma, Reebok, Under Armour} | 9 | 1 | ✗ |
| {New Balance, Nike, Puma, Reebok} | 9 | 1 | ✗ |
| {New Balance, Nike, Puma, Under Armour} | 9 | 1 | ✗ |
| {New Balance, Puma, Reebok, Under Armour} | 8, 9 | 2 | ✓ |
| {Nike, Puma, Reebok, Under Armour} | 2, 9 | 2 | ✓ |

### L4 - Itemsets frecuentes de 4 elementos

Los siguientes 4 itemsets cumplen con min.sup = 2:

| Itemset | Frecuencia |
| ------- | ---------- |
| {Jordan, Nike, Puma, Under Armour} | 2 |
| {Jordan, Nike, Reebok, Under Armour} | 2 |
| {New Balance, Puma, Reebok, Under Armour} | 2 |
| {Nike, Puma, Reebok, Under Armour} | 2 |

### Quinta iteración (C5 - Candidatos de 5 elementos)

Generamos candidatos combinando cuartetos que comparten tres elementos comunes:

| Itemset | Transacciones | Frecuencia | ¿Cumple min.sup? |
| ------- | ------------- | ---------- | ---------------- |
| {Jordan, Nike, Puma, Reebok, Under Armour} | 9 | 1 | ✗ |

### L5 - Itemsets frecuentes de 5 elementos

**No hay itemsets de 5 elementos que cumplan con min.sup = 2.**

El algoritmo termina aquí ya que no se generaron más itemsets frecuentes.

---

## Resumen de Itemsets Frecuentes

| Nivel | Cantidad de Itemsets Frecuentes |
| ----- | ------------------------------- |
| L1 (1 elemento) | 7 |
| L2 (2 elementos) | 18 |
| L3 (3 elementos) | 16 |
| L4 (4 elementos) | 4 |
| L5 (5 elementos) | 0 |
| **Total** | **45** |

---

## Generación de Reglas de Asociación

**Criterio:** min.conf = 75%

Para cada itemset frecuente de 2 o más elementos, generamos todas las reglas posibles y calculamos su confianza.

**Fórmula:** $\text{Confianza}(X \Rightarrow Y) = \frac{\text{soporte}(X \cup Y)}{\text{soporte}(X)} \times 100\%$

### Reglas de Itemsets de 2 elementos (L2)

| Regla | Soporte(X∪Y) | Soporte(X) | Confianza | ¿Cumple 75%? |
| ----- | ------------ | ---------- | --------- | ------------ |
| {Adidas} ⇒ {Jordan} | 3 | 3 | 100.0% | ✓ |
| {Jordan} ⇒ {Adidas} | 3 | 5 | 60.0% | ✗ |
| {Adidas} ⇒ {Nike} | 2 | 3 | 66.7% | ✗ |
| {Nike} ⇒ {Adidas} | 2 | 7 | 28.6% | ✗ |
| {Adidas} ⇒ {Under Armour} | 2 | 3 | 66.7% | ✗ |
| {Under Armour} ⇒ {Adidas} | 2 | 7 | 28.6% | ✗ |
| {Jordan} ⇒ {New Balance} | 2 | 5 | 40.0% | ✗ |
| {New Balance} ⇒ {Jordan} | 2 | 5 | 40.0% | ✗ |
| {Jordan} ⇒ {Nike} | 4 | 5 | 80.0% | ✓ |
| {Nike} ⇒ {Jordan} | 4 | 7 | 57.1% | ✗ |
| {Jordan} ⇒ {Puma} | 2 | 5 | 40.0% | ✗ |
| {Puma} ⇒ {Jordan} | 2 | 6 | 33.3% | ✗ |
| {Jordan} ⇒ {Reebok} | 3 | 5 | 60.0% | ✗ |
| {Reebok} ⇒ {Jordan} | 3 | 6 | 50.0% | ✗ |
| {Jordan} ⇒ {Under Armour} | 4 | 5 | 80.0% | ✓ |
| {Under Armour} ⇒ {Jordan} | 4 | 7 | 57.1% | ✗ |
| {New Balance} ⇒ {Nike} | 3 | 5 | 60.0% | ✗ |
| {Nike} ⇒ {New Balance} | 3 | 7 | 42.9% | ✗ |
| {New Balance} ⇒ {Puma} | 4 | 5 | 80.0% | ✓ |
| {Puma} ⇒ {New Balance} | 4 | 6 | 66.7% | ✗ |
| {New Balance} ⇒ {Reebok} | 2 | 5 | 40.0% | ✗ |
| {Reebok} ⇒ {New Balance} | 2 | 6 | 33.3% | ✗ |
| {New Balance} ⇒ {Under Armour} | 2 | 5 | 40.0% | ✗ |
| {Under Armour} ⇒ {New Balance} | 2 | 7 | 28.6% | ✗ |
| {Nike} ⇒ {Puma} | 4 | 7 | 57.1% | ✗ |
| {Puma} ⇒ {Nike} | 4 | 6 | 66.7% | ✗ |
| {Nike} ⇒ {Reebok} | 3 | 7 | 42.9% | ✗ |
| {Reebok} ⇒ {Nike} | 3 | 6 | 50.0% | ✗ |
| {Nike} ⇒ {Under Armour} | 4 | 7 | 57.1% | ✗ |
| {Under Armour} ⇒ {Nike} | 4 | 7 | 57.1% | ✗ |
| {Puma} ⇒ {Reebok} | 3 | 6 | 50.0% | ✗ |
| {Reebok} ⇒ {Puma} | 3 | 6 | 50.0% | ✗ |
| {Puma} ⇒ {Under Armour} | 4 | 6 | 66.7% | ✗ |
| {Under Armour} ⇒ {Puma} | 4 | 7 | 57.1% | ✗ |
| {Reebok} ⇒ {Under Armour} | 6 | 6 | 100.0% | ✓ |
| {Under Armour} ⇒ {Reebok} | 6 | 7 | 85.7% | ✓ |

**Reglas fuertes de L2 (≥75%):**
1. **{Adidas} ⇒ {Jordan}** - Confianza: 100.0%
2. **{Jordan} ⇒ {Nike}** - Confianza: 80.0%
3. **{Jordan} ⇒ {Under Armour}** - Confianza: 80.0%
4. **{New Balance} ⇒ {Puma}** - Confianza: 80.0%
5. **{Reebok} ⇒ {Under Armour}** - Confianza: 100.0%
6. **{Under Armour} ⇒ {Reebok}** - Confianza: 85.7%

### Reglas de Itemsets de 3 elementos (L3)

| Regla | Soporte(X∪Y) | Soporte(X) | Confianza | ¿Cumple 75%? |
| ----- | ------------ | ---------- | --------- | ------------ |
| {Adidas, Jordan} ⇒ {Nike} | 2 | 3 | 66.7% | ✗ |
| {Adidas, Nike} ⇒ {Jordan} | 2 | 2 | 100.0% | ✓ |
| {Jordan, Nike} ⇒ {Adidas} | 2 | 4 | 50.0% | ✗ |
| {Adidas} ⇒ {Jordan, Nike} | 2 | 3 | 66.7% | ✗ |
| {Jordan} ⇒ {Adidas, Nike} | 2 | 5 | 40.0% | ✗ |
| {Nike} ⇒ {Adidas, Jordan} | 2 | 7 | 28.6% | ✗ |
| {Adidas, Jordan} ⇒ {Under Armour} | 2 | 3 | 66.7% | ✗ |
| {Adidas, Under Armour} ⇒ {Jordan} | 2 | 2 | 100.0% | ✓ |
| {Jordan, Under Armour} ⇒ {Adidas} | 2 | 4 | 50.0% | ✗ |
| {Adidas} ⇒ {Jordan, Under Armour} | 2 | 3 | 66.7% | ✗ |
| {Jordan} ⇒ {Adidas, Under Armour} | 2 | 5 | 40.0% | ✗ |
| {Under Armour} ⇒ {Adidas, Jordan} | 2 | 7 | 28.6% | ✗ |
| {Jordan, New Balance} ⇒ {Nike} | 2 | 2 | 100.0% | ✓ |
| {Jordan, Nike} ⇒ {New Balance} | 2 | 4 | 50.0% | ✗ |
| {New Balance, Nike} ⇒ {Jordan} | 2 | 3 | 66.7% | ✗ |
| {Jordan} ⇒ {New Balance, Nike} | 2 | 5 | 40.0% | ✗ |
| {New Balance} ⇒ {Jordan, Nike} | 2 | 5 | 40.0% | ✗ |
| {Nike} ⇒ {Jordan, New Balance} | 2 | 7 | 28.6% | ✗ |
| {Jordan, Nike} ⇒ {Puma} | 2 | 4 | 50.0% | ✗ |
| {Jordan, Puma} ⇒ {Nike} | 2 | 2 | 100.0% | ✓ |
| {Nike, Puma} ⇒ {Jordan} | 2 | 4 | 50.0% | ✗ |
| {Jordan} ⇒ {Nike, Puma} | 2 | 5 | 40.0% | ✗ |
| {Nike} ⇒ {Jordan, Puma} | 2 | 7 | 28.6% | ✗ |
| {Puma} ⇒ {Jordan, Nike} | 2 | 6 | 33.3% | ✗ |
| {Jordan, Nike} ⇒ {Reebok} | 2 | 4 | 50.0% | ✗ |
| {Jordan, Reebok} ⇒ {Nike} | 2 | 3 | 66.7% | ✗ |
| {Nike, Reebok} ⇒ {Jordan} | 2 | 3 | 66.7% | ✗ |
| {Jordan} ⇒ {Nike, Reebok} | 2 | 5 | 40.0% | ✗ |
| {Nike} ⇒ {Jordan, Reebok} | 2 | 7 | 28.6% | ✗ |
| {Reebok} ⇒ {Jordan, Nike} | 2 | 6 | 33.3% | ✗ |
| {Jordan, Nike} ⇒ {Under Armour} | 3 | 4 | 75.0% | ✓ |
| {Jordan, Under Armour} ⇒ {Nike} | 3 | 4 | 75.0% | ✓ |
| {Nike, Under Armour} ⇒ {Jordan} | 3 | 4 | 75.0% | ✓ |
| {Jordan} ⇒ {Nike, Under Armour} | 3 | 5 | 60.0% | ✗ |
| {Nike} ⇒ {Jordan, Under Armour} | 3 | 7 | 42.9% | ✗ |
| {Under Armour} ⇒ {Jordan, Nike} | 3 | 7 | 42.9% | ✗ |
| {Jordan, Puma} ⇒ {Under Armour} | 2 | 2 | 100.0% | ✓ |
| {Jordan, Under Armour} ⇒ {Puma} | 2 | 4 | 50.0% | ✗ |
| {Puma, Under Armour} ⇒ {Jordan} | 2 | 4 | 50.0% | ✗ |
| {Jordan} ⇒ {Puma, Under Armour} | 2 | 5 | 40.0% | ✗ |
| {Puma} ⇒ {Jordan, Under Armour} | 2 | 6 | 33.3% | ✗ |
| {Under Armour} ⇒ {Jordan, Puma} | 2 | 7 | 28.6% | ✗ |
| {Jordan, Reebok} ⇒ {Under Armour} | 3 | 3 | 100.0% | ✓ |
| {Jordan, Under Armour} ⇒ {Reebok} | 3 | 4 | 75.0% | ✓ |
| {Reebok, Under Armour} ⇒ {Jordan} | 3 | 6 | 50.0% | ✗ |
| {Jordan} ⇒ {Reebok, Under Armour} | 3 | 5 | 60.0% | ✗ |
| {Reebok} ⇒ {Jordan, Under Armour} | 3 | 6 | 50.0% | ✗ |
| {Under Armour} ⇒ {Jordan, Reebok} | 3 | 7 | 42.9% | ✗ |
| {New Balance, Nike} ⇒ {Puma} | 2 | 3 | 66.7% | ✗ |
| {New Balance, Puma} ⇒ {Nike} | 2 | 4 | 50.0% | ✗ |
| {Nike, Puma} ⇒ {New Balance} | 2 | 4 | 50.0% | ✗ |
| {New Balance} ⇒ {Nike, Puma} | 2 | 5 | 40.0% | ✗ |
| {Nike} ⇒ {New Balance, Puma} | 2 | 7 | 28.6% | ✗ |
| {Puma} ⇒ {New Balance, Nike} | 2 | 6 | 33.3% | ✗ |
| {New Balance, Puma} ⇒ {Reebok} | 2 | 4 | 50.0% | ✗ |
| {New Balance, Reebok} ⇒ {Puma} | 2 | 2 | 100.0% | ✓ |
| {Puma, Reebok} ⇒ {New Balance} | 2 | 3 | 66.7% | ✗ |
| {New Balance} ⇒ {Puma, Reebok} | 2 | 5 | 40.0% | ✗ |
| {Puma} ⇒ {New Balance, Reebok} | 2 | 6 | 33.3% | ✗ |
| {Reebok} ⇒ {New Balance, Puma} | 2 | 6 | 33.3% | ✗ |
| {New Balance, Puma} ⇒ {Under Armour} | 2 | 4 | 50.0% | ✗ |
| {New Balance, Under Armour} ⇒ {Puma} | 2 | 2 | 100.0% | ✓ |
| {Puma, Under Armour} ⇒ {New Balance} | 2 | 4 | 50.0% | ✗ |
| {New Balance} ⇒ {Puma, Under Armour} | 2 | 5 | 40.0% | ✗ |
| {Puma} ⇒ {New Balance, Under Armour} | 2 | 6 | 33.3% | ✗ |
| {Under Armour} ⇒ {New Balance, Puma} | 2 | 7 | 28.6% | ✗ |
| {New Balance, Reebok} ⇒ {Under Armour} | 2 | 2 | 100.0% | ✓ |
| {New Balance, Under Armour} ⇒ {Reebok} | 2 | 2 | 100.0% | ✓ |
| {Reebok, Under Armour} ⇒ {New Balance} | 2 | 6 | 33.3% | ✗ |
| {New Balance} ⇒ {Reebok, Under Armour} | 2 | 5 | 40.0% | ✗ |
| {Reebok} ⇒ {New Balance, Under Armour} | 2 | 6 | 33.3% | ✗ |
| {Under Armour} ⇒ {New Balance, Reebok} | 2 | 7 | 28.6% | ✗ |
| {Nike, Puma} ⇒ {Reebok} | 2 | 4 | 50.0% | ✗ |
| {Nike, Reebok} ⇒ {Puma} | 2 | 3 | 66.7% | ✗ |
| {Puma, Reebok} ⇒ {Nike} | 2 | 3 | 66.7% | ✗ |
| {Nike} ⇒ {Puma, Reebok} | 2 | 7 | 28.6% | ✗ |
| {Puma} ⇒ {Nike, Reebok} | 2 | 6 | 33.3% | ✗ |
| {Reebok} ⇒ {Nike, Puma} | 2 | 6 | 33.3% | ✗ |
| {Nike, Puma} ⇒ {Under Armour} | 3 | 4 | 75.0% | ✓ |
| {Nike, Under Armour} ⇒ {Puma} | 3 | 4 | 75.0% | ✓ |
| {Puma, Under Armour} ⇒ {Nike} | 3 | 4 | 75.0% | ✓ |
| {Nike} ⇒ {Puma, Under Armour} | 3 | 7 | 42.9% | ✗ |
| {Puma} ⇒ {Nike, Under Armour} | 3 | 6 | 50.0% | ✗ |
| {Under Armour} ⇒ {Nike, Puma} | 3 | 7 | 42.9% | ✗ |
| {Nike, Reebok} ⇒ {Under Armour} | 3 | 3 | 100.0% | ✓ |
| {Nike, Under Armour} ⇒ {Reebok} | 3 | 4 | 75.0% | ✓ |
| {Reebok, Under Armour} ⇒ {Nike} | 3 | 6 | 50.0% | ✗ |
| {Nike} ⇒ {Reebok, Under Armour} | 3 | 7 | 42.9% | ✗ |
| {Reebok} ⇒ {Nike, Under Armour} | 3 | 6 | 50.0% | ✗ |
| {Under Armour} ⇒ {Nike, Reebok} | 3 | 7 | 42.9% | ✗ |
| {Puma, Reebok} ⇒ {Under Armour} | 3 | 3 | 100.0% | ✓ |
| {Puma, Under Armour} ⇒ {Reebok} | 3 | 4 | 75.0% | ✓ |
| {Reebok, Under Armour} ⇒ {Puma} | 3 | 6 | 50.0% | ✗ |
| {Puma} ⇒ {Reebok, Under Armour} | 3 | 6 | 50.0% | ✗ |
| {Reebok} ⇒ {Puma, Under Armour} | 3 | 6 | 50.0% | ✗ |
| {Under Armour} ⇒ {Puma, Reebok} | 3 | 7 | 42.9% | ✗ |

**Reglas fuertes de L3 (≥75%):**
7. **{Adidas, Nike} ⇒ {Jordan}** - Confianza: 100.0%
8. **{Adidas, Under Armour} ⇒ {Jordan}** - Confianza: 100.0%
9. **{Jordan, New Balance} ⇒ {Nike}** - Confianza: 100.0%
10. **{Jordan, Puma} ⇒ {Nike}** - Confianza: 100.0%
11. **{Jordan, Nike} ⇒ {Under Armour}** - Confianza: 75.0%
12. **{Jordan, Under Armour} ⇒ {Nike}** - Confianza: 75.0%
13. **{Nike, Under Armour} ⇒ {Jordan}** - Confianza: 75.0%
14. **{Jordan, Puma} ⇒ {Under Armour}** - Confianza: 100.0%
15. **{Jordan, Reebok} ⇒ {Under Armour}** - Confianza: 100.0%
16. **{Jordan, Under Armour} ⇒ {Reebok}** - Confianza: 75.0%
17. **{New Balance, Reebok} ⇒ {Puma}** - Confianza: 100.0%
18. **{New Balance, Under Armour} ⇒ {Puma}** - Confianza: 100.0%
19. **{New Balance, Reebok} ⇒ {Under Armour}** - Confianza: 100.0%
20. **{New Balance, Under Armour} ⇒ {Reebok}** - Confianza: 100.0%
21. **{Nike, Puma} ⇒ {Under Armour}** - Confianza: 75.0%
22. **{Nike, Under Armour} ⇒ {Puma}** - Confianza: 75.0%
23. **{Puma, Under Armour} ⇒ {Nike}** - Confianza: 75.0%
24. **{Nike, Reebok} ⇒ {Under Armour}** - Confianza: 100.0%
25. **{Nike, Under Armour} ⇒ {Reebok}** - Confianza: 75.0%
26. **{Puma, Reebok} ⇒ {Under Armour}** - Confianza: 100.0%
27. **{Puma, Under Armour} ⇒ {Reebok}** - Confianza: 75.0%

### Reglas de Itemsets de 4 elementos (L4)

| Regla | Soporte(X∪Y) | Soporte(X) | Confianza | ¿Cumple 75%? |
| ----- | ------------ | ---------- | --------- | ------------ |
| {Jordan, Nike, Puma} ⇒ {Under Armour} | 2 | 2 | 100.0% | ✓ |
| {Jordan, Nike, Under Armour} ⇒ {Puma} | 2 | 3 | 66.7% | ✗ |
| {Jordan, Puma, Under Armour} ⇒ {Nike} | 2 | 2 | 100.0% | ✓ |
| {Nike, Puma, Under Armour} ⇒ {Jordan} | 2 | 3 | 66.7% | ✗ |
| {Jordan, Nike} ⇒ {Puma, Under Armour} | 2 | 4 | 50.0% | ✗ |
| {Jordan, Puma} ⇒ {Nike, Under Armour} | 2 | 2 | 100.0% | ✓ |
| {Jordan, Under Armour} ⇒ {Nike, Puma} | 2 | 4 | 50.0% | ✗ |
| {Nike, Puma} ⇒ {Jordan, Under Armour} | 2 | 4 | 50.0% | ✗ |
| {Nike, Under Armour} ⇒ {Jordan, Puma} | 2 | 4 | 50.0% | ✗ |
| {Puma, Under Armour} ⇒ {Jordan, Nike} | 2 | 4 | 50.0% | ✗ |
| {Jordan} ⇒ {Nike, Puma, Under Armour} | 2 | 5 | 40.0% | ✗ |
| {Nike} ⇒ {Jordan, Puma, Under Armour} | 2 | 7 | 28.6% | ✗ |
| {Puma} ⇒ {Jordan, Nike, Under Armour} | 2 | 6 | 33.3% | ✗ |
| {Under Armour} ⇒ {Jordan, Nike, Puma} | 2 | 7 | 28.6% | ✗ |
| {Jordan, Nike, Reebok} ⇒ {Under Armour} | 2 | 2 | 100.0% | ✓ |
| {Jordan, Nike, Under Armour} ⇒ {Reebok} | 2 | 3 | 66.7% | ✗ |
| {Jordan, Reebok, Under Armour} ⇒ {Nike} | 2 | 3 | 66.7% | ✗ |
| {Nike, Reebok, Under Armour} ⇒ {Jordan} | 2 | 3 | 66.7% | ✗ |
| {Jordan, Nike} ⇒ {Reebok, Under Armour} | 2 | 4 | 50.0% | ✗ |
| {Jordan, Reebok} ⇒ {Nike, Under Armour} | 2 | 3 | 66.7% | ✗ |
| {Jordan, Under Armour} ⇒ {Nike, Reebok} | 2 | 4 | 50.0% | ✗ |
| {Nike, Reebok} ⇒ {Jordan, Under Armour} | 2 | 3 | 66.7% | ✗ |
| {Nike, Under Armour} ⇒ {Jordan, Reebok} | 2 | 4 | 50.0% | ✗ |
| {Reebok, Under Armour} ⇒ {Jordan, Nike} | 2 | 6 | 33.3% | ✗ |
| {Jordan} ⇒ {Nike, Reebok, Under Armour} | 2 | 5 | 40.0% | ✗ |
| {Nike} ⇒ {Jordan, Reebok, Under Armour} | 2 | 7 | 28.6% | ✗ |
| {Reebok} ⇒ {Jordan, Nike, Under Armour} | 2 | 6 | 33.3% | ✗ |
| {Under Armour} ⇒ {Jordan, Nike, Reebok} | 2 | 7 | 28.6% | ✗ |
| {New Balance, Puma, Reebok} ⇒ {Under Armour} | 2 | 2 | 100.0% | ✓ |
| {New Balance, Puma, Under Armour} ⇒ {Reebok} | 2 | 2 | 100.0% | ✓ |
| {New Balance, Reebok, Under Armour} ⇒ {Puma} | 2 | 2 | 100.0% | ✓ |
| {Puma, Reebok, Under Armour} ⇒ {New Balance} | 2 | 3 | 66.7% | ✗ |
| {New Balance, Puma} ⇒ {Reebok, Under Armour} | 2 | 4 | 50.0% | ✗ |
| {New Balance, Reebok} ⇒ {Puma, Under Armour} | 2 | 2 | 100.0% | ✓ |
| {New Balance, Under Armour} ⇒ {Puma, Reebok} | 2 | 2 | 100.0% | ✓ |
| {Puma, Reebok} ⇒ {New Balance, Under Armour} | 2 | 3 | 66.7% | ✗ |
| {Puma, Under Armour} ⇒ {New Balance, Reebok} | 2 | 4 | 50.0% | ✗ |
| {Reebok, Under Armour} ⇒ {New Balance, Puma} | 2 | 6 | 33.3% | ✗ |
| {New Balance} ⇒ {Puma, Reebok, Under Armour} | 2 | 5 | 40.0% | ✗ |
| {Puma} ⇒ {New Balance, Reebok, Under Armour} | 2 | 6 | 33.3% | ✗ |
| {Reebok} ⇒ {New Balance, Puma, Under Armour} | 2 | 6 | 33.3% | ✗ |
| {Under Armour} ⇒ {New Balance, Puma, Reebok} | 2 | 7 | 28.6% | ✗ |
| {Nike, Puma, Reebok} ⇒ {Under Armour} | 2 | 2 | 100.0% | ✓ |
| {Nike, Puma, Under Armour} ⇒ {Reebok} | 2 | 3 | 66.7% | ✗ |
| {Nike, Reebok, Under Armour} ⇒ {Puma} | 2 | 3 | 66.7% | ✗ |
| {Puma, Reebok, Under Armour} ⇒ {Nike} | 2 | 3 | 66.7% | ✗ |
| {Nike, Puma} ⇒ {Reebok, Under Armour} | 2 | 4 | 50.0% | ✗ |
| {Nike, Reebok} ⇒ {Puma, Under Armour} | 2 | 3 | 66.7% | ✗ |
| {Nike, Under Armour} ⇒ {Puma, Reebok} | 2 | 4 | 50.0% | ✗ |
| {Puma, Reebok} ⇒ {Nike, Under Armour} | 2 | 3 | 66.7% | ✗ |
| {Puma, Under Armour} ⇒ {Nike, Reebok} | 2 | 4 | 50.0% | ✗ |
| {Reebok, Under Armour} ⇒ {Nike, Puma} | 2 | 6 | 33.3% | ✗ |
| {Nike} ⇒ {Puma, Reebok, Under Armour} | 2 | 7 | 28.6% | ✗ |
| {Puma} ⇒ {Nike, Reebok, Under Armour} | 2 | 6 | 33.3% | ✗ |
| {Reebok} ⇒ {Nike, Puma, Under Armour} | 2 | 6 | 33.3% | ✗ |
| {Under Armour} ⇒ {Nike, Puma, Reebok} | 2 | 7 | 28.6% | ✗ |

**Reglas fuertes de L4 (≥75%):**
28. **{Jordan, Nike, Puma} ⇒ {Under Armour}** - Confianza: 100.0%
29. **{Jordan, Puma, Under Armour} ⇒ {Nike}** - Confianza: 100.0%
30. **{Jordan, Puma} ⇒ {Nike, Under Armour}** - Confianza: 100.0%
31. **{Jordan, Nike, Reebok} ⇒ {Under Armour}** - Confianza: 100.0%
32. **{New Balance, Puma, Reebok} ⇒ {Under Armour}** - Confianza: 100.0%
33. **{New Balance, Puma, Under Armour} ⇒ {Reebok}** - Confianza: 100.0%
34. **{New Balance, Reebok, Under Armour} ⇒ {Puma}** - Confianza: 100.0%
35. **{New Balance, Reebok} ⇒ {Puma, Under Armour}** - Confianza: 100.0%
36. **{New Balance, Under Armour} ⇒ {Puma, Reebok}** - Confianza: 100.0%
37. **{Nike, Puma, Reebok} ⇒ {Under Armour}** - Confianza: 100.0%

---

## Resumen Final de Reglas de Asociación Fuertes

**Total de reglas fuertes (confianza ≥ 75%): 37 reglas**

### Por nivel:
- **L2:** 6 reglas fuertes
- **L3:** 21 reglas fuertes
- **L4:** 10 reglas fuertes

### Top 10 Reglas con Confianza 100%:

1. **{Adidas} ⇒ {Jordan}** - Soporte: 3, Confianza: 100.0%
2. **{Reebok} ⇒ {Under Armour}** - Soporte: 6, Confianza: 100.0%
3. **{Adidas, Nike} ⇒ {Jordan}** - Soporte: 2, Confianza: 100.0%
4. **{Adidas, Under Armour} ⇒ {Jordan}** - Soporte: 2, Confianza: 100.0%
5. **{Jordan, New Balance} ⇒ {Nike}** - Soporte: 2, Confianza: 100.0%
6. **{Jordan, Puma} ⇒ {Nike}** - Soporte: 2, Confianza: 100.0%
7. **{Jordan, Puma} ⇒ {Under Armour}** - Soporte: 2, Confianza: 100.0%
8. **{Jordan, Reebok} ⇒ {Under Armour}** - Soporte: 3, Confianza: 100.0%
9. **{Nike, Reebok} ⇒ {Under Armour}** - Soporte: 3, Confianza: 100.0%
10. **{Puma, Reebok} ⇒ {Under Armour}** - Soporte: 3, Confianza: 100.0%

### Conclusiones:

- La regla más fuerte es **{Reebok} ⇒ {Under Armour}** con soporte de 6 transacciones.
- Los productos **Under Armour** y **Reebok** aparecen juntos en todas las transacciones donde está Reebok.
- Los productos **Jordan** y **Adidas** también muestran alta asociación (100% de confianza).
- Las combinaciones que incluyen **{Reebok, Under Armour}** tienden a generar reglas muy fuertes.

