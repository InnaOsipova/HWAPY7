from datetime import datetime


def write_log(data, mode):
    if mode == "k":
        edit_log(f'Операция с комплексными числами {datetime.now()} : {data}\n')
    else:
        edit_log(f'Операция с рациональными числами {datetime.now()} : {data}\n')
    


def edit_log(text):
    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(text)