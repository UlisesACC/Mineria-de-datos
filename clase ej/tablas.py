import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# =======================
# Datos
# =======================
puntos = pd.DataFrame({
    "X": [0.35, 0.25, 0.58, 0.68, 0.35, 0.60],
    "Y": [0.45, 0.21, 0.42, 0.81, 0.22, 0.34]
}, index=["A", "B", "C", "D", "E", "F"])


# =======================
# Función para imprimir matriz con índices
# =======================
def print_matrix(title, M, labels):
    df = pd.DataFrame(M, index=labels, columns=labels)
    print("\n" + title)
    print(df)


# =======================
# Función general para iteraciones (muestra clusters por iteración)
# =======================
def hierarchical_iterations(data, method="single"):
    # Matriz de distancias inicial
    dist = squareform(pdist(data.values, metric="euclidean"))
    labels = list(data.index)
    # Inicializar clusters como listas de elementos originales
    clusters = [[lbl] for lbl in labels]

    print_matrix("Matriz inicial", dist, labels)
    print("\nClusters iniciales:", clusters)

    iteration = 1

    while len(dist) > 1:
        # Encontrar el par mínimo (ignorando diagonal)
        masked = np.ma.masked_where(np.eye(len(dist), dtype=bool), dist)
        i, j = np.unravel_index(masked.argmin(), masked.shape)

        print(f"\n=== Iteración {iteration} ===")
        print(f"Se fusionan: {labels[i]} y {labels[j]}")

        # Nuevo cluster (composición de elementos originales)
        new_cluster = clusters[i] + clusters[j]

        # Crear nuevo label del cluster
        new_label = f"({labels[i]}-{labels[j]})"

        # Calcular nuevos valores según método
        new_row = []
        for k in range(len(dist)):
            if k != i and k != j:
                if method == "single":
                    new_row.append(min(dist[i, k], dist[j, k]))
                elif method == "complete":
                    new_row.append(max(dist[i, k], dist[j, k]))
                elif method == "average":
                    new_row.append((dist[i, k] + dist[j, k]) / 2)

        # Construir nueva matriz sin i ni j
        new_dist = []
        for k in range(len(dist)):
            if k != i and k != j:
                row = []
                for m in range(len(dist)):
                    if m != i and m != j:
                        row.append(dist[k, m])
                new_dist.append(row)

        # Agregar nueva fila/columna (columna a cada fila existente)
        for idx, r in enumerate(new_dist):
            r.append(new_row[idx])

        new_row.append(0.0)
        new_dist.append(new_row)

        # Actualizar etiquetas y clusters
        old_labels = labels.copy()
        labels = [old_labels[k] for k in range(len(old_labels)) if k not in (i, j)]
        labels.append(new_label)

        old_clusters = clusters.copy()
        clusters = [old_clusters[k] for k in range(len(old_clusters)) if k not in (i, j)]
        clusters.append(new_cluster)

        dist = np.array(new_dist)

        print_matrix("Matriz actualizada", dist, labels)
        print("Clusters actuales:", clusters)

        iteration += 1
        if len(dist) == 1:
            break


# ===============================
# Ejecutar los 3 métodos y dendrogramas
# ===============================

methods = [("single", "ENLACE SIMPLE"), ("complete", "ENLACE COMPLETO"), ("average", "ENLACE PROMEDIO")]

for method, title in methods:
    print(f"\n\n********* {title} *********")
    hierarchical_iterations(puntos, method=method)

    # Dendograma usando scipy (para visualizar la jerarquía completa)
    Z = linkage(puntos.values, method=method, metric='euclidean')
    plt.figure(figsize=(8, 4))
    dendrogram(Z, labels=puntos.index.tolist(), leaf_rotation=0)
    plt.title(f"Dendrograma ({title})")
    plt.xlabel("Elementos")
    plt.ylabel("Distancia")
    plt.tight_layout()
    plt.show()
