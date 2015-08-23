from django.contrib import admin

# Register your models here.

from portal.models import doctor, patient, profile, diagnosis, appointment, onlineConsultation , allergie, messages



class doctorAdmin(admin.ModelAdmin):
	list_display = ['firstName', 'lastName', 'emailId','speciality']
	class Meta:
		model = doctor

class patientAdmin(admin.ModelAdmin):
	list_display = ['firstName', 'lastName', 'emailId']
	class Meta:
		model = patient

class profileAdmin(admin.ModelAdmin):
	list_display = ['gender','age','phone','address', 'emailId']
	class Meta:
		model = profile

class diagnosisAdmin(admin.ModelAdmin):
	list_display = ['ailment','doctorName','doctorEmail']
	class Meta:
		model = diagnosis

class messagesAdmin(admin.ModelAdmin):
	list_display = ['source','destination','content']
	class Meta:
		model = messages		

class appointmentAdmin(admin.ModelAdmin):
	list_display = ['last','next', 'doctorEmail', 'patientEmail']
	class Meta:
		model = appointment

class consultationAdmin(admin.ModelAdmin):
	list_display = ['last','next']
	class Meta:
		model = onlineConsultation

class allergieAdmin(admin.ModelAdmin):
	list_display = ['email','allergies']
	class Meta:
		model = allergie

admin.site.register(doctor, doctorAdmin)
admin.site.register(patient, patientAdmin)
admin.site.register(profile, profileAdmin)
admin.site.register(diagnosis, diagnosisAdmin)
admin.site.register(appointment, appointmentAdmin)
admin.site.register(onlineConsultation, consultationAdmin)
admin.site.register(allergie, allergieAdmin)
admin.site.register(messages, messagesAdmin)