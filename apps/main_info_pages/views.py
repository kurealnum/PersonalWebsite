import requests

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse


def index(request):
    template = loader.get_template('index.html')

    github_repos = {}

    #init repos here. names need to be exactly as they are on github
    repo_list = ["Non-Profit-Link", "Data-Structures-and-Algorithms", "Personal-Workflows"]

    for repo in repo_list:
        #get all the data
        repo_data = requests.get(f"https://api.github.com/repos/kurealnum/{repo}").json()
        repo_link = repo_data["html_url"]
        name = repo_data["full_name"]
        desc = repo_data["description"]
        lang = repo_data["language"]
        star_count = repo_data["stargazers_count"]
        fork_count = repo_data["forks_count"]

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
