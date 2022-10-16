from glob import glob
from pathlib import Path

# fa = open("123.txt", "w")
# print (type(fa))

begin = True
while begin:
    
    print ('------ \n Введите число для соответствующей задачи или иное для выхода: ')
    print ('   1.\t Найдёт сумму элементов списка, стоящих на нечётной позиции.')
    print ('   2.\t Найдёт произведение пар чисел списка.')
    print ('   3.\t Найдёт разницу между максимальным и минимальным значением дробной части элементов.')
    print ('   4.\t Будет преобразовывать десятичное число в двоичное.')
    print ('   5.\t Список чисел Фибоначчи, в том числе для отрицательных индексов.')

    program = int(input())
    print ()

    if program == 1:
        # with open(glob('*3_1*')[0]) as f:
        #     for i in f:
        #         print(i, end = '')
        
        # f = Path(glob('*3_1*')[0]).stem
        # print (f)
        import HWork_3_1_EverySecond
    
    elif program == 2:
        import HWork_3_2_PairMultiplication
    elif program == 3:
        import HWork_3_3_Difference_Decimal
    elif program == 4:
        import HWork_3_4_DecToBin
    elif program == 5:
        import HWork_3_5_Fibo
    else:
        begin = False
