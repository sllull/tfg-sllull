import pandas as pd
import io
import matplotlib.pyplot as plt
from django.http import JsonResponse, HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from domain.connectionBBDD import insertData, selectPrediction
from domain.readJSON import getJSON
from manage import predict


# Create your views here.


@csrf_exempt
# per evitar utilitzar un token a les peticions post i fer test
def index(request):
    if request.method == 'POST':
        formPatient = request.body.decode("utf=8")
        parsingData = parsingForm(formPatient)
        predict(parsingData)
        return render(request, "resposta.html")
    else:
        return render(request, "index.html")


def parsingForm (data):
    parsingData = data[13] + data[14] + ',' + data[10] + data[11] + ',' + data[5] + \
                  data[6] + data[7] + data[8] + ','
    for i in range(14, len(data)):
        if data[i] is "=":
            parsingData = parsingData + data[i + 1]
            if i + 1 < 44:
                if data[i + 2] is not "&":
                    parsingData = parsingData + data[i + 2]
                    if data[i + 3] is not "&":
                        parsingData = parsingData + data[i + 3]
                        if data[i + 4] is not "&":
                            parsingData = parsingData + data[i + 4]
            parsingData = parsingData + ","
    parsingData = parsingData[:-1]
    return parsingData


def data(request):
    data = getJSON()
    return JsonResponse(data)


@csrf_exempt
def send(request):
    insertData()
    return HttpResponse("La predicció s'ha guardat correctament")


def plot(request):
    data = getJSON()
    # df = pd.read_csv('reg.csv', delimiter=';')
    # filterDiag = (df[(df['diagnostic'] == data['prediction'])])
    filterDiag = selectPrediction( data['prediction'])
    figure, (ax1, ax2, ax3) = plt.subplots(1, 3)
    figure.suptitle('Gràfiques de les variables més importants')
    ax2.hist(filterDiag['edat'])
    ax2.set_title("Mitjana de l'edat")
    ax1.hist(filterDiag['sexe'], color='red')
    ax1.set_title("Mitjana del Sexe")
    ax3.hist(filterDiag['pes'], color='green')
    ax3.set_title("Mitjana del pes")
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(figure)
    canvas.print_png(buf)
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    return response


def plot1(request):
    data = getJSON()
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
    data = getJSON()
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