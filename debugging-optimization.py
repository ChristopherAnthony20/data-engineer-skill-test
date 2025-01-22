{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "052b1918-b7a8-48b7-b7d4-fb7353acaa11",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          price\n",
      "A  1.000264e+12\n",
      "B  1.001172e+12\n",
      "C  1.001160e+12\n",
      "D  1.000479e+12\n",
      "E  1.002264e+12\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "aggregated_result = {}\n",
    "\n",
    "\n",
    "chunksize = 10**6\n",
    "for chunk in pd.read_csv('large_file.csv', chunksize=chunksize):\n",
    "\n",
    "    filtered_chunk = chunk[chunk['price'] > 100]\n",
    "    grouped_chunk = filtered_chunk.groupby('category').sum()\n",
    "    \n",
    "    for category, values in grouped_chunk.iterrows():\n",
    "        if category in aggregated_result:\n",
    "            aggregated_result[category] += values\n",
    "        else:\n",
    "            aggregated_result[category] = values\n",
    "\n",
    "final_result = pd.DataFrame.from_dict(aggregated_result, orient='index')\n",
    "\n",
    "print(final_result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5eed7737-09bd-4aa3-8a01-eddda20a58fc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
