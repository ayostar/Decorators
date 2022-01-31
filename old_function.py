import os
from Log_tools import log_decorator
from Param_log_tools import param_decor


data_dish, data_person = ['Омлет', 'Омлет', 'Омлет', 'Запеченный картофель', 'Фахитос'], 1
recepies_file = os.path.join(os.getcwd(), 'recipies.txt')
log_path = os.path.join(os.getcwd(), 'logs')


@param_decor(parameter = log_path)
# @log_decorator
def get_shop_list_by_dishes(dishes, person_count, file_path):
    with open(file_path, encoding = 'utf-8') as file:
        shop_list = {}
        same_dishes_count_dict = {dish: dishes.count(dish) for dish in dishes}

        for book in file:
            dish_name = book.strip()
            if dish_name in same_dishes_count_dict.keys():
                dish_name_count = same_dishes_count_dict.get(dish_name)
                amount_of_ingridients = int(file.readline().strip())

                for item in range(amount_of_ingridients):
                    ingridient, quantity, measure = file.readline().split('|')
                    quantity = int(quantity)
                    if ingridient in shop_list.keys():
                        current_ingridietnt_quantity = shop_list[ ingridient ].get('quantity')
                        shop_list[ ingridient ] = {'quantity': quantity + current_ingridietnt_quantity}
                    else:
                        shop_list[ ingridient ] = {'measure': measure.strip(),
                                                   'quantity': quantity * person_count * dish_name_count}
                file.readline()
            else:
                amount_of_lines_to_pass = int(file.readline().strip())
                for line in range(amount_of_lines_to_pass):
                    file.readline()
                file.readline()

        return shop_list


print(get_shop_list_by_dishes(data_dish, data_person, recepies_file))

# Проверка на вшивость
# @log_decorator
# def summator(x, y):
#     return x + y
#
# three = summator(1, 2)
#
# five = summator(2, 3)
#
# result = summator(three, five)
#
# print('result: ', result)
# print('result type: ', type(result))


