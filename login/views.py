from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json
#from ..app1 import views as adminViews
# Create your views here.
import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database='onlinefooddeliverysystem')
print('Successfully connected to database from LOGIN')
cur = conn.cursor()


#login Page Views START HERE
def loginPage(request):
    """ print("LOGIN PAGE HAS BEEN RENDERED STATICALLY")

    submitbutton= request.POST.get('loginBtn')
    if submitbutton: 
        print("THE SUBMIIIIIIIIIIIIT BUUUTTTTOOOOON WASSS CLICKEEEEDDD")
        login(request)
    else:
        print("SUBMIT NOT CLICKEDDD") """
    return render(request, 'login/login.html')

def signupPage(request):
    return render(request, 'login/signup.html')

@csrf_exempt
def login(request):
    
    print("ENTERRRINNGGG LOGIN RENDER FUNCTION")
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode) 
        print("REQUEEESSSTTT METHODDDD IS POSTTTTT")
        print(request.POST)
        admin_email = body['email']
        admin_pass = body['password']
        
        cur.execute("SELECT `u_id`, `u_email`, `u_password`, `type_id` FROM `tbl_user` WHERE `u_email` = '{}' AND `u_password` = '{}'".format(admin_email,admin_pass))
        data = cur.fetchone()

        
        print("ENTERED EMAIL IS : ", admin_email)
        print("ENTERED PASSWORD IS : ", admin_pass)

        print("Fetched data from SQL QUERY: ", data)
        
        if data is not None:
            print("DATA IS NOT NONEEEE")

            if len(data) > 0:
                #Fetch Data
                if data[3] == 1:
                    print("data[3] is admin")
                    return JsonResponse({'redirect_to': '/foodAdmin'})
                    
                    return redirect(adminHome)
                elif data[3] == 2:
                    print("data[3] is restaurant")
                    return JsonResponse({'redirect_to': '/restaurant'})
                    return redirect(restaurantHome)
                elif data[3] == 3:
                    print("data[3] is user")
                    return JsonResponse({'redirect_to': '/user'})
                    return redirect(indexFunc)
                    return render(request, 'users/index.html')

                admin_db_id = data[0]
                admin_db_email = data[1]
                print(admin_db_id)
                print(admin_db_email)
                #Session Create Code
                #request.session['admin_id'] = admin_db_id
                #request.session['admin_email'] = admin_db_email
                #Session Create Code
                #Cookie Code
                #response = redirect('/home')
                #response.set_cookie('admin_id', admin_db_id)
                #response.set_cookie('admin_email', admin_db_email)
                #return response

                
                #Cookie Code
            else:
                messages.error(request,"Invalid Login!")
                return render(request, 'login/signup.html')         
        #messages.error(request,"Invalid Login!")
        #return render(request, 'login/signup.html')
        
       # return redirect(dashboard) 
    else:
        return render(request, 'login/signup.html') 

def indexFunc(request):
    print("INSIDE THE INDEX RENDERING FUNCTION")
    return render(request, 'users/index.html')
    
    if 'admin_email' in request.COOKIES and request.session.has_key('admin_email'):
        
        admin_emails = request.session['admin_email']
        #admin_emailc = request.COOKIES['admin_email']

        print("Session is  " + str(admin_emails))
        #print("Cookie is  " + admin_emailc)

        return render(request, 'users/index.html')
    else:
        return redirect('users/index.html')
    
def adminHome(request):
    print("INSIDE ADMIN HOME PAGE RENDER FROM LOGIN APP")
    return render(request, 'admin/user.html')

def restaurantHome(request):
    print("INSIDE RESTAURANT HOME PAGE RENDER FROM LOGIN APP")
    cur.execute("SELECT * FROM `tbl_food_items`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))

    cur.execute("SELECT COUNT(f_id) FROM `tbl_food_items`")
    total = cur.fetchone()

    cur.execute("SELECT COUNT(`f_id`) FROM `tbl_food_items` WHERE `f_category_id` = 101")
    punjabi = cur.fetchone()

    cur.execute("SELECT COUNT(`f_id`) FROM `tbl_food_items` WHERE `f_category_id` = 102")
    chinese = cur.fetchone()

    cur.execute("SELECT COUNT(`f_id`) FROM `tbl_food_items` WHERE `f_category_id` = 104")
    south = cur.fetchone()

    return render(request, 'restaurants/food.html', {'food': data, 'NorthIndian': punjabi[0], 'chineseFood': chinese[0], 'totalItem': total[0], 'southIndian': south[0]})
#login Page Views END HERE

