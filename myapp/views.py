from django.shortcuts import render,redirect 
from .models import User,Product 
import random 

# Create your views here.
def index(request):
    return render(request,'index.html')

def seller_index(request):
    return render(request,'seller-index.html') 

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def product(request):
    products = Product.objects.all()    
    return render(request,'product.html',{'products':products})

def signup(request):
    if request.method == 'POST':
        try:
            User.objects.get(email = request.POST['email'])
            msg = 'You are already registered please login directly!!'
            return render(request,'signup.html',{'msg':msg})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                User.objects.create(
                    fname = request.POST['fname'],
                    lname = request.POST['lname'],
                    email = request.POST['email'],
                    mobile = request.POST['mobile'],
                    address = request.POST['address'],
                    password = request.POST['password'],
                    profile_picture = request.FILES['profile_picture'],
                    usertype = request.POST['usertype']
                    )
                msg = 'User signup successfully'
                return render(request,'signup.html',{'msg':msg})
            else:
                msg = 'Password & Confirm password does not matched!!'
                return render(request,'signup.html',{'msg':msg})
    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email = request.POST['email'])
            if user.password == request.POST['password']:
                request.session['email'] = user.email
                request.session['fname'] = user.fname
                request.session['profile_picture'] = user.profile_picture.url 
                print('You came here all session is made')
                if user.usertype == 'buyer':   
                    return render(request,'index.html')
                else:
                    print('You come in else part also now just you have to render seller-index.html')
                    return render(request,'seller-index.html')
            else:
                msg = 'Incorrect Password'
                return render(request,'login.html',{'msg':msg})
        except:
            msg = 'Email is not registered'
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')

def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        del request.session['profile_picture']
        return render(request,'login.html')
    except:
        return render(request,'login.html')


def profile(request):
    user = User.objects.get(email = request.session['email'])
    if request.method == 'POST':
        user.fname = request.POST['fname']
        user.lname = request.POST['lname']
        user.email = request.POST['email']
        user.mobile = request.POST['mobile']
        user.address = request.POST['address']
        try:
            user.profile_picture = request.FILES['profile_picture']
        except:
            pass
        user.save()
        request.session['profile_picture'] = user.profile_picture.url 
        msg = f'{user.fname} {user.lname} successfully updated profile'
        if user.usertype == 'buyer':
            return render(request,'profile.html',{'user':user,'msg':msg})
        else:
            return render(request,'seller-profile.html',{'user':user,'msg':msg}) 
    else:
        if user.usertype == 'buyer':
            return render(request,'profile.html',{'user':user})
        else:
            return render(request,'seller-profile.html',{'user':user})
    

def change_password(request):
    user = User.objects.get(email = request.session['email'])
    if request.method == 'POST':
        if user.password == request.POST['oldpassword']:
            if request.POST['newpassword'] == request.POST['cnewpassword']:
                if user.password != request.POST['newpassword']:
                    user.password = request.POST['newpassword']
                    user.save()
                    del request.session['email']
                    del request.session['fname']
                    del request.session['profile_picture']

                    msg = 'Password Changed Successfully!!'
                    return render(request,'login.html',{'msg':msg})
                else:
                    msg = 'Old password and new password can not be same!!'
                    if user.usertype == 'buyer':
                        return render(request,'change-password.html',{'msg':msg})
                    else:
                        return render(request,'seller-change-password.html',{'msg':msg})
            else:
                msg = "New password and confirm new password doesn't matched"
                if user.usertype == 'buyer':
                    return render(request,'change-password.html',{'msg':msg})
                else:
                    return render(request,'seller-change-password.html',{'msg':msg})
                
        else:
            msg = "your password is incorrect"
            if user.usertype == 'buyer':
                return render(request,'change-password.html',{'msg':msg})
            else:
                return render(request,'seller-change-password.html',{'msg':msg})

        
    else:
        if user.usertype == 'buyer':
            return render(request,'change-password.html')
        else:
            return render(request,'seller-change-password.html')
    
def forgot_password(request):
    if request.method == 'POST':
        try:
            User.objects.get(mobile = request.POST['mobile'])
            
            otp = str(random.randint(1000,9999))
            print(otp)
            request.session['otp'] = otp 
            request.session['mobile'] = request.POST['mobile'] 
            return render(request,'otp.html')
            
        except:
            msg = "Mobile Number is not registered!"
            return render(request,'forgot-password.html',{'msg':msg})
    
    
    else:
        return render(request,'forgot-password.html')

def verify_otp(request):
        if int(request.session['otp']) == int(request.POST['otp']):
            del request.session['otp']
            msg = 'Enter Your New Password'
            return render(request,'new-password.html',{'msg':msg})
        else:
            msg = "Invalid OTP"
            return render(request,'otp.html',{'msg':msg})

def new_password(request):
    if str(request.POST['newpassword']) == str(request.POST['cnewpassword']):
        user = User.objects.get(mobile = request.session['mobile'])
        user.password = request.POST['newpassword']    
        user.save()
        del request.session['mobile']
        msg = 'Password Updated Successfully!'
        return render(request,'login.html',{'msg':msg})
    else:
        msg = 'New Password and Confirm new password does not Matched'
        return render(request,'new-password.html',{'msg':msg})


def seller_add_product(request):
    if request.method == 'POST':
        seller = User.objects.get(email = request.session['email'])
        Product.objects.create(
            seller = seller,
            product_category = request.POST['product_category'],
            product_size = request.POST['product_size'],
            product_name = request.POST['product_name'],
            product_desc = request.POST['product_desc'],
           product_price = request.POST['product_price'],
            product_picture = request.FILES['product_picture'],
        )
        msg = 'Product Added Successfully'
        return render(request,'seller-add-product.html',{'msg':msg})
    else:
        return render(request,'seller-add-product.html')

def seller_view_product(request):
    seller = User.objects.get(email = request.session['email'])
    products = Product.objects.filter(seller = seller)
    return render(request,'seller-view-product.html',{'products':products})

def seller_product_details(request,pk):
    product = Product.objects.get(pk = pk)
    return render(request,'seller-product-details.html',{'product':product})

def product_details(request,pk):
    product = Product.objects.get(pk = pk)
    return render(request,'product-details.html',{'product':product})

def seller_edit_product(request,pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.product_category = request.POST['product_category']
        product.product_name = request.POST['product_name']
        product.product_price = request.POST['product_price']
        product.product_desc = request.POST['product_desc']
        product.product_size = request.POST['product_size']
        try:
            product.product_picture = request.FILES['product_picture']
        except:
            pass 
        product.save()
        #return render(request,'seller-view-product.html') here we need to take product along with for go in seller-view-product page 
        # for not doing that we can use redirect
        return redirect('seller-view-product') 
            
    else:    
        product = Product.objects.get(pk=pk)
        return render(request,'seller-edit-product.html',{'product':product})
    

def seller_delete_product(request,pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('seller-view-product') 