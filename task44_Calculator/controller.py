import calc_complex
import calc_float
import ui
import log


def run():
    temp = ui.initial()
    #print('тип данных после функции initial:' , type(temp))
    # проверку на комплексные числа закоментарил:
    # if 'j' in temp[0] and 'j' in temp[1]:
    #     result = calc_complex.calc(temp[0], temp[1], temp[2])
    # else:
    result = calc_float.calc(temp[0], temp[1], temp[2])
    print(f'Результат операции: {round(result, 2)}\n')
    log.write_to_file(temp, result)
    return result
