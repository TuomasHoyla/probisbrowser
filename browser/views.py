from django.shortcuts import render
from browser.models import UserProfile
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def palautadata(request):
    if request.method == 'GET':
        cat_id = request.GET['category_id']
    if cat_id:
        cat = UserProfile.objects.get(id=int(cat_id))
        context_dict = {'etunimi': cat.firstname,
                        'sukunimi': cat.lastname,
                        'osoite': cat.address,
                       }
    return render(request, 'browser/personDiv.html', context_dict)

def index(request):
        
    try:
        #Get request "page"
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    #Debuggausta varten
    print(request)
    #Hae kannasta kaikki objektit
    UserProfile_list = UserProfile.objects.all()

    #pilko tavara paginatorilla
    p = Paginator(UserProfile_list, request=request, per_page=4)

    #maarita palautettava page
    people = p.page(page)

    #palautettava data
    context_dict = {'UserProfiles': UserProfile_list, 'people': people}
    # Render the response and send it back
    return render(request, 'browser/index.html', context_dict)


def user_login(request):
    
    if request.method == 'POST':
        print(request.POST.get('password'))
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        #omaa saatoo
        if User.objects.filter(username=username).exists():
            print("User found")
        else:
            print("no user")
            return render(request, 'browser/login.html', {'error': "User not found"})
        
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                login(request,user)
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                return HttpResponseRedirect('/browser/')
            else:
                return("Your account has been disabled")
        else:
            print("loggaus ei toimi: {0}, {1}".format(username, password))
            #return("invalidit credentiaalit tarjottu")
            return render(request, 'browser/login.html', {'error': "No matching username / password found!"})
    else:
    # No context variables to pass to the template system, hence the
    # blank dictionary object...
        return render(request, 'browser/login.html', {})
    
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/browser/')