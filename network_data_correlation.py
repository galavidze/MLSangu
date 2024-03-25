{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d0b343ec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\nLashagiorgi Alavidze\\nMar 25, 2024\\nMachine Learning for Cybersecurity\\nHomework 1\\n'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''\n",
    "Lashagiorgi Alavidze\n",
    "Mar 25, 2024\n",
    "Machine Learning for Cybersecurity\n",
    "Homework 1\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a5673a05",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x432 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>F1</th>\n",
       "      <th>F2</th>\n",
       "      <th>F3</th>\n",
       "      <th>F4</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>F1</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.070337</td>\n",
       "      <td>-0.042720</td>\n",
       "      <td>-0.070587</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>F2</th>\n",
       "      <td>0.070337</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.034694</td>\n",
       "      <td>-0.104321</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>F3</th>\n",
       "      <td>-0.042720</td>\n",
       "      <td>0.034694</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.029216</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>F4</th>\n",
       "      <td>-0.070587</td>\n",
       "      <td>-0.104321</td>\n",
       "      <td>0.029216</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          F1        F2        F3        F4\n",
       "F1  1.000000  0.070337 -0.042720 -0.070587\n",
       "F2  0.070337  1.000000  0.034694 -0.104321\n",
       "F3 -0.042720  0.034694  1.000000  0.029216\n",
       "F4 -0.070587 -0.104321  0.029216  1.000000"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd \n",
    "import random\n",
    "import csv\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "\n",
    "#generate network data and append to network_packet_data.csv\n",
    "network_data = np.random.rand(200, 4)  # Generating random data with 4 features and 200 samples\n",
    "with open('network_data.csv', 'w', newline='') as csvfile:\n",
    "    writer = csv.writer(csvfile)\n",
    "    writer.writerows(network_data)\n",
    "    \n",
    "#Write the Python program that reads the generated data and calculates the correlation matrix using Pearson formula.\n",
    "#The names of features should be displayed in the matrix.\n",
    "cols = ['F1','F2','F3','F4']\n",
    "df = pd.read_csv('network_data.csv')\n",
    "df.columns = cols\n",
    "\n",
    "correlation_matrix = df.corr(method='pearson')\n",
    "\n",
    "# Plot correlation matrix\n",
    "plt.figure(figsize=(8, 6))\n",
    "sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', xticklabels=correlation_matrix.columns, yticklabels=correlation_matrix.columns)\n",
    "plt.title('Correlation Matrix')\n",
    "plt.xlabel('Features')\n",
    "plt.ylabel('Features')\n",
    "plt.tight_layout()\n",
    "plt.savefig('correlation_matrix.pdf')\n",
    "plt.show()\n",
    "plt.close()\n",
    "\n",
    "#find highest correlation features\n",
    "correlation_matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a1ccc2ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "#find highest correlation\n",
    "correlation_values = correlation_matrix.values\n",
    "np.fill_diagonal(correlation_values, -np.inf)\n",
    "max_corr_index = np.argmax(correlation_values)\n",
    "max_corr_row, max_corr_column = np.unravel_index(max_corr_index, correlation_values.shape)\n",
    "max_corr_value = correlation_values[max_corr_row, max_corr_column]\n",
    "\n",
    "max_corr_feature1 = correlation_matrix.columns[max_corr_row]\n",
    "max_corr_feature2 = correlation_matrix.columns[max_corr_column]\n",
    "result_string = f\"The highest correlation value is {max_corr_value} found between distinct features '{max_corr_feature1}' and '{max_corr_feature2}'.\"\n",
    "\n",
    "# Write the result string to a PDF file\n",
    "with open(\"highest_correlation.pdf\", \"w\") as f:\n",
    "    f.write(result_string)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "11fcf75c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
