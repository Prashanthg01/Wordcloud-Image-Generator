from django.shortcuts import render, HttpResponse
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
import urllib
import base64
import os


def home(request):
    return render(request, 'home.html')


def generate_wordcloud(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        wordcloud = WordCloud().generate(text)

        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')

        image = io.BytesIO()
        plt.savefig(image, format='png')
        image.seek(0)
        string = base64.b64encode(image.read()).decode('utf-8')

        plt.close()

        return render(request, 'home.html', {'wordcloud': string})


def download_wordcloud(request):
    if request.method == 'GET':
        string = request.GET.get('wordcloud')
        image = base64.b64decode(string)
        
        filename = 'wordcloud.png'
        filepath = os.path.join('/path/to/temp/folder', filename)  # Replace '/path/to/temp/folder' with the actual path to your temporary folder
        
        with open(filepath, 'wb') as f:
            f.write(image)
        
        with open(filepath, 'rb') as f:
            response = HttpResponse(f.read(), content_type='image/png')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
        
        os.remove(filepath)  # Delete the temporary image file
        
        return response

    return HttpResponse(status=400)  # Return a default response if the request method is not GET

