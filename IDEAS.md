### backgrounds

Фоны будут распологаться в разных категориях папки `backgrounds`, 
все они вообщем будут иметь разные идентификаторы. 
Добавить идентификатор можно двумя способами:

- 1 способ

Через UI

- 2 способ 

Переместив в папку с фонами. Тогда? программа должна обнаружить инородный фон и дать ему свой ID

Создание разных идентификаторов:

```python
from random import randint

def generateId(num):
    """
    num - количество уже существующих фонов + 1
    num = {1 ... 256}
    """
    return str(hex(randint(0, 16*16*16*16)))[2:].zfill(4) + str(hex(num-1))[2:].zfill(2)

for i in range(16*16):
    generateId(i + 1)
```