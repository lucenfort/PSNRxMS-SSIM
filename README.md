# PSNR x MS-MSSSIM

Este é um arquivo README para o projeto intitulado "PSNR x MS-MSSSIM". O projeto envolve o carregamento e processamento de dados, visualização dos dados usando gráficos e a busca pela melhor combinação de parâmetros para compressão.

## Dependências

As seguintes bibliotecas são necessárias para executar o código:

- numpy
- pandas
- matplotlib
- seaborn

Você pode instalar essas bibliotecas usando `pip`:


## Dados

Os dados para este projeto são armazenados em um arquivo CSV chamado `data.csv`. Ele contém os valores obtidos pelas métricas de avaliação de qualidade de imagens para compressão. Os dados são carregados em um DataFrame do pandas usando a função `read_csv`.

## Processamento de Dados

Os dados são processados para remover quaisquer linhas com valores faltantes (NaN) e remover linhas com um valor "level" maior que 5. Os dados processados são salvos em um novo arquivo CSV chamado `data_clean.csv`.

## Visualização de Dados

### Gráfico PSNR

Um gráfico de linha é criado usando a biblioteca seaborn para visualizar a relação entre as colunas "level" e "psnr" dos dados. O gráfico é salvo como uma imagem PNG chamada `grafico_psnr.png`.

### Gráfico MSSSIM

Um gráfico de linha é criado usando a biblioteca seaborn para visualizar a relação entre as colunas "level" e "msssim" dos dados. O gráfico é salvo como uma imagem PNG chamada `grafico_msssim.png`.

## Encontrar a Melhor Combinação

O código calcula a melhor combinação de família de wavelet e nível de decomposição para compressão. Ele usa os valores normalizados das métricas "psnr" e "msssim", juntamente com pesos definidos pelo usuário, para calcular uma pontuação combinada. Os dados são então classificados com base na pontuação combinada em ordem decrescente para encontrar a melhor combinação. Os resultados são impressos no console.

Os dados normalizados são salvos em um novo arquivo CSV chamado `normalized_data.csv`.




