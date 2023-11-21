from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserEntityModel(db.Model):
    __tablename__ = "user_entity"
    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.Text, nullable=False)
    given_name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50))
    city = db.Column(db.String(50))
    phone_number = db.Column(db.String(20), nullable=False)
    profile_description = db.Column(db.Text)
    password = db.Column(db.String(50), nullable=False)
 
    def __init__(self, user_id, email, given_name, surname, city, phone_number, profile_description, password):
        self.user_id = user_id
        self.email = email
        self.given_name = given_name
        self.surname = surname
        self.city = city
        self.phone_number = phone_number
        self.profile_description = profile_description
        self.password = password

    def toDict(self):
        return {
            "user_id": self.user_id,
            "email": self.email,
            "given_name": self.given_name,
            "surname": self.surname,
            "city": self.city,
            "phone_number": self.phone_number,
            "profile_description": self.profile_description,
            "password": self.password,
        }

    def __repr__(self):
        return f"UserEntityModel(user_id={self.user_id}, email='{self.email}', given_name='{self.given_name}', surname='{self.surname}', city='{self.city}', phone_number='{self.phone_number}', profile_description='{self.profile_description}', password='{self.password}')"
    
class CaregiverModel(UserEntityModel):
    __tablename__ = "caregiver"
    caregiver_user_id = db.Column(db.Integer, db.ForeignKey('user_entity.user_id', ondelete="CASCADE" ), primary_key=True, nullable=False)
    photo = db.Column(db.Text)
    gender = db.Column(db.String(15))
    caregiving_type = db.Column(db.String(15))
    hourly_rate = db.Column(db.Float)

    def __init__(self, user_id, email, given_name, surname, city, phone_number, profile_description, password, caregiver_user_id=None, photo=None, gender=None, caregiving_type=None, hourly_rate=None):
        super().__init__(user_id, email, given_name, surname, city, phone_number, profile_description, password)
        self.caregiver_user_id = user_id
        self.photo = photo
        self.gender = gender
        self.caregiving_type = caregiving_type
        self.hourly_rate = hourly_rate

    def toDict(self):
        return {
            "user_id": self.user_id,
            "email": self.email,
            "given_name": self.given_name,
            "surname": self.surname,
            "city": self.city,
            "phone_number": self.phone_number,
            "profile_description": self.profile_description,
            "password": self.password,
            "caregiver_user_id": self.caregiver_user_id,
            "photo": self.photo,
            "gender": self.gender,
            "caregiving_type": self.caregiving_type,
            "hourly_rate": self.hourly_rate
        }
    
    def __repr__(self):
        return f"CaregiverModel(user_id={self.user_id}, email='{self.email}', given_name='{self.given_name}', surname='{self.surname}', city='{self.city}', phone_number='{self.phone_number}', profile_description='{self.profile_description}', password='{self.password}', caregiver_user_id={self.caregiver_user_id}, photo={self.photo}, gender='{self.gender}', caregiving_type='{self.caregiving_type}', hourly_rate={self.hourly_rate})"
        

class MemberModel(UserEntityModel):
    __tablename__ = "member"
    member_user_id = db.Column(db.Integer, db.ForeignKey('user_entity.user_id', ondelete="CASCADE" ), primary_key=True, nullable=False)
    house_rules = db.Column(db.Text)

    def __init__(self, user_id, email, given_name, surname, city, phone_number, profile_description, password,  house_rules=None):
        super().__init__(user_id, email, given_name, surname, city, phone_number, profile_description, password)
        self.member_user_id = user_id
        self.house_rules = house_rules
    
    def toDict(self):
        return {
            "user_id": self.user_id,
            "email": self.email,
            "given_name": self.given_name,
            "surname": self.surname,
            "city": self.city,
            "phone_number": self.phone_number,
            "profile_description": self.profile_description,
            "password": self.password,
            "member_user_id": self.member_user_id,
            "house_rules": self.house_rules
        }

    def __repr__(self):
        return f"Member(user_id={self.user_id}, email='{self.email}', given_name='{self.given_name}', surname='{self.surname}', city='{self.city}', phone_number='{self.phone_number}', profile_description='{self.profile_description}', password='{self.password}', member_user_id={self.member_user_id}, house_rules='{self.house_rules}')"
    
class JobModel(db.Model):
    __tablename__ = "job"
    job_id = db.Column(db.Integer, primary_key=True, nullable=False)
    member_user_id = db.Column(db.Integer, db.ForeignKey('member.member_user_id', ondelete="CASCADE" ), nullable=False)
    required_caregiving_type = db.Column(db.String(15))
    other_requirements = db.Column(db.Text)
    date_posted = db.Column(db.Date)

    def __init__(self, job_id, member_user_id, required_caregiving_type, other_requirements, date_posted):
        self.job_id = job_id
        self.member_user_id = member_user_id
        self.required_caregiving_type = required_caregiving_type
        self.other_requirements = other_requirements
        self.date_posted = date_posted
    
    def toDict(self):
        return {
            "job_id": self.job_id,
            "member_user_id": self.member_user_id,
            "required_caregiving_type": self.required_caregiving_type,
            "other_requirements": self.other_requirements,
            "date_posted": self.date_posted
        }

    def __repr__(self):
        return f"JobModel(job_id={self.job_id}, member_user_id={self.member_user_id}, required_caregiving_type='{self.required_caregiving_type}', other_requirements='{self.other_requirements}', date_posted='{self.date_posted}')"
    
class JobApplicationModel(db.Model):
    __tablename__ = "job_application"
    caregiver_user_id = db.Column(db.Integer, db.ForeignKey('caregiver.caregiver_user_id', ondelete="CASCADE" ), primary_key=True, nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job.job_id', ondelete="CASCADE" ), primary_key=True, nullable=False)
    date_applied = db.Column(db.Date)

    def __init__(self, caregiver_user_id, job_id, date_applied):
        self.caregiver_user_id = caregiver_user_id
        self.job_id = job_id
        self.date_applied = date_applied
    
    def toDict(self):
        return {
            "caregiver_user_id": self.caregiver_user_id,
            "job_id": self.job_id,
            "date_applied": self.date_applied
        }
    
    def __repr__(self):
        return f"JobApplicationModel(caregiver_user_id={self.caregiver_user_id}, job_id={self.job_id}, date_applied='{self.date_applied}')"
    
class AddressModel(db.Model):
    __tablename__ = "address"
    member_user_id = db.Column(db.Integer, db.ForeignKey('member.member_user_id', ondelete="CASCADE" ), primary_key=True, nullable=False)
    house_number = db.Column(db.Integer, primary_key=True, nullable=False)
    street = db.Column(db.String(50), primary_key=True, nullable=False)
    town = db.Column(db.String(50), primary_key=True, nullable=False)
    
    def __init__(self, member_user_id, house_number, street, town):
        self.member_user_id = member_user_id
        self.house_number = house_number
        self.street = street
        self.town = town
    
    def toDict(self):
        return {
            "member_user_id": self.member_user_id,
            "house_number": self.house_number,
            "street": self.street,
            "town": self.town
        }

    def __repr__(self):
        return f"AddressModel(member_user_id={self.member_user_id}, house_number={self.house_number}, street='{self.street}', town='{self.town}')"
    
class AppointmentModel(db.Model):
    __tablename__ = "appointment"
    appointment_id = db.Column(db.Integer, primary_key=True, nullable=False)
    carregiver_user_id = db.Column(db.Integer, db.ForeignKey('caregiver.caregiver_user_id', ondelete="CASCADE" ), primary_key=True, nullable=False)
    member_user_id = db.Column(db.Integer, db.ForeignKey('member.member_user_id', ondelete="CASCADE" ), primary_key=True, nullable=False)
    appointment_date = db.Column(db.Date, nullable=False)
    appointment_time = db.Column(db.Time)
    work_hours = db.Column(db.Float)
    status = db.Column(db.String(15))

    def __init__(self, appointment_id, carregiver_user_id, member_user_id, appointment_date, appointment_time, work_hours, status):
        self.appointment_id = appointment_id
        self.carregiver_user_id = carregiver_user_id
        self.member_user_id = member_user_id
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.work_hours = work_hours
        self.status = status

    def toDict(self):
        return {
            "appointment_id": self.appointment_id,
            "carregiver_user_id": self.carregiver_user_id,
            "member_user_id": self.member_user_id,
            "appointment_date": self.appointment_date,
            "appointment_time": self.appointment_time,
            "work_hours": self.work_hours,
            "status": self.status
        }
    
    def __repr__(self):
        return f"Appointment(appointment_id={self.appointment_id}, carregiver_user_id={self.carregiver_user_id}, member_user_id={self.member_user_id}, appointment_date='{self.appointment_date}', appointment_time='{self.appointment_time}', work_hours={self.work_hours}, status='{self.status}')"
    
