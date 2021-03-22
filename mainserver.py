from flask import Flask, render_template, url_for, request, redirect
import csv 
#weblink: http://127.0.0.1:5000/

#render_template allows us to send a HTML fle
app = Flask(__name__)
print(__name__)

# @app.route("") is basically like the web pae directory. were "/" is the "main page"

#for the javascript and css files, they are "static" files and we have to create
# a folder called "static" and place them inside that 


#this is the main page
@app.route('/')
def my_home():
	#when using render_template, we have to put the HTML files into a folder called "templates"
	#because thats how render_template works in flask
	return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
	return render_template(page_name)

#allows us to save the contact info in the database.txt
def write_to_file(data):
	with open("database.txt", mode = "a") as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
	with open("database.csv", mode = "a", newline="") as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2,delimiter = ',',quotechar='"',quoting = csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])
#contact info
#GET means browser wants us to send info , POST means browser wants us to save info
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
    	try:
    		data = request.form.to_dict()
    		write_to_csv(data)
    		write_to_file(data)
    		return redirect('/thankyou.html')
    	except:
    		return "Did not save to database!"
    else:
   		return "Something went wrong, try again"





# @app.route('/index.html')
# def my_home():
# 	#when using render_template, we have to put the HTML files into a folder called "templates"
# 	#because thats how render_template works in flask
# 	return render_template("index.html")

# @app.route('/about.html')
# def about():
# 	return render_template("about.html")

# @app.route('/components.html')
# def components():
# 	return render_template("components.html")

# @app.route('/contact.html')
# def contact():
# 	return render_template("contact.html")

# @app.route('/works.html')
# def works():
# 	return render_template("works.html")

