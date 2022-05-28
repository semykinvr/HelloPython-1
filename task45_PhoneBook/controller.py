import ui
import log

def run():
    temp = ui.initial()
    print(type(temp))
    print("Было введено: ", temp)
    log.log_to_file(temp[0], temp[1], temp[2], temp[3], temp[4])
    