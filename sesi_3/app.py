# def get_personal_info(name='bayu', age=23):
#     return [name, age]  # return in list


# # can insert a parameters or not
# info = get_personal_info('bayu aji nurmansah', 23)
# info2 = get_personal_info()  # can insert a parameters or not
# info3 = get_personal_info(age=18, name='bayu aji')
# print(info, info2, info3)

# ============================================== 2

# * symbol means that variable can receive multiple length [list]
def buy(customer_name, *items):
    c = [x for x in items]
    return items


item = buy('name', 'egg', 'coconut', 'watermelon')
print(item)

# ** symbol means it will save to dict


# def person_car(total_data, **kwargs):
#     '''Create a function to print who owns what car'''
#     print('Total Data : ', total_data)
#     for key, value in kwargs.items():
#         print('Person : ', key)
#         print('Car    : ', value)
#         print('')


# person_car(3, jimmy='chevrolet', frank='ford', tina='honda')
# person_car(10)
