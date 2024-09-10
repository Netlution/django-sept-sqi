from django.shortcuts import render

def new_view(request):
    context = {
        'home_us': 'Welcome to Netlution Agency, where we empower businesses through cutting-edge digital solutions. Our team specializes in website design, branding, and marketing strategies tailored to elevate your brand. Let’s help you thrive in the digital landscape. Ready to innovate?'
    }
    return render(request, 'netution/home.html', context)

