import re 

input = str(input('Введите свой e-mail адрес:'))

text = r"^(?!\.)(?!.*\.@)(?!.*\.\.)[\w.!#  %&'*+—/=?^_`{|}~]+@(?!\-)[\w{63}\-]+[\w.]+(?!\-)$"
result = re.match(text, input) is not None
print(result)
