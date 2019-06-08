import pandas as pd
import io
import json
import matplotlib.pyplot as plt
from django.http import JsonResponse, HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from manage import predict


# Create your views here.


@csrf_exempt
# per evitar utilitzar un token a les peticions post i fer test
def index(request):
    if request.method == 'POST':
        formulariPacient = request.body.decode("utf=8")
        parsingData = formulariPacient[13] + formulariPacient[14] + ',' + formulariPacient[10] + formulariPacient[11] + ',' + formulariPacient[5] + formulariPacient[6] + formulariPacient[7] + formulariPacient[8] + ','
        for i in range(14, len(formulariPacient)):
            if formulariPacient[i] is "=":
                parsingData = parsingData + formulariPacient[i+1]
                if i+1 < 44:
                    if formulariPacient[i+2] is not "&":
                        parsingData = parsingData + formulariPacient[i + 2]
                        if formulariPacient[i+3] is not "&":
                            parsingData = parsingData + formulariPacient[i + 3]
                            if formulariPacient[i+4] is not "&":
                                parsingData = parsingData + formulariPacient[i + 4]
                parsingData = parsingData + ","
        parsingData = parsingData[:-1]
        predict(parsingData)
        return render(request, "resposta.html")
    else:
        return render(request, "index.html")


def data(request):
    with open('./data.json') as json_file:
        data = json.load(json_file)
        return JsonResponse(data)

@csrf_exempt
def send(request):
    return render(request, "index.html")


def plot(request):
    with open('./data.json') as json_file:
        data = json.load(json_file)
    df = pd.read_csv('reg.csv', delimiter=';')
    filterDiag = (df[(df['diagnostic'] == data['prediction'])])
    figure = plt.figure(1)
    axes = figure.add_axes([0.15, 0.15, 0.75, 0.75])
    axes.hist(filterDiag['edat'])
    axes.set_title("Edat mitjana")
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(figure)
    canvas.print_png(buf)
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    return response


def plot1(request):
    with open('./data.json') as json_file:
        data = json.load(json_file)
    df = pd.read_csv('reg.csv', delimiter=';')
    filterDiag = (df[(df['diagnostic'] == data['prediction'])])
    figure = plt.figure(1)
    axes = figure.add_axes([0.15, 0.15, 0.75, 0.75])
    axes.hist(filterDiag['sexe'])
    axes.set_title("Sexe mitjana")
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(figure)
    canvas.print_png(buf)
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    return response


def plot2(request):
    with open('./data.json') as json_file:
        data = json.load(json_file)
    df = pd.read_csv('reg.csv', delimiter=';')
    filterDiag = (df[(df['diagnostic'] == data['prediction'])])
    figure = plt.figure(1)
    axes = figure.add_axes([0.15, 0.15, 0.75, 0.75])
    axes.hist(filterDiag['pes'])
    axes.set_title("Mitjana del pes")
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(figure)
    canvas.print_png(buf)
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    return response