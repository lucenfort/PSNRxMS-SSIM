import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

###############################################################################
# ENTRADA DOS DADOS:
###############################################################################
# Carrego os dados de um arquivo .csv contendo o valores obtidos pelas métricas
# de avaliação de qualidade de imagens, para avaliar a compressão.
# Esses dados são transformados em um DataFrame pelo pandas
df = pd.read_csv("data.csv")
df.head(10)  # mostra as 10 primeiras linhas do Dataframe na janela interativa

###############################################################################
# TRATAMENTO DE DADOS:
###############################################################################
# Aqui eu substituir os valores inf e -inf por nan e removir as linhas com
# valores nan.
data = df.replace([np.inf, -np.inf], np.nan).dropna(axis=0)
data.head(10)  # mostra as 10 primeiras linhas do Dataframe na janela interativa
# Remover as linhas com levels superiores a 5
data = data.drop(data[data["level"] > 5].index)

# Salva o dataframe tratado
data.to_csv("data_clean.csv", index=False)

###############################################################################
# VIZUALIZAÇÃO DE DADOS:
###############################################################################
plt.style.use("ggplot")  # defino o tema dos gráficos desejado

# Definir o tamanho dos gráficos
plt.figure(figsize=(10, 6))

# Pegar os valores únicos da coluna 'level'
levels = data["level"].unique()

# Exibir os valores únicos
print(levels)

# Gráfico de PSNR
sns.lineplot(data=data, x="level", y="psnr")
plt.xlabel("Level")
plt.ylabel("PSNR")
plt.title("Gráfico de PSNR")
plt.xticks(levels)  # Definir os valores do eixo x como uma lista de inteiros de 0 a 5

# Salvar o gráfico de PSNR em alta resolução
plt.savefig("grafico_psnr.png", dpi=300)
plt.show()

# Gráfico de MSSSIM
sns.lineplot(data=data, x="level", y="msssim")
plt.xlabel("Level")
plt.ylabel("MS-SSIM")
plt.title("Gráfico de MS-SSIM")
plt.xticks(levels)  # Definir os valores do eixo x como uma lista de inteiros de 0 a 5

# Salvar o gráfico de MSSSIM em alta resolução
plt.savefig("grafico_msssim.png", dpi=300)
plt.show()


###############################################################################
# ENCONTRAR MELHOR COMBINAÇÃO
###############################################################################
# Aqui vamos calcular qual a melhor combinação de familia wavelet e de level de
# decomposição para compressão, por meio de parametrização das métricas usando
# normalização min-max.
# A melhor combinação indicarar os paramêtros da melhor compressão.

# Definir pesos personalizados para as métricas
weight_psnr = 0.5
weight_msssim = 0.5

# Parametrizar as métricas usando min-max normalization
data["normalized_psnr"] = (data["psnr"] - data["psnr"].min()) / (
    data["psnr"].max() - data["psnr"].min()
)
data["normalized_msssim"] = (data["msssim"] - data["msssim"].min()) / (
    data["msssim"].max() - data["msssim"].min()
)

# Print dos resultados da parametrização
print("Resultado da parametrização:")
print(data[["family", "level", "normalized_psnr", "normalized_msssim"]])

# Calcular uma métrica combinada com os pesos personalizados
data["combined_score"] = (
    weight_psnr * data["normalized_psnr"] + weight_msssim * data["normalized_msssim"]
)

# Ordenar o dataset pela coluna 'combined_score' em ordem decrescente
sorted_data = data.sort_values(by="combined_score", ascending=False)

# Obter a melhor combinação de 'family' e 'level'
best_combination = sorted_data.iloc[0]

print("Melhor combinação:")
print("Family:", best_combination["family"])
print("Level:", best_combination["level"])

# Print dos valores das métricas da melhor combinação
print("\nValores das métricas da melhor combinação:")
print("PSNR:", best_combination["psnr"])
print("MSSSIM:", best_combination["msssim"])


# Salva o dataframe normalizado
data.to_csv("normalized_data.csv", index=False)
