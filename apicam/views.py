from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import cv2
import numpy as np


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        try:
            # Obtén la imagen del cuerpo de la solicitud
            image_data = request.body
            nparr = np.frombuffer(image_data, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            # Aquí puedes realizar cualquier procesamiento adicional con la imagen recibida
            # Por ejemplo, guardarla en el disco, procesarla, mostrarla, etc.

            # Devuelve una respuesta al cliente
            return HttpResponse('OK', status=200)
        except Exception as e:
            print(f"Error processing image: {e}")
            return HttpResponse('Error', status=500)
    else:
        return HttpResponse('Method not allowed', status=405)
