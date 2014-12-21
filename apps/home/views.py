#-*-coding:utf8-*-
from django.views.generic import TemplateView
from apps.internal.models import Doctor, Hospital, HospitalType
from apps.polls.models import Question

class HomeView(TemplateView):
    """
    Returns homepage
    """

    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # передаємо у context об’єкти Doctor, HospitalType, Hospital, Question
        context['doctors'] = Doctor.objects.all().order_by('-recommend_yes')[:4]
        context['hospital_types'] = HospitalType.objects.all()
        context['hospitals'] = Hospital.objects.all()
        context['question'] = Question.objects.get(pk=1)
        # перетворюємо id питання у рядкову змінну, щоб далі її можна було використати
        # для перевірки на входження в self.request.COOKIES
        cookie_name = str(context['question'].id)
        # перевіряємо чи існує COOKEI з ім’ям, яке дорівнює id питання і, взалежності від результату
        # перевірки, вибираємо потрібну форму, яку передаємо у шаблон
        # Якщо COOKIE існує --- передаємо форму з результатами, у іншому випадку --- передаємо
        # форму для відповіді.
        if cookie_name in self.request.COOKIES:
            context['question_pattern'] = 'polls/results.html'
        else:
            context['question_pattern'] = 'polls/question.html'
        return context
