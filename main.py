# Request XML/JSON data from NordPool UMM API with Python
# Author: Tanel Treuberg (The-Magicians-Code)
import requests
import argparse
from xmltodict import unparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument(
    "-u", "--url",
    type=str,
    default="",
    help="NordPool URL"
)
parser.add_argument(
    "-l", "--limit",
    type=int,
    default=10,
    help="Number of requested items"
)
parser.add_argument(
    "-e", "--export",
    nargs='?',
    const=True,
    help="Automagically puts requested items into files"
)
args = parser.parse_args()

def convert(input_data):
    """
    Convert JSON to XML

    :param input_data: The incoming json document as a list
    :type input_data: list of str

    :return: XML list
    :rtype: list of str
    """
    return [unparse({"document": input_data[i]}, pretty=True) for i in range(len(input_data))]

def get_data(url, limit=10, export=None):
    """
    Get data from URL and write it to a file if requested

    Args:
        args (argparse arguments): export, url

    Returns:
        result (str): data as a dict object
    """
    
    if not url:
        raise ValueError("You have not provided an URL")
    
    headers = {
    "Accept": "application/json"
    }
    params = {
        "status": "Active", 
        "limit": limit
    }
    print("Requesting data...")
    result = requests.get(url, headers=headers, params=params).json()
    print("Data received")
    data = convert(result["items"])
    if export:
        print("Exporting data to outputs/ folder...")
        if not Path("outputs").exists():
            Path("outputs").mkdir(exist_ok=True)
        for i, value in enumerate(data):
            with open(f"outputs/result{i}.xml", "w") as file:
                file.write(value)
        print("Data written to file(s)")
    print("Done")
    return result["items"]

if __name__ == "__main__":
    get_data(args.url, args.limit, args.export)