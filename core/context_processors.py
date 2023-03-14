from vendas.models import Category, Product

def categories(request):
    return {
        'categories': Category.objects.all()
    }

# def Products(request):
#     return {
#         'products': Product.objects.all()
#     }