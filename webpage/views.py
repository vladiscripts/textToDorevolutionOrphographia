from django.shortcuts import render

from webpage.forms import InputForm, OutputForm
from toDO import ToDO


# Create your views here.
def convertpage(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InputForm(request.POST)
        output = OutputForm(request.POST)
        # output.text=''
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(request.POST)
            print(form.cleaned_data)
            data = form.cleaned_data
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')
            to_do = ToDO()
            output = to_do.convert(form['do'].value())
            # output.text = form['do'] # .replace('jj', '1111111111111111111')
            # output = form['do'] # .replace('jj', '1111111111111111111')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InputForm()
        output = OutputForm()

    return render(request, 'webpage/form.html', {'form': form, 'output': output})
