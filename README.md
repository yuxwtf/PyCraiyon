# PyCraiyon
PyCraiyon Is an API Wrapper of craiyon.com Drawing AI, With That AI You Can Generate Literaly Everthing With A Advanced Drawing Artificial Intelligence.

# Docs

Craiyon.generate(prompt, 0, save-path)
- Prompt = Setance you want to draw (ex: a cat)
- 0 = A number from 0-8 (result image choice) (ex: 0)
- save-path = Drawed Image Output Path (ex: ./data/result.png)

# Exemple

```
from pycraiyon import Craiyon

prompt = "Yux Making An API Wrapper" # your prompt
Craiyon.generate(str(prompt), 0, 'result.png')
```
