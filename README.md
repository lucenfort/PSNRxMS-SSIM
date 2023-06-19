## Data

The data for this project is stored in a CSV file named `data.csv`. It contains the values obtained from image quality evaluation metrics for compression. The data is loaded into a pandas DataFrame using the `read_csv` function.

## Data Processing

The data is processed to remove any rows with missing values (NaN) and to remove rows with a "level" value greater than 5. The processed data is saved to a new CSV file named `data_clean.csv`.

## Data Visualization

### PSNR Plot

A line plot is created using the seaborn library to visualize the relationship between the "level" and "psnr" columns of the data. The plot is saved as a PNG image named `grafico_psnr.png`.

### MSSSIM Plot

A line plot is created using the seaborn library to visualize the relationship between the "level" and "msssim" columns of the data. The plot is saved as a PNG image named `grafico_msssim.png`.

## Finding the Best Combination

The code calculates the best combination of wavelet family and level of decomposition for compression. It uses the normalized values of the "psnr" and "msssim" metrics, along with user-defined weights, to calculate a combined score. The data is then sorted based on the combined score in descending order to find the best combination. The results are printed to the console.

The normalized data is saved to a new CSV file named `normalized_data.csv`.

