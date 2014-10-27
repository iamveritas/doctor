def get_redirect_url(request, default_url):

    if request.method == "get":
        return request.GET.get("next", default_url)
    else:
        return request.POST.get("next", default_url)