from main import get_data, convert

# Export to file
# get_data("https://ummapi.nordpoolgroup.com/messages", export=True)

# Or gather to an object
data_json = get_data("https://ummapi.nordpoolgroup.com/messages")

# you can do both at the same time too
# data_json = get_data("https://ummapi.nordpoolgroup.com/messages", export=True)

# Convert it to XML
data_xml = convert(data_json)
print(data_xml)