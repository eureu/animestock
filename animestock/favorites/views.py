from django.shortcuts import render, redirect

# Create your views here.

def add_to_favorites(request, id):
    if request.method == "POST":
        if not request.session.get('favorites'):
            request.session['favorites'] = list()
        else:
            request.session['favorites'] = list(request.session['favorites'])

        item_exist = next((item for item in request.session['favorites'] if item["type"] == request.POST.get('type') and item["id"] == id), False)
        # print(item_exist)

        #get ids list only if needs
        # favorites_ids_list = list()
        # for item in request.session['favorites']:
        #     favorites_ids_list.append(item['id'])

        add_data = {
            'type' : request.POST.get('type'),
            'id' : id
        }

        #if id not in favorites_ids_list:
        if not item_exist:
            request.session['favorites'].append(add_data)
            request.session.modified = True
    return redirect(request.POST.get('url_from'))


def remove_from_favorites(request, id):
    #delete item from favorites
    if request.method == "POST":
        for item in request.session['favorites']:
            if item["type"] == request.POST.get('type') and item["id"] == id:
                item.clear()
            
        #remove empty {} from favorites list
        while {} in request.session['favorites']:
            request.session['favorites'].remove({})
        

        #remove favorites if favorites list is empty
        if not request.session['favorites']:
            del request.session['favorites'] 
            # request.session.modified = True

        request.session.modified = True
    return redirect(request.POST.get('url_from'))



