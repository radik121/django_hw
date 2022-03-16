from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'baked_potato': {
        'Картофель, кг': 1,
        'Чеснок, зубчик': 3,
        'Сыр гаудаб, г': 100,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def hello(request):
    return HttpResponse("""Приветствую!<p>Допишите в адресе необходимое блюдо:
    omlet, pasta, buter, baked_potato""")


def ingredients(request, dish):
    servings = request.GET.get('servings')
    if servings and int(servings) != 0:
        ingred = {}
        for k, v in DATA[dish].items():
            ingred[k] = v * int(servings)
        context = {
            'recipe': ingred
        }
    else:
        context = {
            'recipe': DATA[dish]
        }
    return render(request, 'calculator/index.html', context)
