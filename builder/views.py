from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from .forms import ResumeForm
from django.shortcuts import render

def profile(request):
    return render(request, 'profile.html')
def generate_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            # Create a BytesIO buffer to hold the PDF data
            buffer = BytesIO()
            p = canvas.Canvas(buffer, pagesize=letter)
            width, height = letter  # Page size dimensions

            # Draw text onto the PDF
            p.drawString(100, height - 100, f"Name: {data['name']}")
            p.drawString(100, height - 120, f"Email: {data['email']}")
            p.drawString(100, height - 140, f"Education: {data['education']}")
            p.drawString(100, height - 160, f"Skills: {data['skills']}")
            p.drawString(100, height - 180, f"Internships: {data['internships']}")
            p.drawString(100, height - 200, f"Projects: {data['projects']}")
            if data.get('experience'):
                p.drawString(100, height - 220, f"Experience: {data['experience']}")
            
            # Finalize the PDF
            p.showPage()
            p.save()

            # Get PDF data from the buffer
            pdf = buffer.getvalue()
            buffer.close()

            # Create an HTTP response with the PDF
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
            return response
    else:
        form = ResumeForm()

    # Render the form template for GET requests
    return render(request, 'resume_form.html', {'form': form})
