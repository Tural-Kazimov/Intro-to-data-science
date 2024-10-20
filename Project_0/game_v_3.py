# данная программа будет работать следующим образом.
# компьютер будет сам загадывать число и с помощью алгоритма постарается отгадать данное 
# слово за минимальное количество попыток. Лимит : 20 попыток.

def predict_number(number:int=1) -> int:
    """Компьютер загадывает рандомно некое число. Далее сам отгадывает его по следующему
    алгоритму: будет представлен отрезок где выбирется рандомно число. Далее если полусумма 
    концов отрезка будет равна предполагаемому числу то цикл завершился. В противном случае
    если рандомное число больше или меньше полусуммы то отрезок примет слудущий вид :
    если предполагаемое число больше полусуммы началом отрезка станет результат полусуммы а
    концом конец предыдущего отрезка. Если же меньше то начало остается таким какой есть а 
    конец меняется результат полусуммы и так пока цикл не завершится.
    
    Args:
        number (int, optional): Рандомное число. Defaults to 1.

    Returns:
        int: количество попыток
    """
    attempts = 0 #Количество попыток
    right_border, left_border = 0, 101 # Границы отрезка
    half_a_sum = (right_border + left_border)//2 # Полусумма, которая является результатом
    if number == half_a_sum:
        attempts = 1
        result = f"Компьютер отгадал число за {attempts} попыток"
    else:
        while number != half_a_sum:
            if number > half_a_sum:
                right_border = half_a_sum
                half_a_sum = (right_border + left_border)//2
            elif number < half_a_sum:
                left_border = half_a_sum
                half_a_sum = (right_border + left_border)//2

            attempts += 1
    result = f"Компьютер отгадал число за {attempts} попыток"
    return result