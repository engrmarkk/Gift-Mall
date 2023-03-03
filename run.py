from market import app


if __name__=='__main__':
    app. run(debug=True)
    
    
    
    #use the following steps to add items to your item list
    # from market import app
    # from market.models import db, Item
    # i1 = Item(name='Iphone 11', price='900', barcode='776767677676', description='This is an Iphone 11 promax')  
    # with app.app_context():
    #db.session.add(i1) 
    #db.session.commit()