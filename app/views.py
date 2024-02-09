from django.shortcuts import render
import wikipedia
wikipedia.set_lang("uz")
def javob_ber(text_file, savol):
    with open(text_file, 'r') as file:
        lines = file.readlines()
        javob = ""
        javob_topildi = False
        for line in lines:
            parts = line.strip().split('-')
            if parts[0].strip() == savol:
                javob += parts[1].strip() + "\n"
                javob_topildi = True
            elif javob_topildi:
                break
        if javob_topildi:
            return javob.strip()
        else:
            try:
                result = wikipedia.summary(savol)
                return(result)
            except:
                return("Men SGS tomonidam yaratilgan AI man,Hozirgi bilimim bu savolga javob berish uchun yetmaydi.Lekin albatta men takomillashaman va barcha savollaringizga javob berolaman👍!")

def index(request):
    if request.method == 'POST':
        savol = request.POST['savol'].lower().replace(" ", "")
        text_file = "app/text.txt"
        javob = javob_ber(text_file, savol)
        return render(request, 'index.html', {'javob': javob})
    return render(request, 'index.html')
