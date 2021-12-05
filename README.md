## O que é?

Basicamente esta é uma extensão para a biblioteca python 'keyboard'

## O que ela faz?

Adiciona a opção de verificar se multiplas teclas foram pressionadas ao mesmo tempo

## Demonstração

```py
from hotkey import hotkey

while True:
	if hotkey('ctrl','shift') == True:
		print("feito.")
		break
```

obs: pode ser com quantas teclas precisar, não se limite a apenas duas.