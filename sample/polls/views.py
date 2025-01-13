from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .models import Choice, Question
from django.db.models import F
from django.views import generic
from .service.spread_sheat import get_spread_sheet_data

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by("-pub_data")[:5]

# 入力フォーム /polls/{question_id}    
class DetailView(generic.DeleteView):
    model = Question
    template_name = "polls/detail.html"
    
    # detail.htmlに送る変数を設定
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # SpreadSheetから取得した値をsheet_valueとしてdetail.htmlに送る
        context["sheet_value"] = self.get_sheet_value('sheet')
        
        return context
    
    # sheetの値を取得する
    def get_sheet_value(self, sheet_name):
        return get_spread_sheet_data(sheet_name)
    
class ResultView(generic.DeleteView):
    model = Question
    template_name = "polls/result.html"
    