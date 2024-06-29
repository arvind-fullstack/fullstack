from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from .models import *
from django.contrib.auth.hashers import make_password,check_password
def index(request):
    if request.method == 'POST':
        product_id=request.POST.get('product_id')
        remove=request.POST.get('remove')

        cart_id=request.session.get('cart')

        if cart_id:

            quantity= cart_id.get(product_id)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart_id.pop(product_id)
                    else:
                        cart_id[product_id] = quantity - 1
            
    
                else:
                   cart_id[product_id] = quantity + 1
            else:
                cart_id[product_id] = 1
        else:
          cart_id = {}
          cart_id[product_id] = 1
        
        request.session['cart'] = cart_id


    category_id = request.GET.get('category_id')
    search = request.GET.get('search')


    if category_id:
        product_obj = Product.objects.filter(product_category_id=category_id)

    elif search:
        product_obj = Product.objects.filter(product_name__icontains=search)

    else:
        product_obj = Product.objects.all()


    category_obj = Category.objects.all()
    

    context = {
        'category': category_obj,
        'product': product_obj,
    }
    return render(request, 'home.html',context=context)

def contact(request):
    return render(request, 'contact.html')

def registration(request):
    if request.method == 'POST':
        f_name=request.POST.get('fname')
        l_name=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('pwd')
        mobile=request.POST.get('mbl')
        gender=request.POST.get('gender')

        data=Registration(
            first_name=f_name,
            last_name=l_name,
            email=email,
            password=make_password(password),
            mobile=mobile,
            gender=gender,
        )
        data.save()
    
    return redirect("home")

def login(request):
    if request.method == 'POST':
        email_id=request.POST.get('email')
        password=request.POST.get('pwd')
       
        try:
            email_obj=Registration.objects.get(email=email_id)
            if check_password(password,email_obj.password):
                request.session['name']=email_obj.first_name
                request.session['customer']=email_obj.id
                return redirect("home")
            
            else:
                return HttpResponse('Wrong password')
        except:
            return HttpResponse('Wrong email id')

def logout(request):
    request.session.clear()
    return redirect("home")

def cart_details(request):
    keys=list(request.session.get('cart').keys())
    product_in_cart=Product.objects.filter(id__in=keys)
    context={
        'product_in_cart':product_in_cart
    }
    return render(request, 'cart.html',context=context)

def checkout_details(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')

        customer_id = request.session.get('customer')

        if not customer_id:
            return HttpResponse('please login')
        cart_id = request.session.get('cart')

        product = Product.objects.filter(id__in=list(cart_id.keys()))

        for p in product:
            order_obj = Order(
                
                address=address,
                mobile=mobile,
                product = p,
                customer = Registration(id= customer_id),
                price = p.product_price,
                quantity = cart_id.get(str(p.id)),
            
                
            )
            order_obj.save()
            
    return redirect('order')

def order_detail(request):
    customer_id = request.session.get('customer')

    fetch_orders = Order.objects.filter(customer=customer_id)
    tp=0 
    for i in fetch_orders:
        tp=tp+(i.price*i.quantity)
    context = {
        'fetch_orders': fetch_orders,
        'tp':tp
    }
    return render(request, 'order.html',context=context)

from rest_framework import  viewsets
from .serializers import *
class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
