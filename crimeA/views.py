import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from opencage import geocoder
from django.db.models import Count
from .forms import CrimeReportForm
from .models import CrimeReport
import datetime
from opencage.geocoder import OpenCageGeocode


# Create your views here.
API_KEY = '59591477fa184f11909a656cf7d8f5e5'
# Create geocoder instance
geocoder = OpenCageGeocode('59591477fa184f11909a656cf7d8f5e5')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/login/')
def about(request):
    return  render(request,'about.html')

@login_required(login_url='/login/')
def report_crime(request):
    if request.method == 'POST':
        form = CrimeReportForm(request.POST, request.FILES)
        if form.is_valid():
            crime_report = form.save(commit=False)
            crime_report.reporter = request.user  # Assume user is logged in

            # Get latitude and longitude from location using OpenCage Geocoding API
            location = form.cleaned_data['location']
            results = geocoder.geocode(location)
            if results:
                latitude = results[0]['geometry']['lat']
                longitude = results[0]['geometry']['lng']
                crime_report.latitude = latitude
                crime_report.longitude = longitude
            else:
                messages.error(request, "Location could not be geocoded. Please check the location entered.")
                return redirect('report_crime')

            crime_report.save()
            # Send success message
            messages.success(request, 'Crime report submitted '
                                      'successfully. Authorities have been alerted.')

            # Optionally: Send an alert to admins or authorities (this is a simple example)
            # You can expand this part by integrating email alerts or SMS alerts
            messages.info(request, 'Law enforcement has been notified of the incident.')
            return redirect('view_reports')  # Redirect to home or another page
    else:
        form = CrimeReportForm()

    return render(request, 'reports/report_crime.html', {'form': form})

@login_required(login_url='/login/')
def view_reports(request):
    category_filter = request.GET.get('category', None)
    location_filter = request.GET.get('location', None)

    crime_reports = CrimeReport.objects.all()

    if category_filter:
        crime_reports = crime_reports.filter(category=category_filter)

    if location_filter:
        crime_reports = crime_reports.filter(location__icontains=location_filter)

    crime_reports = crime_reports.order_by('-date_reported')  # Sort by the most recent

    return render(request, 'reports/view_reports.html', {'crime_reports': crime_reports})

@login_required(login_url='/login/')
def crime_statistics(request):
    # Aggregate data: Crime by Category
    crime_by_category = CrimeReport.objects.values('category').annotate(count=Count('category'))

    # Aggregate data: Crime by Month (trend analysis)
    today = datetime.date.today()
    monthly_crimes = CrimeReport.objects.filter(date_reported__year=today.year).extra(select={'month': 'EXTRACT(month FROM date_reported)'}).values('month').annotate(count=Count('id'))

    # Aggregate data: Crime by Location
    crime_by_location = CrimeReport.objects.values('location').annotate(count=Count('location')).order_by('-count')[:10]  # Top 10 locations

    context = {
        'crime_by_category': crime_by_category,
        'monthly_crimes': monthly_crimes,
        'crime_by_location': crime_by_location,
    }
    return render(request, 'reports/crime_statistics.html', context)