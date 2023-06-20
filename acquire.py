{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5fa08b70",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import os as os\n",
    "import csv\n",
    "from env import get_db_url\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b745b8e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_telco_data():\n",
    "#     '''\n",
    "#     # Retrieves the telco dataset either from the codeup server or a csv if its already been imported, returns a dataframe\n",
    "#     '''\n",
    "    url = get_db_url('telco_churn')\n",
    "    query = '''SELECT *\n",
    "             FROM customers\n",
    "             JOIN payment_types USING (payment_type_id)\n",
    "             JOIN contract_types USING (contract_type_id)\n",
    "             JOIN internet_service_types USING (internet_service_type_id);'''\n",
    "    filename = 'telco.csv'\n",
    "    if os.path.isfile(filename):\n",
    "        return pd.read_csv(filename)\n",
    "    else:\n",
    "        df = pd.read_sql(query, url)\n",
    "        df.to_csv(filename)\n",
    "        return df\n",
    "\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3a2f509f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_telco_data():\n",
    "    filename = \"telco.csv\"\n",
    "    if os.path.isfile(filename):\n",
    "        return pd.read_csv(filename)\n",
    "    else:\n",
    "        # read the SQL query into a dataframe\n",
    "        df = pd.read_sql('''SELECT *\n",
    "                            FROM customers\n",
    "                            JOIN contract_types USING (contract_type_id)\n",
    "                            JOIN internet_service_types USING (internet_service_type_id)\n",
    "                            JOIN customer_subscriptions USING (customer_id)\n",
    "                            JOIN customer_contracts USING(customer_id)\n",
    "                            JOIN customer_payments USING (customer_id)\n",
    "                            JOIN customer_signups USING (customer_id)''',\n",
    "                         url=get_db_url('telco_churn'))\n",
    "\n",
    "        # Write that dataframe to disk for later. Called \"caching\" the data for later.\n",
    "        df.to_csv(filename, index=False)\n",
    "\n",
    "        # Return the dataframe to the calling code\n",
    "        return df\n"
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
