from flask import Flask,render_template,request,session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crab-base.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    photo = db.Column(db.String(200), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    coordinates = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    photo = db.Column(db.LargeBinary, nullable=False)  # Используем BLOB для хранения фотографий
    is_active = db.Column(db.Boolean, default=True)


@app.route('/admin',methods = ['POST','GET'])
def admiin():
   if request.method =='POST':
        login = request.form['login']
        password = request.form['password']
        print(login,password)
        if login == 'admin' and password == 'root':
  
            return render_template('add_product.html')
   else:
       
    return render_template('admin.html')

@app.route('/product',methods = ['GET','POST'])
def product():
  
    return render_template('add_product.html',dct)

@app.route('/city',methods = ['GET','POST'])
def city():
    if request.method == 'POST':
        name = request.form['city-name']
        phone = request.form['city-phone']
        coordinates = request.form['city-coordinates']
        is_active = 'city-active' in request.form

        city = City(name=name, phone=phone, coordinates=coordinates, is_active=is_active)
        db.session.add(city)
        db.session.commit()

        return 'City added successfully!'
    
    
    return render_template('add_city.html')

@app.route('/review',methods = ['GET','POST'])
def review():
    if request.method == 'POST':
        author_name = request.form.get('review-author')
        text = request.form.get('review-text')
        photo = request.files['review-photo'].read()  # Читаем фотографию как бинарные данные
        is_active = True if request.form.get('review-active') else False

        # Сохранение данных в модель Review
        review = Review(author_name=author_name, text=text, photo=photo.filename, is_active=is_active)
        db.session.add(review)
        db.session.commit()

        return 'Отзыв успешно сохранен'
    return render_template('add_review.html')

@app.route('/')
def index():
    cities = City.query.all()
    reviews = Review.query.all()
    return render_template('index.html',cities=cities,reviews=reviews)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    