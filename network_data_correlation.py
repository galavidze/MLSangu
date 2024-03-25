{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2df76608",
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
   "execution_count": 5,
   "id": "93504401",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/Users/giorgia/Downloads/hw1\n"
     ]
    }
   ],
   "source": [
    "# install fpdf if you dont have it\n",
    "pip install fpdf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "b1efa758",
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
       "      <td>0.044773</td>\n",
       "      <td>-0.039686</td>\n",
       "      <td>0.079234</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>F2</th>\n",
       "      <td>0.044773</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.149937</td>\n",
       "      <td>0.015539</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>F3</th>\n",
       "      <td>-0.039686</td>\n",
       "      <td>-0.149937</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.070489</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>F4</th>\n",
       "      <td>0.079234</td>\n",
       "      <td>0.015539</td>\n",
       "      <td>0.070489</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          F1        F2        F3        F4\n",
       "F1  1.000000  0.044773 -0.039686  0.079234\n",
       "F2  0.044773  1.000000 -0.149937  0.015539\n",
       "F3 -0.039686 -0.149937  1.000000  0.070489\n",
       "F4  0.079234  0.015539  0.070489  1.000000"
      ]
     },
     "execution_count": 22,
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
    "from fpdf import FPDF\n",
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
   "execution_count": 23,
   "id": "4e9723a6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'The names of the two features with highest correlation are F1 F4'"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#find highest correlation\n",
    "correlation_values = correlation_matrix.values\n",
    "np.fill_diagonal(correlation_values, -np.inf)\n",
    "max_corr_index = np.argmax(correlation_values)\n",
    "max_corr_row, max_corr_column = np.unravel_index(max_corr_index, correlation_values.shape)\n",
    "max_corr_value = correlation_values[max_corr_row, max_corr_column]\n",
    "\n",
    "f1 = correlation_matrix.columns[max_corr_row]\n",
    "f2 = correlation_matrix.columns[max_corr_column]\n",
    "\n",
    "highest_corr= \"The names of the two features with highest correlation are \"+str(f1)+' '+str(f2)\n",
    "highest_corr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "ea3ba588",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "''"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pdf = FPDF()\n",
    "pdf.add_page()\n",
    "pdf.set_xy(0, 0)\n",
    "pdf.set_font('arial', 'B', 13.0)\n",
    "pdf.cell(ln=0, h=5.0, align='L', w=0, txt=highest_corr, border=0)\n",
    "pdf.output('test.pdf', 'F')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "22dbd66e",
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
