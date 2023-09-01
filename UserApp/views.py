from django.shortcuts import render,redirect
from AdminApp.models import Category,Product,UserInfo,PaymentMaster,Contact
from UserApp.models import MyCart,OrderMaster
from datetime import datetime
from django.contrib import messages
import bcrypt
from AdminApp.models import Category, UserInfo
from django.contrib.auth import authenticate, login
from django.http import HttpResponse




# Create your views here.


def homepage(request):
    cats = Category.objects.all()
    return render(request,"homepage.html",{"cats":cats})    


def login(request):
    cats = Category.objects.all() 
    
    if request.method == "GET":
        return render(request, "login.html", {"cats": cats})
    else:
        uname = request.POST["uname"]
        password = request.POST["password"]
        try:
            user = UserInfo.objects.get(uname=uname)
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                # Password matches, create the session
                request.session["uname"] = uname
                return redirect('homepage')
            else:
                # Password doesn't match
                return redirect('login')
        except UserInfo.DoesNotExist:
            return redirect('login')

    



def signup(request):
    cats = Category.objects.all()
    
    if request.method == "GET":
        return render(request, "signup.html", {"cats": cats})
    else:
        uname = request.POST["uname"]
        password = request.POST["password"]
        email = request.POST["email"]
        
        # Hash the password using bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        user = UserInfo(uname=uname, password=hashed_password, email=email)  # Use the hashed password
        user.save()
        return redirect('homepage')


def signout(request):
    request.session.clear()
    return redirect(homepage)


def menu(request):
    cats = Category.objects.all()
    pizzas = Product.objects.all()
    return render(request,"menu.html",{"pizzas":pizzas,"cats":cats})  


def ShowPizzas(request,id):    
    #get method returns single object
    id = Category.objects.get(id=id) 
    #filter method returns multiple objects   
    pizzas = Product.objects.filter(cat = id)
    cats = Category.objects.all()    
    return render(request,"menu.html",{"cats":cats,"pizzas":pizzas})


def contact(request):
    cats = Category.objects.all()
    return render(request,"contact.html",{"cats":cats})  
    

def about(request):
    cats = Category.objects.all()
    return render(request,"about.html",{"cats":cats})  
    
def services(request):
    cats = Category.objects.all()
    return render(request,"services.html",{"cats":cats})  

def ViewDetails(request,id):
    cats = Category.objects.all()
    pizza = Product.objects.get(id=id)
    return render(request,"ViewDetails.html",{"pizza":pizza,"cats":cats})

def addToCart(request):
    if request.method == "POST":
        if "uname" in request.session:
            # Add to cart
            pizzaid = request.POST["pizzaid"]
            user = request.session["uname"]
            qty = request.POST["qty"]
            pizza = Product.objects.get(id=pizzaid)
            user = UserInfo.objects.get(uname=user)
           
            cart = MyCart(user=user, pizza=pizza, qty=qty)
            cart.save()
          
            return redirect(ShowAllCartItems)
        else:
            return redirect(login)


def contact(request):
    cats = Category.objects.all()
    if(request.method == "GET"):
        return render(request,"contact.html",{"cats":cats})
    else:
        uname = request.POST["uname"]
        email =request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        user = Contact(uname,email,subject,message)
        user.save()
        return redirect(homepage)

            
def ShowAllCartItems(request):
    cats = Category.objects.all()
    uname = request.session["uname"]
    user = UserInfo.objects.get(uname = uname)
    if(request.method == "GET"):       
        cartitems = MyCart.objects.filter(user=user)
        total = 0
        for item in cartitems:
            total+= item.qty*item.pizza.price
        request.session["total"] = total
        return render(request,"ShowAllCartItems.html",{"items":cartitems,"cats":cats})
    else:
        id = request.POST["pizzaid"]
        pizza = Product.objects.get(id=id)
        item = MyCart.objects.get(user=user,pizza=pizza)            
        qty = request.POST["qty"]
        item.qty = qty
        item.save() #Update
        return redirect(ShowAllCartItems)


def removeItem(request):
    uname = request.session["uname"]
    user = UserInfo.objects.get(uname = uname)
    id = request.POST["pizzaid"]
    pizza = Product.objects.get(id=id)
    item = MyCart.objects.get(user=user,pizza=pizza)   
    item.delete()
    return redirect(ShowAllCartItems)


def MakePayment(request):
    if(request.method == "GET"):
        return render(request,"MakePayment.html",{})
    else:
        cardno = request.POST["cardno"]
        cvv = request.POST["cvv"]
        expiry = request.POST["expiry"]
        try:
            buyer = PaymentMaster.objects.get(cardno=cardno,cvv=cvv,expiry=expiry)
        except:
            return redirect(MakePayment)
        else:
            #Its a match
            owner = PaymentMaster.objects.get(cardno='111',cvv='111',expiry='12/2025')
            owner.balance += request.session["total"]
            buyer.balance -=request.session["total"]
            owner.save()
            buyer.save()
            #Delete all items from cart
            uname = request.session["uname"]
            user = UserInfo.objects.get(uname = uname)
            
            order = OrderMaster()
            order.user = user
            order.amount = request.session["total"]
            #order.dateOfOrder = datetime.now
            #Fetch all cart items for that user
            details = ""
            items = MyCart.objects.filter(user=user)
            for item in items:
                details += (item.pizza.pname)+","
                item.delete()            
            order.details = details
            order.save()
            return redirect(paymentsucces)
        


def paymentsucces(request):
    cats = Category.objects.all()
    return render(request,"paymentsucces.html",{"cats":cats})

def paymenthistory(request):
    # Assuming you have a way to identify the user whose payment history you want to display
    if "uname" in request.session:
        uname = request.session["uname"]
        user = UserInfo.objects.get(uname=uname)

        # Fetch payment history for the specific user
        payment_history = OrderMaster.objects.filter(user=user)

        # You can include other context data as needed
        cats = Category.objects.all()

        return render(request, "paymenthistory.html", {"payment_history": payment_history, "cats": cats})
    else:
        # Handle the case where the user is not authenticated or no session data is available
        # For example, redirect to a login page or show an error message
        return HttpResponse("User not authenticated.")


