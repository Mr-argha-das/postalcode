from django.http import JsonResponse
from .index import find_row

def getPostolData(request):
    param1 = request.GET.get('code', None)
    csv_file_path = 'myproject/pincode-dataset.csv'
    result_row = find_row(csv_file_path, param1)
    if result_row:
        return JsonResponse({'data':result_row})
    else :
        return JsonResponse({'data':None})
    