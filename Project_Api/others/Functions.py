import random
import unicodedata
class Functions:
    def __init__(self):
        pass

    def generate_ramdom_code(self,n=6):
        return str(random.randint(10**(n-1),10**n-1))
    
    def remove_acents(self,text):
        text_normalize = unicodedata.normalize('NFKD', text)
        return ''.join(c for c in text_normalize if unicodedata.category(c) != 'Mn')