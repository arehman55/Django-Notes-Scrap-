# Part 3 - Extracted Scripts

### Script 1
**Summary:** Now let’s add a few more views to polls/views.py. These views are slightly different, because they take an argument:

```python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

---

### Script 2
**Summary:** Now let’s add a few more views to polls/views.py. These views are slightly different, because they take an argument:

```python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

---

### Script 3
**Summary:** Wire these new views into the polls.urls module by adding the following path() calls:

```python
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

---

### Script 4
**Summary:** Wire these new views into the polls.urls module by adding the following path() calls:

```python
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

---

### Script 5
**Summary:** When somebody requests a page from your website – say, “/polls/34/”, Django will load the mysite.urls Python module because it’s pointed to by the ROO...

```python
detail(request=<HttpRequest object>, question_id=34)
```

---

### Script 6
**Summary:** When somebody requests a page from your website – say, “/polls/34/”, Django will load the mysite.urls Python module because it’s pointed to by the ROO...

```python
detail(request=<HttpRequest object>, question_id=34)
```

---

### Script 7
**Summary:** Because it’s convenient, let’s use Django’s own database API, which we covered in Tutorial 2. Here’s one stab at a new index() view, which displays th...

```python
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# Leave the rest of the views (detail, results, vote) unchanged
```

---

### Script 8
**Summary:** Because it’s convenient, let’s use Django’s own database API, which we covered in Tutorial 2. Here’s one stab at a new index() view, which displays th...

```python
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# Leave the rest of the views (detail, results, vote) unchanged
```

---

### Script 9
**Summary:** Put the following code in that template:

```python
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

---

### Script 10
**Summary:** Put the following code in that template:

```python
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

---

### Script 11
**Summary:** Now let’s update our index view in polls/views.py to use the template:

```python
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))
```

---

### Script 12
**Summary:** Now let’s update our index view in polls/views.py to use the template:

```python
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))
```

---

### Script 13
**Summary:** It’s a very common idiom to load a template, fill a context and return an HttpResponse object with the result of the rendered template. Django provide...

```python
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
```

---

### Script 14
**Summary:** It’s a very common idiom to load a template, fill a context and return an HttpResponse object with the result of the rendered template. Django provide...

```python
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
```

---

### Script 15
**Summary:** Now, let’s tackle the question detail view – the page that displays the question text for a given poll. Here’s the view:

```python
from django.http import Http404
from django.shortcuts import render

from .models import Question


# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
```

---

### Script 16
**Summary:** Now, let’s tackle the question detail view – the page that displays the question text for a given poll. Here’s the view:

```python
from django.http import Http404
from django.shortcuts import render

from .models import Question


# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
```

---

### Script 17
**Summary:** We’ll discuss what you could put in that polls/detail.html template a bit later, but if you’d like to quickly get the above example working, a file co...

```python
{{ question }}
```

---

### Script 18
**Summary:** We’ll discuss what you could put in that polls/detail.html template a bit later, but if you’d like to quickly get the above example working, a file co...

```python
{{ question }}
```

---

### Script 19
**Summary:** It’s a very common idiom to use get() and raise Http404 if the object doesn’t exist. Django provides a shortcut. Here’s the detail() view, rewritten:

```python
from django.shortcuts import get_object_or_404, render

from .models import Question


# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
```

---

### Script 20
**Summary:** It’s a very common idiom to use get() and raise Http404 if the object doesn’t exist. Django provides a shortcut. Here’s the detail() view, rewritten:

```python
from django.shortcuts import get_object_or_404, render

from .models import Question


# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
```

---

### Script 21
**Summary:** Back to the detail() view for our poll application. Given the context variable question, here’s what the polls/detail.html template might look like:

```python
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

---

### Script 22
**Summary:** Back to the detail() view for our poll application. Given the context variable question, here’s what the polls/detail.html template might look like:

```python
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

---

### Script 23
**Summary:** Remember, when we wrote the link to a question in the polls/index.html template, the link was partially hardcoded like this:

```python
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

---

### Script 24
**Summary:** Remember, when we wrote the link to a question in the polls/index.html template, the link was partially hardcoded like this:

```python
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

---

### Script 25
**Summary:** The problem with this hardcoded, tightly-coupled approach is that it becomes challenging to change URLs on projects with a lot of templates. However, ...

```python
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

---

### Script 26
**Summary:** The problem with this hardcoded, tightly-coupled approach is that it becomes challenging to change URLs on projects with a lot of templates. However, ...

```python
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

---

### Script 27
**Summary:** The way this works is by looking up the URL definition as specified in the polls.urls module. You can see exactly where the URL name of ‘detail’ is de...

```python
...
# the 'name' value as called by the {% url %} template tag
path("<int:question_id>/", views.detail, name="detail"),
...
```

---

### Script 28
**Summary:** The way this works is by looking up the URL definition as specified in the polls.urls module. You can see exactly where the URL name of ‘detail’ is de...

```python
...
# the 'name' value as called by the {% url %} template tag
path("<int:question_id>/", views.detail, name="detail"),
...
```

---

### Script 29
**Summary:** If you want to change the URL of the polls detail view to something else, perhaps to something like polls/specifics/12/ instead of doing it in the tem...

```python
...
# added the word 'specifics'
path("specifics/<int:question_id>/", views.detail, name="detail"),
...
```

---

### Script 30
**Summary:** If you want to change the URL of the polls detail view to something else, perhaps to something like polls/specifics/12/ instead of doing it in the tem...

```python
...
# added the word 'specifics'
path("specifics/<int:question_id>/", views.detail, name="detail"),
...
```

---

### Script 31
**Summary:** The answer is to add namespaces to your URLconf. In the polls/urls.py file, go ahead and add an app_name to set the application namespace:

```python
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

---

### Script 32
**Summary:** The answer is to add namespaces to your URLconf. In the polls/urls.py file, go ahead and add an app_name to set the application namespace:

```python
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

---

### Script 33
**Summary:** Now change your polls/index.html template from:

```python
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

---

### Script 34
**Summary:** Now change your polls/index.html template from:

```python
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

---

### Script 35
**Summary:** to point at the namespaced detail view:

```python
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

---

### Script 36
**Summary:** to point at the namespaced detail view:

```python
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

---

