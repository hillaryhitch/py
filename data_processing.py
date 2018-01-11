import pandas as pd
from dateutil import relativedelta

df_whole_data = pd.read_csv('data/R_months_by_months.csv')
df_whole_data['NR_ORGN'] = df_whole_data['NR_ORGN'].apply(lambda x: str(int(x)))
df_whole_data['months'] = df_whole_data['months'].apply(lambda x: str(x)[:4] + '/' + str(x)[4:] + '/' + '01')


list_months = sorted(list(set(df_whole_data['months'])))

# for each_person in list_nr:
#    for j in range(1,len(list_months)+1):
#        for k in range(1,j):
#            df[(df['NR_ORGN']==each_person) & (df['months']==j)]['NR_DSTN_count_' + str(j-k)]=df[(df['NR_ORGN']==each_person) & (df['months']==j)]['NR_DSTN_count']



grouped_whole_data = df_whole_data.groupby(['NR_ORGN', 'months'])

for index, row in df_whole_data.iterrows():
    if index % 10000 == 0:
        print(index)
    row_month = row['months']
    row_nr = row['NR_ORGN']

    if row_month != list_months[0]:
        index_row_month = list_months.index(row_month)
        for k in range(0, index_row_month):
            lookup_month = list_months[k]

            index_lookup = grouped_whole_data.groups[row_nr, lookup_month][0]
            x = relativedelta.relativedelta(pd.to_datetime(row_month,
                                                       infer_datetime_format=True), pd.to_datetime(lookup_month,
                                                                                                        infer_datetime_format=True))
            df_whole_data.set_value(index, 'NR_DSTN_count_' + str(x.months),
                                                                      df_whole_data.ix[index_lookup]['NR_DSTN_count'])


    pass

pass