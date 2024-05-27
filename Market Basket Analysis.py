import pandas as pd
import numpy as np
from itertools import groupby, combinations
from collections import Counter


order_list = pd.read_csv('order_products__prior.csv')
order_list = order_list.set_index('order_id')
order_list = order_list['product_id']
products_names = pd.read_csv('products.csv')


def freq(df):
    return pd.Series(Counter(df)).rename('fr')
    
def total(df):
    return len(set(df.index))

def product_list(df):
    
    df = df.reset_index().values
    for order_id, group in groupby(df, lambda x: x[0]):
        products = [p[1] for p in group]
        
        for p in set(combinations(products, 2)):
            yield p
            

def Rules(df, min_support):
    
    stats = freq(df).to_frame('freq')
    stats['support'] = stats['freq'] / total(df) * 100
    
    qual_items = stats[stats['support'] >= min_support].index
    df = df[df.isin(qual_items)]
    
    size = freq(df.index)
    qual_prod = size[size >=2].index
    df = df[df.isin(qual_prod)]
    
    stats = freq(df).to_frame('freq')
    stats['support'] = stats['freq'] / total(df) * 100
    
    pairs = product_list(df)
    
    pair_stats = freq(pairs).to_frame('freqAB')
    pair_stats['supportAB'] = pair_stats['freqAB'] / len(qual_prod) * 100
    
    pair_stats = pair_stats[pair_stats['supportAB'] >= min_support]
    pair_stats = pair_stats.reset_index().rename(columns={'level_0': 'A', 'level_1': 'B'})
    
    Comb_stats = pair_stats.merge(stats.rename(columns = {'freq' : 'frA', 'support' : 'supA'}), left_on = 'A', right_index = True).merge(
        stats.rename(columns = {'freq' : 'frB', 'support' : 'supB'}), left_on = 'B', right_index = True)
    
    Comb_stats['Conf_AtoB'] = Comb_stats['supportAB'] / Comb_stats['supA']
    Comb_stats['Conf_BtoA'] = Comb_stats['supportAB'] / Comb_stats['supB']
    Comb_stats['Lift'] = (Comb_stats['Conf_AtoB'] / Comb_stats['supB'])
    
    return Comb_stats.sort_values('Lift', ascending= False)

def final(rules, products):
    p = (rules.merge(products.rename(columns = {'product_name' : 'ProductA'}), left_on = 'A', right_on = 'product_id').merge(
        products.rename(columns = {'product_name' : 'ProductB'}), left_on = 'B', right_on = 'product_id'))
    columns = ['ProductA', 'ProductB', 'supA', 'supB', 'Conf_AtoB', 'Lift']
    
    return p[columns].sort_values('Lift', ascending=False)



rules = Rules(order_list, 0.01)
Final_Rules = final(rules, products_names)