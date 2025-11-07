import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df=world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return df[['name', 'population', 'area']]
    # res=[]
    # for index, row in world.iterrows():
    #     if row['area']>=3000000 or row['population']>=25000000:
    #         res.append({
    #             'name': row['name'],
    #             'population': row['population'],
    #             'area': row['area']}
    #         )
    # res=pd.DataFrame(res)
    # return res