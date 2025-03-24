# from .models import Category, Brand, Cart

# def menu(request):
#     categories = Category.objects.all()
#     brands = Brand.objects.all()
#     return {'categories': categories, 'brands': brands}

from django.db import connection

def cart_item_count(request):
    total_item = 0
    tenTaiKhoan = request.session.get('tenTaiKhoan')
    if tenTaiKhoan:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM CTGioHang WHERE TenTK = %s", [tenTaiKhoan])
            row = cursor.fetchone()
            total_item = row[0]
    return {'cart_item_count': total_item}
