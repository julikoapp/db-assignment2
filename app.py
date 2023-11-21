
from flask import Flask, render_template, request, redirect,url_for
from accounts.models import db, MemberModel, UserEntityModel, CaregiverModel, JobApplicationModel, JobModel, AddressModel, AppointmentModel

app = Flask(__name__, template_folder='./templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:HoChaYoung@localhost:5432/caregiverdb'
# db = SQLAlchemy(app)
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template('base.html')

@app.route('/member/get', methods=['GET', 'POST'])
def get_members():
    members = MemberModel.query.all()
        
    return render_template('get_member.html', members=members )

@app.route('/member/create', methods=['GET', 'POST'])
def create_member():
    if request.method == 'GET':
        return render_template('create_member.html')
 
    if request.method == 'POST':
        user_id = request.form['user_id']
        email = request.form['email']
        given_name = request.form['given_name']
        surname = request.form['surname']
        city = request.form['city']
        phone_number = request.form['phone_number']
        profile_description = request.form['profile_description']
        password = request.form['password']
        house_rules = request.form['house_rules']

        member = MemberModel(user_id=user_id, given_name=given_name, 
                                      surname=surname,
                                   email=email,
                                   city=city,
                                     phone_number=phone_number, 
                                     profile_description=profile_description, 
                                     password=password, 
                             house_rules=house_rules)
        
        db.session.add(member)
        db.session.commit()
        return redirect('/member/get')
    
@app.route('/caregiver/create', methods=['GET', 'POST'])
def create_caregiver():
    if request.method == 'GET':
        return render_template('create_caregiver.html')
    
    if request.method == "POST":
        user_id = request.form['user_id']
        email = request.form['email']
        given_name = request.form['given_name']
        surname = request.form['surname']
        city = request.form['city']
        phone_number = request.form['phone_number']
        profile_description = request.form['profile_description']
        password = request.form['password']
        gender = request.form['gender']
        caregiving_type = request.form['caregiving_type']
        hourly_rate = request.form['hourly_rate']

        caregiver = CaregiverModel(user_id=user_id, email=email, 
                                   given_name=given_name, surname=surname, 
                                   city=city, phone_number=phone_number,
                                   profile_description=profile_description,
                                   password=password, gender = gender,
                                   caregiving_type=caregiving_type,
                                   hourly_rate=hourly_rate)
        db.session.add(caregiver)
        db.session.commit()
        return redirect('/caregiver/get')

@app.route('/caregiver/get', methods=['GET', 'POST'])
def get_caregivers():
    caregivers = CaregiverModel.query.all()
    return render_template('get_caregiver.html',caregivers = caregivers)

@app.route('/member/update/<int:id>',methods = ['GET','POST'])
def update_member(id):
    member = MemberModel.query.filter_by(user_id=id).first()
    if request.method == 'POST':
        if member:
            db.session.delete(member)
            db.session.commit()
            email = request.form['email']
            city = request.form['city']
            phone_number = request.form['phone_number']
            profile_description = request.form['profile_description']
            house_rules = request.form['house_rules']

            member = MemberModel( user_id=id, given_name=member.given_name, 
                                      surname=member.surname,
                                   email=email,
                                   city=city,
                                     phone_number=phone_number, 
                                     profile_description=profile_description, 
                                     password=member.password, 
                             house_rules=house_rules)
 
            db.session.add(member)
            db.session.commit()
            return redirect('/members/get')
        return f"Member with id = {id} Does not exist"
 
    return render_template('update_member.html', member = member)

@app.route('/caregiver/update/<int:id>',methods = ['GET','POST'])
def update_caregiver(id):
    caregiver = CaregiverModel.query.filter_by(user_id=id).first()
    if request.method == 'POST':
        if caregiver:
            db.session.delete(caregiver)
            db.session.commit()
            email = request.form['email']
            city = request.form['city']
            phone_number = request.form['phone_number']
            profile_description = request.form['profile_description']
            # phtoto
            gender = request.form['gender']
            caregiving_type = request.form['caregiving_type']
            hourly_rate = request.form['hourly_rate']

            caregiver = CaregiverModel(user_id=id, email=email, 
                                   given_name=caregiver.given_name, surname=caregiver.surname, 
                                   city=city, phone_number=phone_number,
                                   profile_description=profile_description,
                                   password=caregiver.password, gender = gender,
                                   caregiving_type=caregiving_type,
                                   hourly_rate=hourly_rate)
 
            db.session.add(caregiver)
            db.session.commit()
            return redirect('/caregivers/get')
        return f"caregiver with id = {id} Does not exist"
    return render_template('update_caregiver.html', caregiver = caregiver)


@app.route('/member/delete/<int:id>', methods=['GET', 'POST'])
def delete_member(id):
    member = MemberModel.query.filter_by(user_id=id).first()
    if request.method == 'POST':
        if member:
            db.session.delete(member)
            db.session.commit()
            return redirect('/members/get')
        abort(404)
 
    return render_template('delete_member.html', member=member)

@app.route('/caregiver/delete/<int:id>', methods=['GET','POST'])
def delete_caregiver(id):
    caregiver = CaregiverModel.query.filter_by(user_id=id).first()
    if request.method == 'POST':
        if caregiver:
            db.session.delete(caregiver)
            db.session.commit()
            return redirect('/caregiver/get')
        abort(404)
 
    return render_template('delete_caregiver.html', caregiver = caregiver)




if __name__ == "__main__":
    app.run()
