from django.shortcuts import render
import pandas as pd
url= 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%ED%99%98%EC%9C%A8%EC%A1%B0%ED%9A%8C'
tables=pd.read_html(url)
df=tables[1]
df.columns
df=df[['매매기준율']]
exchange_list=df.values.tolist()
exchange_list=sum(exchange_list,[])
def home (request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html',)

def result(request):
    nation = list(['USD','JPY','EUR','CNY','GBP','AUD','CAD','NZD'])
    for i in range(8):
        if nation[i] in request.POST :
            # 만약 넘어갈게 한두개가 아니면 그때는 어떻게 처리할까? 이떄는 name 밖에 없었지만
            name = nation[i]
            korea = request.POST['korea']
            tocountry = int(korea)
            tocountry = round(tocountry / exchange_list[i],2)
    return render(request,'result.html',{'country':tocountry,'name':name,'korea':korea})