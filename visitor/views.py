from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.template.loader import render_to_string

from users.models import User
from doctor.models import DoctorRole

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from accounts.views import home_page
# from doctor.views import doctor_details, product_home, doctors_dashboard


# Create your views here.
def home_page(request):
    print('Hello from prue')
    doctor = User.objects.filter(is_active=True, is_doctor=True)
    doctor = doctor.order_by('username')
    doc_roles = DoctorRole.objects.all()
            
    # paginator = Paginator(doctor, 12)
    # page = request.GET.get('page')
    # try:
    #     doctor = paginator.page(page)
    # except PageNotAnInteger:
    #     doctor = paginator.page(1)
    # except EmptyPage:
    #     doctor = paginator.page(paginator.num_pages)
    if request.user.is_authenticated:
        if request.user.is_patient:
            return redirect('patient:patient_dashboard')
    else:
        return render(request,'visitor/view.html', {'doctor': doctor, "doc_roles": doc_roles,})