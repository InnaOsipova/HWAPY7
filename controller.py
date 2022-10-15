import csv
import complex_calc as cl
import rational_calc as rt
import log

def ask_user():
    choise = input("С какими числами работаем косплексные / рациональные (k/r/): ")
    if choise == "k":
        log.write_log(cl.calc(), "k")
    elif choise == "r":
        log.write_log(rt.calc(), "r")
    else:
        print("Неизвестная команда")