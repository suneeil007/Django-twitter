from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect

from emails.forms import InventoryWaitlistForm

from .forms import ProductModelForm
from .models import Product

def featured_product_view(request, *args, **Kwargs):
    qs = Product.objects.filter(featured=True)
    product = None
    form = None
    can_order = False
    if qs.exists():
        product = qs.first()
    if product != None:   
        can_order = product.can_order 
        if can_order:
             product_id = product.id
             request.session['product_id'] = product_id    
    form = InventoryWaitlistForm(request.POST or None, product=product)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.product = product
        if request.user.is_authenticated:
            obj.user = request.user
        obj.save()
        return redirect("/witlist-success")    
    context = {
        "object": product,
        "can_order": can_order,
        "form": form,
    }
    return render (request, 'products/detail.html', context)    

# Create your views here.

# def bad_view(request, *args, **Kwargs):
#     print(dict(request.GET))
#     my_request_data = dict(request.GET)
#     new_product = my_request_data.get("new_product")
#     print(my_request_data, new_product)
#     if new_product[0].lower() == "true":
#         print("new product")
#         Product.objects.create(title=my_request_data.get('title')[0], content=my_request_data.get('content')[0])
#     return HttpResponse("Dont do this")



def search_view(request, *args, **Kwargs):
    # return HttpResponse('<h2>hello world</h2>')
    query = request.GET.get('q')
    qs = Product.objects.filter(title__icontains=query[0])
    print(query, qs)
    context = {"name": "Suneeil"}
    return render(request, "home.html", context)

# def product_create_view(request, *args, **Kwargs):
#     # print(request.POST)
#     # print(request.GET) 
#     if request.method == 'POST':
#         post_data = request.POST or None
#         if post_data != None:
#             my_form = ProductForm(request.POST)
#             if my_form.is_valid():
#                 # print(my_form.cleaned_data.get('title'))
#                 title= my_form.cleaned_data.get('title')
#                 Product.objects.create(title=title)
#                 # print('post_data', post_data)
#     return render(request, "forms.html", {})    

@staff_member_required
def product_create_view(request, *args, **Kwargs):
    form = ProductModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        image = request.FILES.get('image')
        media = request.FILES.get('media')
        # do some stuff
        if image:
            obj.media = media
        if media:    
            obj.image = image
        obj.user = request.user
        obj.save()
        # print(form.cleaned_data)
        # data = form.cleaned_data
        # Product.objects.create(**data)
        form = ProductModelForm()
        # return HttpResponseRedirect('/success')
        # return render('/success')
    return render(request, 'forms.html', {'form': form})

def product_detail_view(request, id):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    # return HttpResponse(f"Product id {obj.id}")    
    return render(request, "products/detail.html", {"object": obj})

def product_list_view(request, *args, **Kwargs):
    qs = Product.objects.all()
    context = {"object_list": qs}
    return render(request, "products/list.html", context)

def product_api_detail_view(request, id=id):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"})
    return JsonResponse({'id': obj.id})     
