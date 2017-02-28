from django.http import Http404, HttpResponse 
import datetime 
 
def horas_adelante(request, offset): 
    try: 
        offset = int(offset) 
    except ValueError: 
        raise Http404()  
    dt= datetime.datetime.now()+datetime.timedelta(hours=offset)  
    #assert False       
    html = "<html><body><h1>En %s hora(s), seran:</h1> <h3>%s</h3></body></html>" % (offset, dt) 
    return HttpResponse(html)  