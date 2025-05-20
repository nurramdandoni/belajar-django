from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializersProduct import ProductSerializer

@api_view(['GET','POST'])
def dataProducts(request):
    auth_header = request.headers.get('Authorization')
    try:
        if request.method == 'GET':
            products = Product.objects.all()
            print(products)
            serializer = ProductSerializer(products, many=True)
            # for item in serializer.data:
            #     print(item['name']) # cara benar untuk akses data
            #     # print(item.name) # salah karena dictionary list
            # print("++++++++++++++++")
            # print(auth_header)
            return Response(serializer.data,status=200)
        elif request.method == 'POST':
            bodyRequest = request.data
            dataSerializer = ProductSerializer(data=bodyRequest)
            validRequest = dataSerializer.is_valid()
            
            if validRequest:
                dataSerializer.save()
                return Response({"data":bodyRequest},status=200)
            else:
                return Response({"message":"Invalid Request"},status=400)
                
    except:
        return Response({"message":"Terjadi Kesalahan Saat Menerima Request"},status=500)
    
@api_view(['GET','PUT','DELETE'])
def dataProductsDetail(request, id):
    auth_header = request.headers.get('Authorization')
    try:
        product = Product.objects.get(pk=id)
        
        if request.method == 'GET':
            serializer = ProductSerializer(product)
            return Response(serializer.data,status=200)
        elif request.method == 'PUT':
            bodyRequest = request.data
            dataSerializer = ProductSerializer(product,data=bodyRequest)
            validRequest = dataSerializer.is_valid()
            
            
            if validRequest:
                dataSerializer.save()
                return Response({"data":bodyRequest},status=200)
            else:
                return Response({"message":"Invalid Request"},status=400)
        elif request.method == 'DELETE':
            product.delete()
            return Response({"message":"Data Berhasil Dihapus"},status=200)
    except:
        return Response({"message":"Data Tidak Ditemukan"},status=404)
            