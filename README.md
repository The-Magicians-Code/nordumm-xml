# NordPool data to XML from UMM with Python 3
This script enables one to do what the title says  
Run:  
```pipenv install``` to recreate the configured virtual environment  
```pipenv run python3 main.py --url https://ummapi.nordpoolgroup.com/messages -l 1 -e```  
```--url``` Self explanatory, from nordpool  
```-l``` or ```--limit``` Maximum number of desired results  
```-e``` or ```--export``` Exports to ```outputs/result[0..n].xml``` files
### One can also
```python
from main import get_data, convert

# Export to file
# get_data("https://ummapi.nordpoolgroup.com/messages", export=True)

# Or gather to an object
data_json = get_data("https://ummapi.nordpoolgroup.com/messages")
print(data_json)

# you can do both at the same time too
# data_json = get_data("https://ummapi.nordpoolgroup.com/messages", export=True)

# Convert it to XML
data_xml = convert(data_json)
print(data_xml)
```