from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    # Jos käyttäjä lähettää lomakkeen (painaa "Lisää"-nappia)
    if request.method == 'POST':
        title = request.POST.get('title') # Haetaan tekstikentän arvo
        if title: # Jos kenttä ei ollut tyhjä
            Task.objects.create(title=title) # Luodaan uusi tehtävä tietokantaan
        return redirect('task_list') # Ladataan sivu uudelleen, jotta uusi tehtävä näkyy

    # Haetaan kaikki tehtävät (tämä tapahtuu, jos sivu vain ladataan normaalisti)
    tasks = Task.objects.all()
    return render(request, 'todo_app/index.html', {'tasks': tasks})

# Uusi näkymä tehtävän poistamiseen
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id) # Etsitään oikea tehtävä ID:n perusteella
    task.delete() # Poistetaan se tietokannasta
    return redirect('task_list') # Palataan takaisin etusivulle