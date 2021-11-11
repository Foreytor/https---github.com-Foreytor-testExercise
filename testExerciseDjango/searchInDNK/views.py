from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import SearcherDNKSerializer
from .forms import SearcherDNKForm
import re


DNK = '''TTTTTCCCAAAAGCGTAGCTCGTAGATTAGCGCCTTACGATCGTCGATCGATCGGCGCGCGCGCTAGACTGCTATATATAGCGCATGCTCGCTAGCGCGCGCTAGCAGCGATGCTCTAGCTAGCTAGCTATCGATCGATCGCGCTAGCTACGTCGATCGATCGTACGATCGATCGATCGATTATATAGCATCGCGCTGATCGTCGTA'''

# Create your views here.
class Index(View):
    #context_object_name = 'header_home'
    template_name = 'searchInDNK/index.html'
#    queryset = HeaderHome.objects.all()[0:1]
    def get(self, request, *args, **kwargs):
        form = SearcherDNKForm()
        return render(request, self.template_name, {'form': form, 'DNK': DNK,})

    def post(self, request, *args, **kwargs):
        form = SearcherDNKForm(request.POST)
        result = ''
        if form.is_valid():
            codon = str(form.cleaned_data.get('codon')).upper()
            n = 3
            DNKList = list([DNK.upper()[i:i+n] for i in range(0, len(DNK), n)])
            if codon in DNKList:
                result = 'Найдено'
            else:
                result = 'Не найдено'

        return render(request, self.template_name, {'form': form, 'result': result,'DNK': DNK,})


class IndexAPIView(APIView):
    '''/API/?codon=ttc'''
    def get(self, request):
        codon = str(request.GET.get('codon', False)).upper()
        n = 3
        DNKList = list([DNK.upper()[i:i+n] for i in range(0, len(DNK), n)])

        tpl = '[ACGT]{3}'
        print(re.match(tpl, codon))
        if re.match(tpl, codon) is not None and codon:
            if codon.upper() in DNKList:
                serializer = SearcherDNKSerializer({'codon':'Найдено'})
            else:
                serializer = SearcherDNKSerializer({'codon':'Не найдено'})
        else:
            serializer = SearcherDNKSerializer({'codon':'Неверный формат кодона, кодон может содержать только 3 символа (A,C,G,T)'})
        return Response(serializer.data)
