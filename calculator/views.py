from django.shortcuts import render, reverse

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

def recipe_show(request, name_recipe):
    servings = int(request.GET.get("servings", 1))
    recipe = DATA.get(name_recipe).copy()
    for ingr in DATA.get(name_recipe):
        recipe[ingr] = DATA.get(name_recipe).get(ingr) * servings

    context = {
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)

def home(request):
    pages = {}
    for recipe in DATA.keys():
        pages[recipe] = recipe + '/'

    context = {
        'pages': pages
    }
    return render(request, 'calculator/home.html', context)