import pandas as pd
data = {
    'user_id': [1, 2, 3, 4, 5, 6, 7],
    'name': ['Winston', 'Jonathan', 'Annabelle', 'Sally', 'Marwan', 'David', 'Shapiro'],
    'mail': [
        'winston@leetcode.com',
        'jonathanisgreat',
        'bella-@leetcode.com',
        'sally.come@leetcode.com',
        'quarz#2020@leetcode.com',
        'david69@gmail.com',
        '.shapo@leetcode.com'
    ]
}

df = pd.DataFrame(data)
def is_valid_email(email):
    return email.startswith('@') or (
        email.endswith('@leetcode.com') and
        all(c.isalnum() or c in ['_', '.', '-'] for c in email.split('@')[0])
    )
valid_emails = df[df['mail'].apply(is_valid_email)]
print(valid_emails)
