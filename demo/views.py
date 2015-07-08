from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.forms import BigForm


def bigform(request):

	form = BigForm()

	field1 = ''
	field2 = ''
	field3 = None

	if request.method == 'POST':
		form = BigForm(request.POST, request.FILES)
		if form.is_valid():
			field1 = form.cleaned_data.get('field1')
			field2 = form.cleaned_data.get('field2')
			field3 = form.cleaned_data.get('field3') 

			form = BigForm()

	context = {
		'form': form,
		'field1': field1,
		'field2': field2,
		'field3': field3,
	}

	return render_to_response('bigform.html', context, context_instance=RequestContext(request))