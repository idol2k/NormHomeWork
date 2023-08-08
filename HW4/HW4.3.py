from typing import List, Dict

def cou(listik: List[int]) -> Dict[int, int]:
    number: Dict[int, int] = {}

    for num in listik:
        count: int = number.get(num, 0)

        count += 1

        number[num] = count

    return number
nomera: List[int] = (1, 3, 5 ,1 ,2 ,4 ,1 ,2 ,3) 
polychilsya_dict: Dict[int, int] = cou(nomera)
print(polychilsya_dict)