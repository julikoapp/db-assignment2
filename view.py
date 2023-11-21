from flask import Flask, render_template, request, redirect
from accounts.models import UserEntityModel, CaregiverModel, MemberModel, JobModel, JobApplicationModel, AddressModel, AppoinmentModel, db
from flask_login import login_required, current_user


app = Flask(__name__)

@app.route('/')
def main_page():
    return "HELLO WORLD"
    return render_template('./templates/main_page.html')


@app.route('/member/create', methods=['GET', 'POST'])
def create_member():
    if request.method == 'GET':
        return render_template('templates/member_page.html')
 
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

        member = MemberModel(user_id, email, given_name, surname, city, 
                             phone_number, profile_description, password, 
                             house_rules=house_rules)
        db.session.add(member)
        db.session.commit()
        return redirect('/data')



@app.route('/caregiver/create', methods=['GET', 'POST'])
def create_caregiver():
    if request.method == 'GET':
        return render_template('templates/caregiver_page.html')
    
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
        return redirect('/data')
    
@app.route('/members/get')
def get_members():
    members = MemberModel.query.all()
    return render_template('templates/members.html',members = members)

@app.route('/caregivers/get')
def get_caregivers():
    caregivers = CaregiverModel.query.all()
    return render_template('templates/caregivers.html',caregivers = caregivers)

@app.route('/members/update/<int:id>',methods = ['GET','POST'])
def update_member(id):
    member = MemberModel.query.filter_by(user_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(member)
            db.session.commit()
            email = request.form['email']
            # if (email == ""):
            #     email = member.email
            city = request.form['city']
            # if (city == ""):
            #     city = member.city
            phone_number = request.form['phone_number']
            # if (phone_number == ""):
            #     phone_number = member.phone_number
            profile_description = request.form['profile_description']
            # if (profile_description == ""):
            #     profile_description = member.profile_description
            house_rules = request.form['house_rules']
            # if (house_rules == ""):
            #     house_rules = member.house_rules

            member = MemberModel( user_id=id, member_user_id = id, given_name=member.given_name, 
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
 
    return render_template('templates/update_member.html', member = member)

@app.route('/caregivers/update/<int:id>',methods = ['GET','POST'])
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
    return render_template('templates/update_caregiver.html', caregiver = caregiver)


@app.route('/members/create_job', methods=['GET', 'POST'])
@login_required
def create_job():
    if isinstance(current_user, MemberModel):
        # Only allow access to MemberModel users
        if request.method == 'POST':
            # Handle job creation logic here
            return "Job created successfully"
        else:
            # Render the job creation form
            return render_template('create_job.html')
    else:
        # Redirect to unauthorized page if user is not a MemberModel
        return redirect('/unauthorized')
