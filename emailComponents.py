from email.message import EmailMessage
import time

password = 'thxzmehkqejpgcsd' # Recommend a temporary Gmail password or application password. Best case is a throwaway email account solely for this project.

emailMsg = EmailMessage()

# Assigning email headers to EmailMessage object
emailMsg['Subject'] = f'Cyber Security News Catchup {time.strftime("%Y-%m-%d")}'
emailMsg['From'] = "emailsenderbotforcybsec@gmail.com" # Please don't attempt to compromise this account, there is MFA!!
emailMsg['To'] = "htbuckley7@gmail.com"

def formatEmail(linkToArticle):
    # Returns the email formatted with scraped links
    email = f""" 
This week the catchup consists of:

{linkToArticle[0]}

{linkToArticle[1]}

{linkToArticle[2]}

{linkToArticle[3]}

{linkToArticle[4]}

{linkToArticle[5]}

{linkToArticle[6]}

{linkToArticle[7]}

{linkToArticle[8]}

{linkToArticle[9]}
"""   
    return email