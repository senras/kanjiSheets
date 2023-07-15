from django.shortcuts import render, redirect
from .forms import InputKanjiForm
from django.http import HttpResponse
from django.views import View

from .utils import render_to_pdf
from .kanjivg_utils.utils import FindSvg

data = {
    "kanjiInput": "漢字",
}


def index(request):
    if request.method == 'POST':
        form = InputKanjiForm(request.POST)
        if form.is_valid():
            # kanjiInput get the data from the form
            kanjiInput = form.cleaned_data['kanjiInput']
            repetitions = form.cleaned_data['columnasInput']
            kanjiSvgCollection = []
            for element in kanjiInput:
                kanjiSvg = FindSvg(element)
                kanjiSvgCollection.append(kanjiSvg)
            pdf = render_to_pdf(
                'pdf2.html', {'kanjis': kanjiSvgCollection, 'repetitions': repetitions})
            return HttpResponse(pdf, content_type='application/pdf')
            # return render(request, "displaySheet.html", {'kanjis': kanjiSvgCollection})
    else:
        form = InputKanjiForm()
    return render(request, 'index.html', {'form': form})


def displaySheet(request):
    return render(request, 'displaySheet.html')
