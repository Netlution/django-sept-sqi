from django.shortcuts import render

def new_view(request):
    context = {
        'my_name': 'Ajagun Samuel',
        'is_dark': True,
        'students': ["Abdul-Rahman", "Joseph", "Sam", "Gbemisola", "Solomon", "Dr shina"]
    }
    return render(request, 'dtl/dtl_example.html', context)
    
