from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def get_products(request):
    auth_header = request.headers.get('Authorization')
    try:
        products = Product.objects.all()
        print(products)
        serializer = ProductSerializer(products, many=True)
        print("<======================")
        print(serializer.data)
        print("======================>")
        for item in serializer.data:
            print(item['name']) # cara benar untuk akses data
            # print(item.name) # salah karena dictionary list
        print("++++++++++++++++")
        print(auth_header)
        return Response(serializer.data)
    except:
        return Response({"message":"Terjadi Kesalahan"})
        