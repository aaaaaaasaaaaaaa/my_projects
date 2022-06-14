import os
import argparse
import requests
import bs4
from colorama import Fore



parser = argparse.ArgumentParser()
parser.add_argument("dir")
args = parser.parse_args()
search_stack = []
# f = open(f"{args.dir}/{search.split('.')[0]}", 'w')

os.makedirs(args.dir, exist_ok=True)


def gav(search_web, web):
    if search_web.status_code == 200:
        soap = bs4.BeautifulSoup(web, "html.parser")
        for i in soap.find_all("a"):
            i.string = "".join([Fore.BLUE, i.get_text(), Fore.RESET])
        web_res = soap.get_text()  # .split('\n')

        print(web_res)
        search_stack.append(web_res)
        f = open(f"{args.dir}/{search.split('.')[1]}", 'w', encoding="utf-8")
        f.write(web_res)
        f.close()
    else:
        print('Incorrect URL')

# if os.access("tb_tabs", os.F_OK):
#     shutil.rmtree("tb_tabs")


while True:
    search = input()

    if search == 'back':
        try:
            search_stack.pop()
            if len(search_stack) > 0:
                print(search_stack[-1])
        except IndexError:
            pass
    elif search != 'exit':

        if f"{search}" in os.listdir():
            file = open(f"{args.dir}/{search}", 'r')
            print(file.read())
            search_stack.append(file.read())
            file.close()
        else:
            if not search.startswith("https://"):
                search = "https://" + search
            try:
                search_web = requests.get(search)
                web = search_web.content
                # web.replace('<a', Fore.BLUE + '<a')
                gav(search_web, web)
            except requests.exceptions.ConnectionError:
                print("Incorrect URL")

    elif search == 'exit':
        exit()





