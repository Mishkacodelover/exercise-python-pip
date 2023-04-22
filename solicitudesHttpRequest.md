# Hacer solicitudes HTTPS con request

Para hacer solicitudes dede API con python, tenemos que instalar una librerñia
llamada request

1. pip3 install requests
2. creamos archivo store.py

```python


import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)

```

3. creamos archivo main.py para hacer el script

```python


import requests

import store

def run():
    store.get_categories()

if __name__ == '__main__':
    run()

```