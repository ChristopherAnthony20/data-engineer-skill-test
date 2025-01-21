{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1562b7e0-53c2-4a4a-bb91-539a13920ac0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   order_id  user_id order_date  product_id  price  quantity  total_amount  \\\n",
      "0         1      101 2023-01-12         501    100         2           200   \n",
      "1         2      102 2023-02-12         502    150         1           150   \n",
      "\n",
      "      category  \n",
      "0  Electronics  \n",
      "1    Furniture  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "\n",
    "file_path = 'skill_test.csv'\n",
    "df = pd.read_csv(file_path)\n",
    "\n",
    "df_cleaned = df.dropna()  \n",
    "df_cleaned = df_cleaned[df_cleaned['price'] > 0]  \n",
    "df_cleaned = df_cleaned[df_cleaned['quantity'] > 0]  \n",
    "\n",
    "df_cleaned['order_date'] = pd.to_datetime(df_cleaned['order_date'], errors='coerce', dayfirst=True)\n",
    "df_cleaned = df_cleaned.dropna(subset=['order_date'])  \n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "df_cleaned['total_amount'] = df_cleaned['price'] * df_cleaned['quantity']\n",
    "def get_category(product_id):\n",
    "    if product_id == 501:\n",
    "        return 'Electronics'\n",
    "    elif product_id == 502:\n",
    "        return 'Furniture'\n",
    "    else:\n",
    "        return 'Lain - Lain'\n",
    "\n",
    "df_cleaned['category'] = df_cleaned['product_id'].apply(get_category)\n",
    "\n",
    "\n",
    "print(df_cleaned)\n"
   ]
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
