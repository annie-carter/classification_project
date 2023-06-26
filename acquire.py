import pandas as pd
import os as os
import csv
from env import user, password, hostname, get_db_url

def get_telco_data(df):
    filename = "telco.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('''SELECT *
                            FROM customers
                            JOIN contract_types USING (contract_type_id)
                            JOIN internet_service_types USING (internet_service_type_id)
                            JOIN customer_subscriptions USING (customer_id)
                            JOIN customer_payments USING (customer_id)
                            JOIN customer_contracts USING(customer_id)
                            JOIN customer_signups USING (customer_id)''',
                         url=get_db_url('telco_churn'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename, index=False)

        # Return the dataframe to the calling code
        return df
    
def telco_data_acquire(telco_df):
    print(telco_df.info())
    print('                        ')
    print(telco_df.describe())
    print('                        ')
    print(telco_df.describe(include='object').T)
    print('                        ')
    print('The telco data used for this project has', telco_df.shape[0], 'rows and', telco_df.shape[1], 'columns')
    print('                        ')
    print('This was the initial exploration of acquired data')
    return telco_df