import urllib
from django.shortcuts import render
from django.views.generic import View
# from models import Music
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import urllib2,json
import requests


# Create your views here.
from dns import query


class MusicTrackDetails(View):

    def get(self, request):
        #Fetch the data
        response = urllib2.urlopen('http://104.197.128.152:8000/v1/tracks')
        data = response.read()
        get_data =  json.loads(data)
        # print get_data['results'][0]['id'],get_data['results'][0]['name']
        # print data
        # print get_data
        results =  get_data['results']
        # for i in results:
        #     print i["title"]

        return render(request, 'show_music_track.html', {'get_data': results})

class Add_Music_Details(View):
    def get(self, request):
        return render(request, 'add_music_track.html')
        # return HttpResponseRedirect(reverse('add_music_track.ht'))

    def post(self, request):
        title = request.POST['title']
        rating = request.POST['rating']
        genres = request.POST['genres']

        headers = {'content-type': 'application/json'}
        url = 'http://104.197.128.152:8000/v1/tracks'

        data = {
            "results": [
                {
                    "title": title,
                    "rating": rating,
                    "genres": [
                        {"name ": genres },
                                ]
                }
                        ]
        }
        requests.post(url, data=json.dumps(data), headers=headers)

        return HttpResponseRedirect(reverse('music_show'))



class EditMusicTrackDetails(View):

    def get(self, request, id):
        # Fetch the sighal data
        # print id,"id"
        # url = 'http://104.197.128.152:8000/v1/tracks/' + str(id)
        # # print url
        # response = urllib2.urlopen(url)
        # # print response,"okokokokokokokk"
        # data = response.read()
        # get_data = json.loads(data)
        # print get_data

        return render(request, 'edit_music_track.html')

    def post(self, request, id):
        title = request.POST['title']
        # genres = request.POST['genres']
        rating = request.POST['rating']

        headers = {'content-type': 'application/json'}
        url = 'http://104.197.128.152:8000/v1/tracks/' +str(id)

        data = {
                "results": [
                            {"id": id,
                            "title": title,
                            "rating": rating,
                            # "genres": [
                            #     {"name ": genres },
                            #  ]
                            }
                            ]
                }
        requests.post(url, data=json.dumps(data), headers=headers)

        return HttpResponseRedirect(reverse('music_show'))


class GenresDetails(View):

    def get(self, request):
        # Fetch the data
        response = urllib2.urlopen('http://104.197.128.152:8000/v1/genres')
        data = response.read()
        get_data = json.loads(data)
        # print get_data
        Results= get_data['results']
        # print Results,'result'

        return render(request, 'show_genres.html', {'get_data': Results})


class Add_Genres_Details(View):

    def get(self, request):

        return render(request, 'add_genres.html')

    def post(self, request):
        # name = request.POST['name']
        genres = request.POST['genres']
        # print name ,'name'
        # print genres, 'genres'

        headers = {'content-type': 'application/json'}
        url = 'http://104.197.128.152:8000/v1/genres'

        data = {

            "results": [
                {"name ": genres,}
             ]
         }
        requests.post(url, data=json.dumps(data), headers=headers)

        return HttpResponseRedirect(reverse('genres_show'))


class EditGenresDetails(View):
    def get(self, request, id):
        # Fetch the sighal data
        # print id,'id'
        url = 'http://104.197.128.152:8000/v1/genres/' + str(id)
        response = urllib2.urlopen(url)
        data = response.read()
        # print data,'databeforload'
        get_data = json.loads(data)
        print get_data

        return render(request, 'edit_genres.html', {'get_data': get_data})

    def post(self, request, id):
        id = request.POST['id']
        name = request.POST['name']
        print name
        headers = {'content-type': 'application/json'}
        url = 'http://104.197.128.152:8000/v1/genres' +str(id)

        data = {
            "id": id,
            "name": name,

        }
        requests.post(url, data=json.dumps(data), headers=headers)

        return HttpResponseRedirect(reverse('genres_show'))


def get_title_data(request):
    search_data=request.GET.get('get-data','')
    print search_data
    response = urllib2.urlopen('http://104.197.128.152:8000/v1/tracks?title=%s'%search_data)
    data = response.read()
    # get_data = json.loads(data)
    return HttpResponse(data)

