from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse
from .models import PlaceInfo, Image
from django.forms.models import model_to_dict
from django.core import serializers
import json
from itertools import chain


def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoicnRrc28iLCJhIjoiY2txYW0wamMxMDl3YTJuazE2djgxeGM4NyJ9.ds9vMvs7PKzhP94Ln4R8XA'
    if request.method == "POST":
        if "place" in request.POST:
            plac = request.POST.get('place')
            q = PlaceInfo.objects.all().filter(place_name=plac)
            i = Image.objects.all().filter(place_id=plac)
            print(i)
            queryset = list(chain(q, i))        
            ser_query = serializers.serialize('json', queryset)
            print(ser_query)
            return JsonResponse(ser_query,safe=False)
    return render(request, 'default.html', 
                  { 'mapbox_access_token': mapbox_access_token })
# def default_map(request):
#     # TODO: move this token to Django settings from an environment variable
#     # found in the Mapbox account settings and getting started instructions
#     # see https://www.mapbox.com/account/ under the "Access tokens" section
#     mapbox_access_token = 'pk.eyJ1IjoicnRrc28iLCJhIjoiY2txYW0wamMxMDl3YTJuazE2djgxeGM4NyJ9.ds9vMvs7PKzhP94Ln4R8XA'
#     if request.method == "POST":
#         print(request.POST)
#         if "place" in request.POST:
#             print('1')
#             plac = request.POST.get('place')
#             print(plac)
#             q = PlaceInfo.objects.filter(place_name=plac).values('place_name', 'info_about_place')
#             i = Image.objects.filter(place_id=plac)

#             # for k,v in json_posts.items():
#             #     print(k, v)
#             # print()
#             # con = json.dumps([q])
#             # pl = serializers.serialize('json',con)
#             # im = serializers.serialize('json',i)
#             # print(json_posts.info_about_place)
#             print(type(q))

#             print(q)
#             return HttpResponse(q)
#     # print('reached')
#     # if request.method == 'POST':
#     #     print(request.POST)
#     #     print('is post')
#     #     for k,v in request.POST.items():
#     #         print(k, v)
#     #     return JsonResponse({'results':True})
    
#     return render(request, 'default.html', 
#                   { 'mapbox_access_token': mapbox_access_token })

