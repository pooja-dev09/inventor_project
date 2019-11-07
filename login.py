from flask import *
from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
import os
import ast  
bootstrap = Bootstrap(app)
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = './static/upload/'
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
	mycursor.execute("SELECT * FROM adduser WHERE id= %s",[id])
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
	return redirect(url_for('category_view'))
	

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
	return redirect(url_for('brand_view'))
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
		id = str(request.form.get('id'))
		mycursor.execute("UPDATE addcompany SET CompanyName= '"+str(Company_name)+"',ChargeAmount = '"+str(Charge_amount)+"',VatCharge ='"+str(Vat_charge)+"',Address = '"+str(Address)+"',phone = '"+str(Phone)+"',Country = '"+str(Country)+"',Message = '"+str(Message)+"',Currency = '"+str(Currency)+"' WHERE id = '"+str(id)+"'")
		mydb.commit()
		return redirect(url_for('home'))
	

	
@app.route('/company_delete/<string:id>' ,methods =['POST'])
def company_delete(id):
	mycursor.execute("DELETE FROM addcompany WHERE id=%s",[id])
	mydb.commit()
	print('Deleted Successfully')
	return redirect(url_for('company_view'))
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
		print(ProductName)
		print(Sku)
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
		id = str(request.form.get('id'))
		query = ("UPDATE addproduct SET ProductName= '"+str(Product_name)+"',Sku = '"+str(Sku)+"',Price ='"+str(Price)+"',Qty = '"+str(Qty)+"',Description = '"+str(Description)+"',Brands = '"+str(Brands)+"',Category = '"+str(Category)+"',Store = '"+str(Store)+"',Availability = '"+str(Availability)+"' WHERE id = '"+str(id)+"'")
		mycursor.execute(query)
		print(query)
		print(mycursor.rowcount, "record(s) affected")
		mydb.commit()
		print('djbvijv')
		return redirect(url_for('product_view'))
	
@app.route('/product_delete/<string:id>' ,methods =['POST'])
def product_delete(id):
	mycursor.execute("DELETE FROM addproduct WHERE id=%s",[id])
	mydb.commit()
	print('Deleted Successfully')
	return redirect(url_for('product_view'))
	
	

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
		
		Product = ast.literal_eval(Product)
		Qty = ast.literal_eval(Qty)
		Rate = ast.literal_eval(Rate)
		Amount = ast.literal_eval(Amount)
		for i in range(len(Product)):
			sql = "INSERT INTO addorder (CustomerName,CustomerAddress,CustomerPhone,Product,Qty,Rate,Amount,GrossAmount,SCharge,Vat,Discount,NetAmount) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val=(CustomerName,CustomerAddress,CustomerPhone,Product[i],Qty[i],Rate[i],Amount[i],GrossAmount,SCharge,Vat,Discount,NetAmount)
			result = mycursor.execute(sql,val)
			mydb.commit()
		
		return  redirect(url_for('order_view',new = new))
	else:
		
		# all = []
		# product = request.form.get('product')
		# print(product)
		# mycursor.execute("SELECT ProductName,Price FROM addproduct")
		# rowcursor=mycursor.fetchall()
		# print(rowcursor)
		# for i in rowcursor:
			# ProductName = i[0]
			# Price = i[1]
			# data = {'ProductName':ProductName,'Price':Price}
			# all.append(data)
			
		return render_template('order_add.html')

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
	results = []
	search = request.args.get('q')
	mycursor.execute("SELECT * from addproduct WHERE ProductName like '%"+search+"%' ")
	rowcursor=mycursor.fetchall()
	for i in rowcursor:
		ProductName = i[1]
		Price = i[4]
		data = {'value':ProductName,'data':Price}
		results.append(data)
	return jsonify(matching_results=results)


		
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
		id = str(request.form.get('id'))
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
#----------------start store-------------------------#
@app.route('/store_add',methods=['GET','POST'])
def store_add():
	if (request.method == 'POST'):
		Store_name = str(request.form.get('store_name'))
		Status = str(request.form.get('status'))
		sql = "INSERT INTO addstore (StoreName,Status) VALUES (%s,%s)"
		val = (Store_name,Status)
		result = mycursor.execute(sql,val)
		mydb.commit()
		return  redirect(url_for('store_view'))
	else:
		return render_template('store_add.html')
		
		
@app.route('/store_view')		
def store_view():
	all = []
	mycursor.execute("SELECT * FROM addstore")
	rowcursor=mycursor.fetchall()
	for i in rowcursor:
		id = i[0]
		StoreName = i[1]
		Status = i[2]
		data = {'id':id,'StoreName':StoreName,'Status':Status}
		all.append(data)
	return render_template('store_view.html', results = all) 
	
@app.route('/store_edit/<string:id>')
def store_edit(id):
	row = []
	mycursor.execute("SELECT * FROM addstore WHERE id= %s",[id])
	new = mycursor.fetchall()
	for j in new:
		id = j[0]
		StoreName = j[1]
		Status = j[2]
		data = {'StoreName':StoreName,'Status':Status,'id':id,}
		row.append(data)
	return render_template('store_edit.html', row = row)

@app.route('/store_update',methods=['POST'])
def store_update():
	if (request.method == 'POST'):
		StoreName = str(request.form.get('store_name'))
		Status = str(request.form.get('status'))
		id = str(request.form.get('id'))
		mycursor.execute("UPDATE addstore SET StoreName = '"+str(StoreName)+"',Status = '"+str(Status)+"' WHERE id = '"+str(id)+"'")
		mydb.commit()
		return redirect(url_for('home'))
	

	
@app.route('/store_delete/<string:id>' ,methods =['POST'])
def store_delete(id):
	mycursor.execute("DELETE FROM addstore WHERE id=%s",[id])
	mydb.commit()
	print('Deleted Successfully')
	return redirect(url_for('store_view'))

#-----------------order end------------------#
#------------------attributes start------------------#
@app.route('/attributes_add',methods=['GET','POST'])
def attributes_add():
	if (request.method == 'POST'):
		Attributes_name = str(request.form.get('attributes_name'))
		Status = str(request.form.get('status'))
		sql = "INSERT INTO addattributes(AttributeName,Status) VALUES (%s,%s)"
		val = (Attributes_name,Status)
		result = mycursor.execute(sql,val)
		mydb.commit()
		return  redirect(url_for('attributes_view'))
	else:
		return render_template('attributes_add.html')
		
		
@app.route('/attributes_view')		
def attributes_view():
	all = []
	mycursor.execute("SELECT * FROM addattributes")
	rowcursor=mycursor.fetchall()
	for i in rowcursor:
		id = i[0]
		AttributeName = i[1]
		Status = i[2]
		data = {'id':id,'AttributeName':AttributeName,'Status':Status}
		all.append(data)
	return render_template('attributes_view.html', results = all) 
	
@app.route('/attributes_edit/<string:id>')
def attributes_edit(id):
	row = []
	mycursor.execute("SELECT * FROM addattributes WHERE id= %s",[id])
	new = mycursor.fetchall()
	for j in new:
		id = j[0]
		AttributeName = j[1]
		Status = j[2]
		data = {'AttributeName':AttributeName,'Status':Status,'id':id,}
		row.append(data)
	return render_template('attributes_edit.html', row = row)

@app.route('/attributes_update',methods=['POST'])
def attributes_update():
	if (request.method == 'POST'):
		AttributeName = str(request.form.get('attributes_name'))
		Status = str(request.form.get('status'))
		id = str(request.form.get('id'))
		mycursor.execute("UPDATE addattributes SET AttributeName = '"+str(AttributeName)+"',Status = '"+str(Status)+"' WHERE id = '"+str(id)+"'")
		mydb.commit()
		return redirect(url_for('home'))
	

	
@app.route('/attributes_delete/<string:id>' ,methods =['POST'])
def attributes_delete(id):
	mycursor.execute("DELETE FROM addattributes WHERE id=%s",[id])
	mydb.commit()
	print('Deleted Successfully')
	return redirect(url_for('attributes_view'))
	
#----------------------login-------------------------------------------------------#
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')	
	
class RegisterForm(FlaskForm):
	email = StringField('email',validators=[InputRequired(),Email(message='Invalid email'),Length(max=50)])
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	cpassword = PasswordField('cpassword', validators=[InputRequired(), Length(min=8, max=80)])
	firstname = PasswordField('firstname', validators=[InputRequired(), Length(min=5, max=80)])
	lastname  = PasswordField('lastname', validators=[InputRequired(), Length(min=5, max=80)])
	phone = StringField('phone', validators=[InputRequired(), Length(min=8, max=80)])
	gender = RadioField('gender', choices = [('M','Male'),('F','Female')])
	
	
@app.route('/login',methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		passwordf = form.password.data
		Username = form.username.data
		mycursor.execute("SELECT * from adduser WHERE Username = '%s' AND Password = '%s'" % (Username, passwordf))
		rowcursor=mycursor.fetchall()
		print(rowcursor)
		for i in rowcursor:
			email = i[3]
			print(email)
		length =len(rowcursor)
		if length > 0:
			session['email']=email
			return redirect(url_for('home'))
	
		else:
			return'<h3>Invalid Username or Password </h3>'

	return render_template('login.html', form=form)
@app.route('/profile', methods = ['GET','POST'])
def profile():
	new = []
	if 'email' in session:  
		s = session['email'];  
		mycursor.execute("SELECT * from adduser  WHERE Email = '%s'" % s)
		rowcursor=mycursor.fetchall()
		print(rowcursor)
		for i in rowcursor:
			id = i[0]
			Group = i[1]
			Username = i[2]
			Email = i[3]
			Firstname = i[5]	
			Lastname = i[6]
			Phone = i[7]
			Gender = i[8]
			print(new)
			data = {'id':id,'Group':Group,'Username':Username,'Email':Email,'Firstname':Firstname,'Lastname':Lastname,'Phone':Phone,'Gender':Gender}
			new.append(data)
			
			
		return render_template('profile.html',result = new) 
	else:
		return redirect(url_for('home'))
@app.route('/setting', methods = ['GET','POST'])
def setting():
	row = []
	if 'email' in session:  
		s = session['email'];  
		mycursor.execute("SELECT * from adduser  WHERE Email = '%s'" % s)
		rowcursor=mycursor.fetchall()
		for i in rowcursor:
			id = i[0]
			Group = i[1]
			Username = i[2]
			Email = i[3]
			Password = i[4]
			Firstname = i[5]	
			Lastname = i[6]
			Phone = i[7]
			Gender = i[8]
			data = {'id':id,'Group':Group,'Email':Email,'Firstname':Firstname,'Lastname':Lastname,'Password':Password,'Phone':Phone,'Gender':Gender}
			row.append(data)
		return render_template('setting.html', row = row)


@app.route('/sinup',methods=['GET', 'POST'])
def sinup():
	form = RegisterForm()
	if form.validate_on_submit():
		username = form.username.data
		email = form.email.data
		password  = form.password.data
		cpassword = form.cpassword.data
		firstname = form.firstname.data
		lastname = form.lastname.data
		phone = form.phone.data
		gender = form.gender.data
		if (password == cpassword):
		
			sql = "INSERT INTO adduser (Username,Email,Password,FirstName,LastName,Phone,Gender) VALUES (%s,%s,%s,%s,%s,%s,%s)"
			val = (username,email,password,firstname,lastname,phone,gender)
			result = mycursor.execute(sql,val)
			mydb.commit()

		return redirect(url_for('login'))
	return render_template('sinup.html',form=form)
	
if __name__ == '__main__':
	app.run(port='5000',host='0.0.0.0',debug=True)