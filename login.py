from flask import Flask, render_template, request, url_for, redirect
from array import array
app = Flask(__name__)
import os

from werkzeug.utils import secure_filename
UPLOAD_FOLDER = './static/upload'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="exchange"
)
mycursor = mydb.cursor()

@app.route('/')
def home():
	return render_template('home.html')
	
@app.route('/welcome' ,methods=['GET','POST'])
def welcome():
	if (request.method == 'POST'):
		Group = str(request.form.get('group'))
		Username = str(request.form.get('username'))
		Email = str(request.form.get('email'))
		Password = str(request.form.get('password'))
		Confirm_password = str(request.form.get('confirm_password'))
		Fname = str(request.form.get('fname'))
		Lname = str(request.form.get('lname'))
		Phone = str(request.form.get('phone'))
		Gender = str(request.form.get('gender'))
		if (Password == Confirm_password):
			sql = "INSERT INTO adduser (grouping,Username,Email,Password,FirstName,LastName,Phone,Gender) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
			val = (Group,Username,Email,Password,Fname,Lname,Phone,Gender)
			result = mycursor.execute(sql,val)
			mydb.commit()
		else:
			print('Password and Confirm Password')
		return redirect(url_for('view'))
	else:
		return render_template('welcome.html')
		
@app.route('/view')
def view():
	new = []
	print(new)
	mycursor.execute("SELECT * FROM adduser")
	row=mycursor.fetchall()
	for i in row:
		id = i[0]
		Group = i[1]
		Username = i[2]
		Email = i[3]
		Password = i[4]
		Firstname = i[5]	
		Lastname = i[6]
		Phone = i[7]
		Gender = i[8]
		data = {'id':id,'Group':Group,'Username':Username,'Email':Email,'Password':Password,'Firstname':Firstname,'Lastname':Lastname,'Phone':Phone,'Gender':Gender}
		new.append(data)
		
	return render_template('view.html', result = new) 
	
@app.route('/edit/<string:id>')
def edit(id):
	row = []
	print('kljjofjjfvij')
	print('kdnkckln')
	mycursor.execute("SELECT * FROM adduser WHERE id= %s",[id])
	print('kjhcuihi')
	new = mycursor.fetchall()
	print(new)
	for j in new:
		id = j[0]
		Group = j[1]
		Username = j[2]
		Email = j[3]
		Password = j[4]
		Firstname = j[5]	
		Lastname = j[6]
		Phone = j[7]
		Gender = j[8]
		print(id)
		print(Group)
		print(Username)
		data = {'Grouping':Group,'Username':Username,'Email':Email,'Password':Password,'Firstname':Firstname,'Lastname':Lastname,'Phone':Phone,'Gender':Gender,'id':id,}
		row.append(data)
	return render_template('edit.html', row = row)

	
@app.route('/update',methods=['POST'])
def update():
	if (request.method == 'POST'):
		Group = str(request.form.get('group'))
		Username = str(request.form.get('username'))
		Email = str(request.form.get('email'))
		Password = str(request.form.get('password'))
		Fname = str(request.form.get('fname'))
		Lname = str(request.form.get('lname'))
		Phone = str(request.form.get('phone'))
		Gender = str(request.form.get('gender'))
		id = str(request.form.get('id'))
		
		mycursor.execute("UPDATE adduser SET grouping = '"+str(Group)+"',Username = '"+str(Username)+"',Email = '"+str(Email)+"',Password = '"+str(Password)+"',FirstName = '"+str(Fname)+"',LastName = '"+str(Lname)+"',Phone = '"+str(Phone)+"',Gender = '"+str(Gender)+"' WHERE id = '"+str(id)+"'")
		mydb.commit()
		return redirect(url_for('home'))
	
 
@app.route('/delete/<string:id>' ,methods =['POST'])
def delete(id):
	mycursor.execute("DELETE FROM adduser WHERE id=%s",[id])
	mydb.commit()
	print('Deleted Successfully')
	return redirect(url_for('view'))
	
#---------------category-------------------#
@app.route('/category_add',methods=['GET','POST'])
def category_add():
	if (request.method == 'POST'):
		Category_name = str(request.form.get('category_name'))
		Status = str(request.form.get('status'))
		sql = "INSERT INTO addcategory (CategoryName,Status) VALUES (%s,%s)"
		val = (Category_name,Status)
		result = mycursor.execute(sql,val)
		mydb.commit()
		return  redirect(url_for('category_view'))
	else:
		return render_template('category_add.html')
		
		
@app.route('/category_view')		
def category_view():
	all = []
	mycursor.execute("SELECT * FROM addcategory")
	rowcursor=mycursor.fetchall()
	for i in rowcursor:
		id = i[0]
		CategoryName = i[1]
		Status = i[2]
		data = {'id':id,'CategoryName':CategoryName,'Status':Status}
		all.append(data)
	return render_template('category_view.html', results = all) 
	
@app.route('/category_edit/<string:id>')
def category_edit(id):
	row = []
	mycursor.execute("SELECT * FROM addcategory WHERE id= %s",[id])
	new = mycursor.fetchall()
	print('dfghjk')
	print(new)
	for j in new:
		id = j[0]
		CategoryName = j[1]
		Status = j[2]
		data = {'CategoryName':CategoryName,'Status':Status,'id':id,}
		row.append(data)
	return render_template('category_edit.html', row = row)

@app.route('/category_update',methods=['POST'])
def category_update():
	if (request.method == 'POST'):
		CategoryName = str(request.form.get('category_name'))
		Status = str(request.form.get('status'))
		id = str(request.form.get('id'))
		mycursor.execute("UPDATE adduser SET grouping = '"+str(CategoryName)+"',Email = '"+str(Status)+"' WHERE id = '"+str(id)+"'")
		mydb.commit()
		return redirect(url_for('home'))
	

	
@app.route('/category_delete/<string:id>' ,methods =['POST'])
def category_delete(id):
	mycursor.execute("DELETE FROM addcategory WHERE id=%s",[id])
	mydb.commit()
	print('Deleted Successfully')
	return redirect(url_for('home'))
	

#------BRAND---------------#
@app.route('/brand_add',methods=['GET','POST'])
def brand_add():
	if (request.method == 'POST'):
		Brand_name = str(request.form.get('brand_name'))
		Status = str(request.form.get('status'))
		sql = "INSERT INTO addbrand (BrandName,Status) VALUES (%s,%s)"
		val = (Brand_name,Status)
		result = mycursor.execute(sql,val)
		mydb.commit()
		return  redirect(url_for('brand_view'))
	else:
		return render_template('brand_add.html')
		
		
@app.route('/brand_view')		
def brand_view():
	all = []
	mycursor.execute("SELECT * FROM addbrand")
	rowcursor=mycursor.fetchall()
	for i in rowcursor:
		id = i[0]
		BrandName = i[1]
		Status = i[2]
		data = {'id':id,'BrandName':BrandName,'Status':Status}
		all.append(data)
	return render_template('brand_view.html', results = all) 
	
@app.route('/brand_edit/<string:id>')
def brand_edit(id):
	row = []
	mycursor.execute("SELECT * FROM addbrand WHERE id= %s",[id])
	new = mycursor.fetchall()
	for j in new:
		id = j[0]
		BrandName = j[1]
		Status = j[2]
		data = {'BrandName':BrandName,'Status':Status,'id':id,}
		row.append(data)
	return render_template('Brand_edit.html', row = row)

@app.route('/brand_update',methods=['POST'])
def brand_update():
	if (request.method == 'POST'):
		BrandName = str(request.form.get('brand_name'))
		Status = str(request.form.get('status'))
		id = str(request.form.get('id'))
		mycursor.execute("UPDATE addbrand SET BrandName = '"+str(BrandName)+"',Status = '"+str(Status)+"' WHERE id = '"+str(id)+"'")
		mydb.commit()
		return redirect(url_for('home'))
	

	
@app.route('/brand_delete/<string:id>' ,methods =['POST'])
def brand_delete(id):
	mycursor.execute("DELETE FROM addbrand WHERE id=%s",[id])
	mydb.commit()
	print('Deleted Successfully')
	return redirect(url_for('home'))
#-------------------------Company---------------------------#
@app.route('/company_add',methods=['GET','POST'])
def company_add():
	if (request.method == 'POST'):
		Company_name = str(request.form.get('company_name'))
		Charge_amount = str(request.form.get('charge_amount'))
		Vat_charge = str(request.form.get('vat_charge'))
		Address = str(request.form.get('address'))
		Phone = str(request.form.get('phone'))
		Country = str(request.form.get('country'))
		Message = str(request.form.get('message'))
		Currency = str(request.form.get('currency'))
		
		sql = "INSERT INTO addcompany (CompanyName,ChargeAmount,VatCharge,Address,phone,Country,Message,Currency) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
		val = (Company_name,Charge_amount,Vat_charge,Address,Phone,Country,Message,Currency)
		result = mycursor.execute(sql,val)
		mydb.commit()
		return redirect(url_for('company_view'))
	else:
		return render_template('company_add.html')
		
		
@app.route('/company_view')		
def company_view():
	all = []
	mycursor.execute("SELECT * FROM addcompany")
	rowcursor=mycursor.fetchall()
	for i in rowcursor:
		id = i[0]
		CompanyName = i[1]
		ChargeAmount = i[2]
		VatCharge = i[3]
		Address = i[4]
		phone = i[5]
		Country = i[6]
		Message = i[7]
		Currency = i[8]
		data = {'id':id,'CompanyName':CompanyName,'ChargeAmount':ChargeAmount,'VatCharge':VatCharge,'Address':Address,'phone':phone,'Message':Message,'Country':Country,'Message':Message,'Currency':Currency}
		all.append(data)
	return render_template('company_view.html', results = all) 
	
@app.route('/company_edit/<string:id>')
def company_edit(id):
	row = []
	mycursor.execute("SELECT * FROM addcompany WHERE id= %s",[id])
	new = mycursor.fetchall()
	for i in new:
		id = i[0]
		CompanyName = i[1]
		ChargeAmount = i[2]
		VatCharge = i[3]
		Address = i[4]
		phone = i[5]
		Country = i[6]
		Message = i[7]
		Currency = i[8]
		data = {'id':id,'CompanyName':CompanyName,'ChargeAmount':ChargeAmount,'VatCharge':VatCharge,'Address':Address,'phone':phone,'Country':Country,'Message':Message,'Currency':Currency}
		row.append(data)
	return render_template('company_edit.html', row = row)

@app.route('/company_update',methods=['POST'])
def company_update():
	if (request.method == 'POST'):
		Company_name = str(request.form.get('Company_name'))
		Charge_amount = str(request.form.get('charge_amount'))
		Vat_charge = str(request.form.get('vat_charge'))
		Address = str(request.form.get('address'))
		Phone = str(request.form.get('phone'))
		Country = str(request.form.get('country'))
		Message = str(request.form.get('message'))
		Currency = str(request.form.get('currency'))
		mycursor.execute("UPDATE addcompany SET CompanyName= '"+str(Company_name)+"',ChargeAmount = '"+str(Charge_amount)+"',VatCharge ='"+str(Vat_charge)+"',Address = '"+str(Address)+"',phone = '"+str(Phone)+"',Country = '"+str(Country)+"',Message = '"+str(Message)+"',Currency = '"+str(Currency)+"' WHERE id = '"+str(id)+"'")
		mydb.commit()
		return redirect(url_for('home'))
	

	
@app.route('/company_delete/<string:id>' ,methods =['POST'])
def company_delete(id):
	mycursor.execute("DELETE FROM addcompany WHERE id=%s",[id])
	mydb.commit()
	print('Deleted Successfully')
	return redirect(url_for('home'))
#---------------product-----------#
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/product_add',methods=['GET','POST'])
def product_add():
	if (request.method == 'POST'):
		file = request.files['inputfile']
		filename =" "
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		Product_name = str(request.form.get('product_name'))
		Sku = str(request.form.get('sku'))
		Price = str(request.form.get('price'))
		Qty = str(request.form.get('qty'))
		Description = str(request.form.get('description'))
		Brands = str(request.form.get('brands'))
		Category = str(request.form.get('category'))
		Store = str(request.form.get('store'))
		Availability = str(request.form.get('availability'))
		sql = "INSERT INTO addproduct (File,ProductName,Sku,Price,Qty,Description,Brands,Category,Store,Availability) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		val = (filename,Product_name,Sku,Price,Qty,Description,Brands,Category,Store,Availability)
		result = mycursor.execute(sql,val)
		mydb.commit()
		return redirect(url_for('product_view'))
	else:
		return render_template('product_add.html')
		
@app.route('/product_view',methods=['GET','POST'])
def product_view():
	all = []
	mycursor.execute("SELECT * FROM addproduct")
	rowcursor=mycursor.fetchall()
	for i in rowcursor:
		id = i[0]
		ProductName = i[1]
		file = i[2]
		Sku = i[3]
		Price = i[4]
		Qty = i[5]
		Description = i[6]
		Brands = i[7]
		Category = i[8]
		Store = i[9]
		Availability = i[10]
		data = {'id':id,'ProductName':ProductName,'file':file,'Sku':Sku,'Price':Price,'Qty':Qty,'Description':Description,'Brands':Brands,'Category':Category,'Store':Store,'Availability':Availability}
		all.append(data)
	return render_template('product_view.html', results = all) 

@app.route('/product_edit/<string:id>')
def product_edit(id):
	row = []
	mycursor.execute("SELECT * FROM addproduct WHERE id= %s",[id])
	new = mycursor.fetchall()
	for i in new:
		id = i[0]
		ProductName = i[1]
		file = i[2]
		Sku = i[3]
		Price = i[4]
		Qty = i[5]
		Description = i[6]
		Brands = i[7]
		Category = i[8]
		Store = i[9]
		Availability = i[10]
		data = {'id':id,'ProductName':ProductName,'file':file,'Sku':Sku,'Price':Price,'Qty':Qty,'Description':Description,'Brands':Brands,'Category':Category,'Store':Store,'Availability':Availability}
		row.append(data)
	return render_template('product_edit.html', row = row)
	
	
@app.route('/product_update',methods=['POST'])
def product_update():
	if (request.method == 'POST'):
		Product_name = str(request.form.get('product_name'))
		file = str(request.form.get('inputfile'))
		Sku = str(request.form.get('sku'))
		Price = str(request.form.get('price'))
		Qty = str(request.form.get('qty'))
		Description = str(request.form.get('description'))
		Brands = str(request.form.get('brands'))
		Category = str(request.form.get('category'))
		Store = str(request.form.get('store'))
		Availability = str(request.form.get('availability'))
		
		mycursor.execute("UPDATE addproduct SET ProductName= '"+str(Product_name)+"',file= '"+str(file)+"',Sku = '"+str(Sku)+"',Price ='"+str(Price)+"',Qty = '"+str(Qty)+"',Description = '"+str(Description)+"',Brands = '"+str(Brands)+"',Category = '"+str(Category)+"',Store = '"+str(Store)+"',Availability = '"+str(Availability)+"' WHERE id = '"+str(id)+"'")
		mydb.commit()
		return redirect(url_for('home'))
	
@app.route('/product_delete/<string:id>' ,methods =['POST'])
def product_delete(id):
	mycursor.execute("DELETE FROM addproduct WHERE id=%s",[id])
	mydb.commit()
	print('Deleted Successfully')
	return redirect(url_for('home'))
#-------------------order-------------#
@app.route('/order_add',methods=['GET','POST'])
def order_add():
	if (request.method == 'POST'):
		CustomerName = str(request.form.get('customer_name'))
		CustomerAddress = str(request.form.get('customer_address'))
		CustomerPhone = str(request.form.get('customer_phone'))
		Product = str(request.form.getlist('product[]'))
		Qty = str(request.form.getlist('qty[]'))
		Rate = str(request.form.getlist('rate[]'))
		Amount = str(request.form.getlist('amount[]'))
		GrossAmount = str(request.form.get('gross_amount'))
		SCharge = str(request.form.get('s_charge'))
		Vat = str(request.form.get('vat'))
		Discount = str(request.form.get('discount'))
		NetAmount = str(request.form.get('net_amount'))
		print(type(Product))
		
		s=list(Product.split(" "))
		print(s)
		print(type(s))
		l = len(s)
		print(l)
		for i in range(l):
			sql = "INSERT INTO addorder (CustomerName,CustomerAddress,CustomerPhone,Product,Qty,Rate,Amount,GrossAmount,SCharge,Vat,Discount,NetAmount) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val=(CustomerName,CustomerAddress,CustomerPhone,Product,Qty,Rate,Amount,GrossAmount,SCharge,Vat,Discount,NetAmount)
			result = mycursor.execute(sql,val)
			mydb.commit()
			
			
		return  redirect(url_for('order_view'))
	else:
		return render_template('order_add.html')
		
		
@app.route('/order_view',methods=['GET','POST'])
def order_view():
	all = []
	mycursor.execute("SELECT * FROM addorder")
	rowcursor=mycursor.fetchall()
	for i in rowcursor:
		id = i[0]
		CustomerName = i[1]
		CustomerAddress = i[2]
		CustomerPhone = i[3]
		Product = i[4]
		Qty = i[5]
		Rate = i[6]
		Amount = i[7]
		GrossAmount = i[8]
		SCharge = i[9]
		Vat = i[10]
		Discount = i[11]
		NetAmount = i[12]
		print(CustomerName)
		print(CustomerAddress)
		data = {'id':id,'CustomerName':CustomerName,'CustomerAddress':CustomerAddress,'CustomerPhone':CustomerPhone,'Product':Product,'Qty':Qty,'Rate':Rate,'Amount':Amount,'GrossAmount':GrossAmount,'SCharge':SCharge,'Vat':Vat,'Discount':Discount,'NetAmount':NetAmount}
		all.append(data)
	return render_template('order_view.html', results = all) 

@app.route('/order_edit/<string:id>')
def order_edit(id):
	row = []
	mycursor.execute("SELECT * FROM addorder WHERE id= %s",[id])
	new = mycursor.fetchall()
	for i in new:
		id = i[0]
		CustomerName = i[1]
		CustomerAddress = i[2]
		CustomerPhone = i[3]
		Product = i[4]
		Qty = i[5]
		Rate = i[6]
		Amount = i[7]
		GrossAmount = i[8]
		SCharge = i[9]
		Vat = i[10]
		Discount = i[11]
		NetAmount = i[12]
		data = {'id':id,'CustomerName':CustomerName,'CustomerAddress':CustomerAddress,'CustomerPhone':CustomerPhone,'Product':Product,'Qty':Qty,'Rate':Rate,'Amount':Amount,'GrossAmount':GrossAmount,'SCharge':SCharge,'Vat':Vat,'Discount':Discount,'NetAmount':NetAmount}
		row.append(data)
	return render_template('order_edit.html', row = row)
	
@app.route('/order_update',methods=['POST'])
def order_update():
	if (request.method == 'POST'):
		CustomerName = str(request.form.get('customer_name'))
		CustomerAddress = str(request.form.get('customer_address'))
		CustomerPhone = str(request.form.get('customer_phone'))
		Product = str(request.form.get('product'))
		Qty = str(request.form.get('qty'))
		Rate = str(request.form.get('rate'))
		Amount = str(request.form.get('amount'))
		GrossAmount = str(request.form.get('gross_amount'))
		SCharge = str(request.form.get('s_charge'))
		Vat = str(request.form.get('vat'))
		Discount = str(request.form.get('discount'))
		NetAmount = str(request.form.get('net_amount'))
		
		mycursor.execute("UPDATE addorder SET CustomerName = '"+str(CustomerName)+"',CustomerAddress = '"+str(CustomerAddress)+"',CustomerPhone ='"+str(CustomerPhone)+"',Product = '"+str(Product)+"',Qty = '"+str(Qty)+"',Rate = '"+str(Rate)+"',Amount = '"+str(Amount)+"',GrossAmount = '"+str(GrossAmount)+"',SCharge = '"+str(SCharge)+"',Vat ='"+str(Vat)+"',Discount ='"+str(Discount)+"',NetAmount ='"+str(NetAmount)+"' WHERE id = '"+str(id)+"'")
		
		mydb.commit()
		return redirect(url_for('home'))
		
@app.route('/order_delete/<string:id>' ,methods =['POST'])
def order_delete(id):
	mycursor.execute("DELETE FROM addorder WHERE id=%s",[id])
	mydb.commit()
	print('Deleted Successfully')
	return redirect(url_for('order_view'))
#---------------end order---------------------------#	
@app.route('/login',methods=['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
		else:
			return redirect(url_for('home'))
	return render_template('login.html', error=error)
	
	
	
if __name__ == '__main__':
	app.run(port='5000',host='0.0.0.0',debug=True)