from flask import render_template, render_template_string, request
from app import app
from app.processing import find_stores, find_home, get_data, make_site
from datetime import date

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("/public/index.html")

@app.route("/locate", methods=['GET', 'POST'])
def locate():
    today = date.today()
    now = today.strftime("%b-%d-%Y")
    store = request.form['store'].upper()
    c_list = request.form.getlist('company')
    d_list = request.form.getlist('distance')
    cAL = cJM = cJN = cr5 = cr10 = cr25 = cr50 = None
    if  'AL' in c_list:
        cAL = "checked"
    elif  'JM' in c_list:
        cJM = "checked"
    elif  'JN' in c_list:
        cJN = "checked"
    else:
        cAL = "checked"
    if 'm5' in d_list:
        cr5 = "checked"
        miles = "5 miles"
        zoom = 13
    elif 'm10' in d_list:
        cr10 = "checked"
        miles = "10 miles"
        zoom = 12
    elif 'm25' in d_list:
        cr25 = "checked"
        miles = "25 miles"
        zoom = 11
    elif 'm50' in d_list:
        cr50 = "checked"
        miles = "50 miles"
        zoom = 10
    else:
        cr25 = "checked"
        miles = "25 miles"
        zoom = 11
    stores = find_stores(store, c_list, d_list)
    if stores != None:
        home = find_home(store)
        count = len(stores)
        website = make_site(count)
        d = get_data(stores)
        return render_template_string(website, home=home, now=now, miles=miles, d=d, count=count, zoom=zoom, cAL=cAL, cJM=cJM, cJN=cJN, cr5=cr5, cr10=cr10, cr25=cr25, cr50=cr50)
    else:
        return render_template("/public/error.html", cAL=cAL, cJM=cJM, cJN=cJN, cr5=cr5, cr10=cr10, cr25=cr25, cr50=cr50)