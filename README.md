## WorldData.AI
Python API wrapper for [WorldData.AI](https://worlddata.ai)

### Installation
- From pypi:
`pip3 install worlddata`
- From GitHub:
Clone our repository and `python3 setup.py install` Or `pip install git+https://github.com/worlddata-ai/python-api.git`
  

### Requirements
- [requests](https://github.com/kennethreitz/requests)

### Usage
```python
from pprint import pprint
from worlddata.worlddata import WorldData

worlddata = WorldData(auth_token = '1212312-12312312')
pprint(worlddata.search(search_text = 'worlddata'))
```

#### Connection pooling
If you are going to make a couple of request, you can user connection pooling provided by `requests`. This will save significant time by avoiding re-negotiation of TLS (SSL) with the chat server on each call.

```python
from requests import sessions
from pprint import pprint
from worlddata.worlddata import WorldData

with sessions.Session() as session:
    worlddata = WorldData(auth_token = '1212312-12312312')
    pprint(worlddata.search('worlddata'))
```
 

### Method parameters
Only required parameters are explicit on the WorldData class but you can still use all other parameters. For a detailed parameters list check the [WorldData.AI](https://documenter.getpostman.com/view/5099717/TzRa6jAj)

### API coverage
Most of the API methods are already implemented. If you are interested in a specific call just open an issue or open a pull request.

### Tests
We are actively testing :) 

### Contributing
You can contribute by doing Pull Requests. (It may take a while to merge your code but if it's good it will be merged). Please, try to implement tests for all your code and use a PEP8 compliant code style.

Reporting bugs and asking for features is also contributing ;) Feel free to help us grow by registering issues.

We hang out [here](WorldData.AI) if you want to talk. 
