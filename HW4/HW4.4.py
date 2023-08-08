from datetime import datetime
import time
from typing import List

def dai_vremya_seichas() -> str:
    time.sleep(1)
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
def dai_list() -> List[str]:
    n = int(input('Введите кол-во:'))
    return [dai_vremya_seichas() for chto in range(n)]
resultat = dai_list()
print(resultat)