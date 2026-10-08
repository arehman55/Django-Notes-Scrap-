# Part 1 - Extracted Scripts

### Script 1
**Summary:** We’ll assume you have Django installed already. You can tell Django is installed and which version by running the following command in a shell prompt ...

```python
$ python -m django --version
```

---

### Script 2
**Summary:** We’ll assume you have Django installed already. You can tell Django is installed and which version by running the following command in a shell prompt ...

```python
$ python -m django --version
```

---

### Script 3
**Summary:** From the command line, cd into a directory where you’d like to store your code and run the following command to bootstrap a new Django project:

```python
$ django-admin startproject mysite djangotutorial
```

---

### Script 4
**Summary:** From the command line, cd into a directory where you’d like to store your code and run the following command to bootstrap a new Django project:

```python
$ django-admin startproject mysite djangotutorial
```

---

### Script 5
**Summary:** Let’s look at what startproject created:

```python
djangotutorial/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

---

### Script 6
**Summary:** Let’s look at what startproject created:

```python
djangotutorial/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

---

### Script 7
**Summary:** Let’s verify your Django project works. Change into the djangotutorial directory, if you haven’t already, and run the following commands:

```python
$ python manage.py runserver
```

---

### Script 8
**Summary:** Let’s verify your Django project works. Change into the djangotutorial directory, if you haven’t already, and run the following commands:

```python
$ python manage.py runserver
```

---

### Script 9
**Summary:** To create your app, make sure you’re in the same directory as manage.py and type this command:

```python
$ python manage.py startapp polls
```

---

### Script 10
**Summary:** To create your app, make sure you’re in the same directory as manage.py and type this command:

```python
$ python manage.py startapp polls
```

---

### Script 11
**Summary:** That’ll create a directory polls, which is laid out like this:

```python
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

---

### Script 12
**Summary:** That’ll create a directory polls, which is laid out like this:

```python
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

---

### Script 13
**Summary:** Let’s write the first view. Open the file polls/views.py and put the following Python code in it:

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

---

### Script 14
**Summary:** Let’s write the first view. Open the file polls/views.py and put the following Python code in it:

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

---

### Script 15
**Summary:** To define a URLconf for the polls app, create a file polls/urls.py with the following content:

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

---

### Script 16
**Summary:** To define a URLconf for the polls app, create a file polls/urls.py with the following content:

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

---

### Script 17
**Summary:** Your app directory should now look like:

```python
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```

---

### Script 18
**Summary:** Your app directory should now look like:

```python
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```

---

### Script 19
**Summary:** The next step is to configure the root URLconf in the mysite project to include the URLconf defined in polls.urls. To do this, add an import for djang...

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

---

### Script 20
**Summary:** The next step is to configure the root URLconf in the mysite project to include the URLconf defined in polls.urls. To do this, add an import for djang...

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

---

### Script 21
**Summary:** You have now wired an index view into the URLconf. Verify it’s working with the following command:

```python
$ python manage.py runserver
```

---

### Script 22
**Summary:** You have now wired an index view into the URLconf. Verify it’s working with the following command:

```python
$ python manage.py runserver
```

---

