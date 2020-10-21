from jsonstream import loads 
import sys
import requests

def open_file():
    with open(sys.argv[1]) as json_dump:
        final = loads(json_dump.read())

        lista_final = list(final)

        return

def check_status_code(image):
    r = requests.get(image)

    return r.status_code

def check_args_passes():
    try:
        sys.argv[1]
        return True
    except:
        print("Please, pass a valid json file, example: python main.py input.json")


if __name__ == "__main__":
     if check_args_passes():
        open_file()