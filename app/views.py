from django.shortcuts import render
from django.http import HttpResponse
import urllib2
import json
# Create your views here.

def home(request):
	try:
		f = urllib2.urlopen("http://congresorest.appspot.com/diputado/3")
		g = f.read()
		f.close()
	except HTTPError, e:
		g = "Error"
		g = e.code
	except URLError, e:
		g = "Error"
		g = e.code
	dictionario = json.loads(g)
	return HttpResponse(dictionario["entidad"])

def home2(request):
	return HttpResponse("Otro mundo <.<")

def post(request, id_post):
	if int(id_post) > 10:
		return HttpResponse("Este numero es mayor a 10 : %s" % id_post)
	elif int(id_post) < 10:
		return HttpResponse("Este numero es menor a 10 : %s" % id_post)
	else:
		return HttpResponse("Este numero es igual a 10 : %s" % id_post)


def live(request, id1, id2):
	return HttpResponse("Este es el post %s y %s" % (id1,id2))

def request(request):
	return HttpResponse("Este es el %s" % request)
