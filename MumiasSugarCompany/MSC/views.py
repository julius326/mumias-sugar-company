from django.shortcuts import render
from .models import Contact

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def products(request):
    return render(request, 'products.html')
from .models import Order

def order(request):

    if request.method == "POST":

        quantity = int(request.POST.get("quantity"))
        price = float(request.POST.get("price"))
        total = quantity * price

        Order.objects.create(
            customer_name=request.POST.get("customer_name"),
            contact=request.POST.get("contact"),
            product=request.POST.get("product"),
            quantity=quantity,
            price=price,
            notes=request.POST.get("notes"),
            total=total,
        )

        return render(request, "order.html", {
            "success": "Your order has been submitted successfully!"
        })

    return render(request, "order.html")
def contact(request):

    if request.method == "POST":
        Contact.objects.create(
            full_name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone_number=request.POST.get("phone"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )

        return render(request, "contact.html", {
            "success": "Your message has been sent successfully!"
        })

    return render(request, "contact.html")