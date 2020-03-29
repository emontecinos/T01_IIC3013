from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Episode,Character,Location
import requests
import json


def index(request):
    eps_json=get_episodes()
    episode_list = []
    for ep in eps_json:
        char_list = []
        episode_list.append(Episode(api_id=ep["id"],name=ep["name"],air_date=ep["air_date"],ep_code=ep["episode"],characters=[],api_url=ep["url"]))
    context = {
        'episode_list': episode_list,
    }
    return render(request,'rickmorty/index.html',context)

def episode_detail(request, episode_api_id):
    ep = get_episode(episode_api_id)
    char_list = []
    chars_ids = ''
    for ch_url in ep["characters"]:
        chars_ids+=ch_url.split("/")[-1]
        chars_ids+=','
    chars_json = get_characters(chars_ids)
    for c in chars_json:
        char_list.append(Character(api_id=c["id"],name=c["name"],status="",species="",char_type="",gender="",origin="",location="",image=c["image"],episodes="",api_url=c["url"]))
    episode = Episode(api_id=ep["id"],name=ep["name"],air_date=ep["air_date"],ep_code=ep["episode"],characters=[],api_url=ep["url"])
    
    context = {
        'character_list': char_list,
        'episode':episode,
    }
    return render(request,'rickmorty/episode_detail.html',context)

def character_detail(request, character_api_id):
    c = get_characters(str(character_api_id))
    character = Character(api_id=c["id"],name=c["name"],status=c["status"],species=c["species"],char_type=c["type"],gender=c["gender"],origin=c["origin"],location=c["location"],image=c["image"],episodes=c["episode"],api_url=c["url"])
    episodes = []
    ep_ids=""
    eps_ids_names = {}
    for ep in character.episodes:
        ep_ids += "{},".format(ep.split("/")[-1])
    episodes = get_episode(ep_ids)
    for e in episodes:
        if e["id"]:
            eps_ids_names[str(e["id"])]=e["name"]
    location = c["location"]
    location["id"]=c["location"]["url"].split("/")[-1]
    origin = c["origin"]
    origin["id"]=c["origin"]["url"].split("/")[-1]
    context={
        'character':character,
        'location_name':location["name"],
        'location_id':location["id"],
        'origin_name':origin["name"],
        'origin_id':origin["id"],
        'episodes_ids_names': eps_ids_names,
    }
    return render(request,'rickmorty/character_detail.html',context)

def location_detail(request, location_api_id):
    l = get_location(location_api_id)
    char_list = {}
    chars_ids = ''
    for ch_url in l["residents"]:
        chars_ids+="{},".format(ch_url.split("/")[-1])
        chars_ids+=','
    chars_json = get_characters(chars_ids)
    if (chars_json):
        for c in chars_json:
            char_list[c["id"]]=c["name"]
    location = Location(api_id=l["id"],name=l["name"],loc_type=l["type"],dimension=l["dimension"],residents=[],api_url=l["url"])
    context = {
        'character_list': char_list,
        'location':location,
    }
    return render(request,'rickmorty/location_detail.html',context)

def search(request):
    #episodios
    text = request.GET.get("search")
    ep_dic={}
    e=get_episode("")
    for e_url in e["results"]:
        if text.upper() in e_url["name"].upper():
            ep_dic[e_url["id"]]=e_url["name"]
    #characters
    ch_dic={}
    c=get_characters('')
    for c_url in c["results"]:
        if text.upper() in c_url["name"].upper():
            ch_dic[c_url["id"]]=c_url["name"]
    #locations
    lo_dic={}
    l=get_location('')
    for l_url in l["results"]:
        if text.upper() in l_url["name"].upper():
            lo_dic[l_url["id"]]=l_url["name"]

    context={
        'episode_dict':ep_dic,
        'character_dict':ch_dic,
        'location_dict':lo_dic,
        'text':text,
    }
    return render(request,'rickmorty/search_res.html',context)


##Requests de la busqueda
def generate_request(url,params={}):
    response = requests.get(url,params=params)
    if response.status_code==200:
        data = json.loads(response.text.encode("utf-8"))
        return data

def get_episodes(params={}):
    response = generate_request('https://rickandmortyapi.com/api/episode/',params)
    if response:
        return response["results"]

def get_episode(ep_id):
    response = generate_request('https://rickandmortyapi.com/api/episode/{}'.format(ep_id))
    if response:
        return response

def get_characters(chars_ids):
    response = generate_request('https://rickandmortyapi.com/api/character/{}'.format(chars_ids))
    if response:
        return response

def get_location(location_id):
    response = response = generate_request('https://rickandmortyapi.com/api/location/{}'.format(location_id))
    if response:
        return response