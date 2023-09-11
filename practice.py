import pandas as pd
data = [[1, 'aLice'], [2, 'bOB']]
users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    def fix(users):
        return users[0].upper()+users[1:].lower()
    users['name']=users['name'].apply(fix)
    users=users.sort_values(by='user_id')
    print(users)
fix_names(users)
