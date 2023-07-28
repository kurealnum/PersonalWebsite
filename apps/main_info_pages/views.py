import requests, environ

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse


# getting env stuff
env = environ.Env()
environ.Env.read_env()
github_token = env('GITHUB_TOKEN')


def index(request):
    template = loader.get_template('index.html')

    github_repos = {}

    #init repos here. names need to be exactly as they are on github
    headers = {'Authorization': 'token ' + github_token}
    all_repo_data = requests.get("https://api.github.com/users/kurealnum/repos", headers=headers).json()
    repos = [all_repo_data[i]["name"] for i in range(len(all_repo_data))]   

    for i in range(len(repos)):
        if all_repo_data[i]["name"] == "kurealnum":
            continue
        
        #get all the data
        repo_link = all_repo_data[i]["html_url"]
        name = all_repo_data[i]["full_name"]
        desc = all_repo_data[i]["description"]
        lang = all_repo_data[i]["language"]
        star_count = all_repo_data[i]["stargazers_count"]
        fork_count = all_repo_data[i]["forks_count"]

        github_repos[name] = [desc, lang, star_count, fork_count, repo_link]
        # (index) 0 is description, 1 is the language, 2 is the star count, 3 is the fork count, 4 is the link

    context = {
        "github_repos": github_repos,
    }

    return HttpResponse(template.render(context, request))


def layout(request):
    #basic variables
    template = loader.get_template('layout.html')
    referer_url = request.META.get('HTTP_REFERER')

    #if we're coming from "/", just redirect to our index page
    if not referer_url:
        return redirect("index")

    return HttpResponse(template.render())
