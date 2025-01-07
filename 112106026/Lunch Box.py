from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

lunch=[]
price=[]
with open("lunch.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line == '': break
        line=line[2:].strip()
        a,b=line.split(':')
        lunch.append(a)
        price.append(int(b))

@app.route('/list')
def list():
    html='<table border><br><tr><th></th><th>Item</th><th>price</th></tr>'
    for i in range(len(lunch)):
        html+='<tr><td>'+str(i+1)+'</td><td>'+lunch[i]+'</td><td>'+str(price[i])+'</td></tr>'
    html+='</table>'

    return html

@app.route('/order')
def order():
    html='''
    <form action="/accept" method="get">
    <input type=text name=name>
    <select name="mealId">
            <option value=0>Item:price</option>
            <option value=1>排骨飯($110)</option>
            <option value=2>鯖魚飯($105)</option>
            <option value=3>雞腿飯($115)</option>
    </select>
    <input type=submit value='Submit'>
    </form>
    '''
    return html

@app.route('/accept')
def accept():
    mealId=int(request.values['mealId'])
    html=f"{request.values['name']} orders "
    html+=f"{lunch[mealId-1]}(${price[mealId-1]})"
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('order.txt', 'a', encoding='utf-8') as file:
        file.write(f"{time} {request.values['name']} {mealId}\n")
    return html
    

@app.route('/total')
def total():
    time=[]
    name=[]
    meal=[]
    price_total=0
    with open("order.txt", "r", encoding="utf-8") as file:
        for line in file:
            if line == '': break
            line=line.strip()
            time.append(line[:19])
            meal.append(int(line[-1]))
            name.append(line[20:-2])
            price_total+=price[meal[-1]-1]
    html='<table border><br> <tr> <th>Time</th> <th>Name</th> <th>Meal</th> </tr>'
    for i in range(len(lunch)):
        html+=f"<tr><td>{time[i]}</td><td>{name[i]}</td><td>{lunch[int(meal[i])-1]}(${price[int(meal[i])-1]})</td></tr>"
    html+=f'<tr><td></td><td>Total</td><td>${price_total}</td></tr></table>'
    return html
