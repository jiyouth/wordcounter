from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'wordcount/home.html')


def about(request):
    return render(request, 'wordcount/about.html')


def count(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1

        else:
            # add to the dictionary
            word_dictionary[word] = 1    

    return render(request, 'wordcount/count.html', {'fulltext' : full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()})

    #공백포함    
def blank(request):    
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}
    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
            # add to dictionary
            word_dictionary[word]=1
    total = len(words)*2 -1

    return render(request, 'result.html', {'full': text, 'total' : total, 'dictionary' : word_dictionary.items()})

