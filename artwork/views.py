from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from artwork.models import Artwork
from artwork.serializers import ArtworkSerializer
from django.views import View


class ArtworkListView(View):
    '''
    View class to handle Artwork
    '''

    def get(self, request):
        '''
        Return Artworks list, depends on GET attr: category, type, author-username, author-first-name, author-last-name
        :param request:
        :return serialized list of Artwork objects:
        '''
        if (request.GET.get('category')):
            artworks = Artwork.objects.filter(category=request.GET.get('category'))
        elif (request.GET.get('type')):
            artworks = Artwork.objects.filter(type=request.GET.get('type'))
        elif (request.GET.get('author-username')):
            artworks = Artwork.objects.filter(author__username=request.GET.get('author-username'))
        elif (request.GET.get('author-first-name')):
            artworks = Artwork.objects.filter(author__first_name=request.GET.get('author-first-name'))
        elif (request.GET.get('author-last-name')):
            artworks = Artwork.objects.filter(author__last_name=request.GET.get('author-last-name'))
        else:
            artworks = Artwork.objects.all()
        serializer = ArtworkSerializer(artworks, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        '''
        Create new Artwork
        :param request:
        :return new serialzed artwork or error message:
        '''
        data = JSONParser().parse(request)
        serializer = ArtworkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
