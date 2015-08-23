from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from portal.forms import doctorForm, patientForm, profileForm, appointmentForm
from portal.models import doctor, patient, profile, appointment, messages


def index(request) :
	return render(request, 'easydoctor/index.html')


def doctorDashboard(request):
	if 'session_id' not in request.session:
		return redirect('http://localhost:8000/portal/')
	else:
		email = request.session['emailId']
		category = request.session['category']
		if category == 'doctor':
			e = doctor.objects.filter(emailId=email)
			p = profile.objects.filter(emailId=email)
		else :
			e = patient.objects.filter(emailId=email)
			p = profile.objects.filter(emailId=email)
		messageList = []
		m = messages.objects.filter(destination=email)
		for message in m :
			mes = {
				"source" : patient.objects.filter(emailId=message.source).first().firstName,
				"content" : message.content
			}
			messageList.append(mes)
		try:
			data = {
				"name" : "{0} {1}".format(e.first().firstName, e.first().lastName),
				"emailId" : e.first().emailId,
				"age" : p.first().age, 
				"phone" : p.first().phone, 
				"address" : p.first().address, 
				"gender" : p.first().gender,
				"speciality" : e.first().speciality,
				"messageList" : messageList
			} 
		except AttributeError:
			data = {
				"name" : "{0} {1}".format(e.first().firstName, e.first().lastName),
				"emailId" : e.first().emailId,
				"age" : "", 
				"phone" : "", 
				"address" : "", 
				"gender" : "",
				"speciality" : e.first().speciality,
				"messageList" : messageList 
			}
		return render(request, 'easydoctor/doctorDashboard.html', data)


def patientProfile(request):
	if 'session_id' not in request.session:
		return redirect('http://localhost:8000/portal/')
	else:
		email = request.session['emailId']
		category = request.session['category']
		if category == 'doctor':
			e = doctor.objects.filter(emailId=email)
			p = profile.objects.filter(emailId=email)
		else :
			e = patient.objects.filter(emailId=email)
			p = profile.objects.filter(emailId=email)
		try:
			data = {
				"name" : "{0} {1}".format(e.first().firstName, e.first().lastName),
				"emailId" : e.first().emailId,
				"age" : p.first().age, 
				"phone" : p.first().phone, 
				"address" : p.first().address, 
				"gender" : p.first().gender
			} 
		except AttributeError:
			data = {
				"name" : "{0} {1}".format(e.first().firstName, e.first().lastName),
				"emailId" : e.first().emailId,
				"age" : "", 
				"phone" : "", 
				"address" : "", 
				"gender" : ""
			}
		return render(request, 'easydoctor/patientProfile.html', data)

def patientDiagnosis(request):
	if 'session_id' not in request.session:
		return redirect('http://localhost:8000/portal/')
	else:
		email = request.session['emailId']
		category = request.session['category']
		if category == 'doctor':
			e = doctor.objects.filter(emailId=email)
			p = profile.objects.filter(emailId=email)
		else :
			e = patient.objects.filter(emailId=email)
			p = profile.objects.filter(emailId=email)
		try:
			data = {
				"name" : "{0} {1}".format(e.first().firstName, e.first().lastName),
				"emailId" : e.first().emailId,
				"age" : p.first().age, 
				"phone" : p.first().phone, 
				"address" : p.first().address, 
				"gender" : p.first().gender
			} 
		except AttributeError:
			data = {
				"name" : "{0} {1}".format(e.first().firstName, e.first().lastName),
				"emailId" : e.first().emailId,
				"age" : "", 
				"phone" : "", 
				"address" : "", 
				"gender" : ""
			}
		return render(request, 'easydoctor/patientDiagnosis.html', data)


def doctorProfile(request):
	if 'session_id' not in request.session:
		return redirect('http://localhost:8000/portal/')
	else:
		email = request.session['emailId']
		category = request.session['category']
		if category == 'doctor':
			e = doctor.objects.filter(emailId=email)
			p = profile.objects.filter(emailId=email)
		else :
			e = patient.objects.filter(emailId=email)
			p = profile.objects.filter(emailId=email)
		messageList = []
		m = messages.objects.filter(destination=email)
		for message in m :
			mes = {
				"source" : patient.objects.filter(emailId=message.source).first().firstName,
				"content" : message.content
			}
			messageList.append(mes)
		try:
			data = {
				"name" : "{0} {1}".format(e.first().firstName, e.first().lastName),
				"emailId" : e.first().emailId,
				"age" : p.first().age, 
				"phone" : p.first().phone, 
				"address" : p.first().address, 
				"gender" : p.first().gender,
				"speciality" : e.first().speciality,
				"messageList" : messageList
			} 
		except AttributeError:
			data = {
				"name" : "{0} {1}".format(e.first().firstName, e.first().lastName),
				"emailId" : e.first().emailId,
				"age" : "", 
				"phone" : "", 
				"address" : "", 
				"gender" : "",
				"speciality" : e.first().speciality,
				"messageList" : messageList 
			}
		return render(request, 'easydoctor/doctorProfile.html', data)

def doctorDiagnosis(request):
	if 'session_id' not in request.session:
		return redirect('http://localhost:8000/portal/')
	else:
		email = request.session['emailId']
		category = request.session['category']
		if category == 'doctor':
			e = doctor.objects.filter(emailId=email)
			p = profile.objects.filter(emailId=email)
		else :
			e = patient.objects.filter(emailId=email)
			p = profile.objects.filter(emailId=email)
		messageList = []
		m = messages.objects.filter(destination=email)
		for message in m :
			mes = {
				"source" : patient.objects.filter(emailId=message.source).first().firstName,
				"content" : message.content
			}
			messageList.append(mes)
		try:
			data = {
				"name" : "{0} {1}".format(e.first().firstName, e.first().lastName),
				"emailId" : e.first().emailId,
				"age" : p.first().age, 
				"phone" : p.first().phone, 
				"address" : p.first().address, 
				"gender" : p.first().gender,
				"speciality" : e.first().speciality,
				"messageList" : messageList 
			} 
		except AttributeError:
			data = {
				"name" : "{0} {1}".format(e.first().firstName, e.first().lastName),
				"emailId" : e.first().emailId,
				"age" : "", 
				"phone" : "", 
				"address" : "", 
				"gender" : "",
				"speciality" : e.first().speciality,
				"messageList" : messageList
			}
		return render(request, 'easydoctor/doctorDiagnosis.html', data)
			
def doctorAppointments(request):
	if 'session_id' not in request.session:
		return redirect('http://localhost:8000/portal/')
	else:
		email = request.session['emailId']
		category = request.session['category']
		if category == 'doctor':
			e = doctor.objects.filter(emailId=email)
			p = profile.objects.filter(emailId=email)
		else :
			e = patient.objects.filter(emailId=email)
			p = profile.objects.filter(emailId=email)
		messageList = []
		m = messages.objects.filter(destination=email)
		for message in m :
			mes = {
				"source" : patient.objects.filter(emailId=message.source).first().firstName,
				"content" : message.content
			}
			messageList.append(mes)
		appointmentsList = []
		appointments = appointment.objects.filter(doctorEmail=request.session['emailId'])
		for a in appointments :
			ap = {
				"date" : a.next,
				"patientName" : patient.objects.filter(emailId=a.patientEmail).first().firstName
			}
			appointmentsList.append(ap)
		allPatientData = []
		allPatient = patient.objects.all()
		for val in allPatient :
			pat = {
				"name" : "{0} {1}".format(val.firstName, val.lastName),
				"emailId" : val.emailId
			}
			allPatientData.append(pat)
		try:
			data = {
				"name" : "{0} {1}".format(e.first().firstName, e.first().lastName),
				"emailId" : e.first().emailId,
				"age" : p.first().age, 
				"phone" : p.first().phone, 
				"address" : p.first().address, 
				"gender" : p.first().gender,
				"speciality" : e.first().speciality,
				"patientList" : allPatientData,
				"doctorEmailId" : request.session['emailId'],
				"appointmentsList" : appointmentsList,
				"messageList" : messageList
			} 
		except AttributeError:
			data = {
				"name" : "{0} {1}".format(e.first().firstName, e.first().lastName),
				"emailId" : e.first().emailId,
				"age" : "", 
				"phone" : "", 
				"address" : "", 
				"gender" : "",
				"speciality" : e.first().speciality,
				"messageList" : messageList
			}
		return render(request, 'easydoctor/doctorAppointments.html', data)

def patientAppointments(request):
	if 'session_id' not in request.session:
		return redirect('http://localhost:8000/portal/')
	else:
		email = request.session['emailId']
		category = request.session['category']
		if category == 'doctor':
			e = doctor.objects.filter(emailId=email)
			p = profile.objects.filter(emailId=email)
		else :
			e = patient.objects.filter(emailId=email)
			p = profile.objects.filter(emailId=email)
		appointmentsList = []
		appointments = appointment.objects.filter(patientEmail=request.session['emailId'])
		for a in appointments :
			ap = {
				"doctorName" : doctor.objects.filter(emailId=a.doctorEmail).first().firstName,
				"date" : a.next
			}
			appointmentsList.append(ap)
		try:
			data = {
				"name" : "{0} {1}".format(e.first().firstName, e.first().lastName),
				"emailId" : e.first().emailId,
				"age" : p.first().age, 
				"phone" : p.first().phone, 
				"address" : p.first().address, 
				"gender" : p.first().gender,
				"appointmentsList" : appointmentsList
			} 
		except AttributeError:
			data = {
				"name" : "{0} {1}".format(e.first().firstName, e.first().lastName),
				"emailId" : e.first().emailId,
				"age" : "", 
				"phone" : "", 
				"address" : "", 
				"gender" : "",
			}
		return render(request, 'easydoctor/patientAppointments.html', data)


def patientDashboard(request):
	if 'session_id' not in request.session:
		return redirect('http://localhost:8000/portal/')
	else:
		email = request.session['emailId']
		category = request.session['category']
		if category == 'doctor':
			e = doctor.objects.filter(emailId=email)
			p = profile.objects.filter(emailId=email)
		else :
			e = patient.objects.filter(emailId=email)
			p = profile.objects.filter(emailId=email)
		try:
			data = {
				"name" : "{0} {1}".format(e.first().firstName, e.first().lastName),
				"emailId" : e.first().emailId,
				"age" : p.first().age, 
				"phone" : p.first().phone, 
				"address" : p.first().address, 
				"gender" : p.first().gender
			} 
		except AttributeError:
			data = {
				"name" : "{0} {1}".format(e.first().firstName, e.first().lastName),
				"emailId" : e.first().emailId,
				"age" : "", 
				"phone" : "", 
				"address" : "", 
				"gender" : ""
			}
		return render(request, 'easydoctor/patientDashboard.html', data)

def register (request):
	
	category = request.POST['category']
	if category == 'Doctor':
		data = doctorForm(request.POST)
		if data.is_valid():
	  		data.save()
			return(HttpResponse('<p>Thank you</p>'))
		else :
			return(HttpResponse('<p>Could not Register</p>'))
	else :
		data = patientForm(request.POST)
		print data
		if data.is_valid():
	  		data.save()
			return(HttpResponse('<p>Thank you</p>'))
		else :
			return(HttpResponse('<p>Could not Register</p>'))

def showDoctor (request, doctorId):
	e = doctor.objects.filter(id=doctorId)
	doctorData = "{0}</br> {1}</br> {2}</br> {3}".format(e.first().firstName, e.first().lastName, e.first().displayName, e.first().emailId)    
	return(HttpResponse("%s" %doctorData))

def verify (request):
	email = request.POST['emailId']
	password = request.POST['password']
	category = request.POST['category']
	if category == 'doctor':
		e = doctor.objects.filter(emailId=email,password=password)
	else :
		e = patient.objects.filter(emailId=email,password=password)
		
	if e.count() == 1:

		request.session['session_id'] = request.COOKIES.get('sessionid') 
		request.session['category'] = category 
		request.session['firstName'] = e.first().firstName
		request.session['emailId'] = email
		return redirect('http://localhost:8000/portal/'+ category +'Dashboard/')
	else :
		return HttpResponse("Check Credintials")

def logout(request):
    try:
        del request.session['session_id'], request.session['displayName'], request.session['emailId'], request.session['category']
    except KeyError:
        pass
    return redirect('http://localhost:8000/portal/')
    # return HttpResponse("You're logged out.")

def updateProfile(request):
	if 'session_id' not in request.session:
		return redirect('http://localhost:8000/portal/')
	else:
		email = request.session['emailId']
		category = request.session['category']
		gender = request.POST['gender']
		age = request.POST['age']
		phone = request.POST['phone']
		address = request.POST['address']
		if category == 'doctor':
			p = profile.objects.filter(emailId=email)
		else :
			p = profile.objects.filter(emailId=email)
		data = profileForm(request.POST)
		print data
		if data.is_valid():
	  		data.save()
			return(HttpResponse('<p>Thank you</p>'))
		else :
			return(HttpResponse('<p>Could not Update</p>'))

def addAppointment(request):
	name = request.session['firstName']
	date = request.POST['next']
	data = appointmentForm(request.POST)
	print data
	if data.is_valid :
		data.save()
		msg = "Your appointment with Dr. %s is at %s" %(name,date)
		sms(msg)

		return redirect('http://localhost:8000/portal/doctorAppointments/')
	else :
		return HttpResponse("Error Occured")


def sms(msg):
	import plivo

	auth_id = "MAYTEYNZYXYTVLZTM5OT"
	auth_token = "NWZjMDBjY2M1MTVmMDZhODYwOTY0YmI5OTVhNWM4"

	p = plivo.RestAPI(auth_id, auth_token)

	params = {
	    'src': '917278660572', # Sender's phone number with country code
	    'dst' : '917411313860', # Receiver's phone Number with country code
	    'text' : msg, # Your SMS Text Message - English
	    'url' : "", # The URL to which with the status of the message is sent
	    'method' : 'POST' # The method used to call the url
	}

	response = p.send_message(params)
