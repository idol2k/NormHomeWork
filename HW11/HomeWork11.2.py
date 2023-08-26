import re 
input = str(input('Введите свой e-mail адрес:'))    
def e_mail(self):
    text = r"^(?!\.)(?!.*\.@)(?!.*\.\.)[\w.!#  %&'*+—/=?^_`{|}~]+@(?!\-)[\w{63}\-]+[\w.]+(?!\-)$"
    result = re.match(text, input) is not None
    print(result)
e_mail(input)