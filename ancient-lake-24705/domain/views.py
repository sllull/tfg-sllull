from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from manage import predict

# Create your views here.


@csrf_exempt
# per evitar utilitzar un token a les peticions post i fer test
def index(request):
    if request.method == 'POST':
        formulariPacient = request.body.decode("utf=8")
        parsingData = ""
        for i in range(len(formulariPacient)):
            if formulariPacient[i] is "=":
                parsingData = parsingData + formulariPacient[i+1]
                if i+1 < 56:
                    if formulariPacient[i+2] is not "&":
                        parsingData = parsingData + formulariPacient[i + 2]
                        if formulariPacient[i+3] is not "&":
                            parsingData = parsingData + formulariPacient[i + 3]
                            if formulariPacient[i+4] is not "&":
                                parsingData = parsingData + formulariPacient[i + 4]
                parsingData = parsingData + ","

        parsingData = parsingData[:len(parsingData)-1]
        print(parsingData)
        predict(parsingData)
        return render(request, "resposta.html")
    else:
        return render(request, "index.html")


def data(request):
    with open('./data.json') as json_file:
        data = json.load(json_file)
        return JsonResponse(data)