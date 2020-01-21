![Language](https://img.shields.io/badge/language-Python-blue)
<h1 align="center">Rune Web Project</h1>
<h2>Legends of Runeterra Analysis Site</h2>

<h3>목차</h3>

1. 이 프로젝트의 기능은 무엇인가?
2. 이 프로젝트에 사용되는 것들은 무엇인가?
3. Django 와 프로젝트 연동
4. 간단한 화면 명세서
5. 참조

---

<h4>이 프로젝트의 기능은 무엇인가?</h4>

* 카드 정보(효과) 기능
* 덱 조합 기능 
  * 문자열 코드를 이용하여 자신이 만든 덱 조합을 공유 하고 타인의 코드를 읽을 수 있음
  * 필터를 이용하여 자신이 원하는 카드를 빠르게 검색
  * 조합된 덱의 평균 코스트 확인 및 평균 코스트를 이용하여 대략적인 승률을 짐작할 수 있다.
  * 조합된 덱의 시너지 확인 및 시너지를 이용하여 대략적인 승률을 짐작할 수 있다.
* 시너지별 승률 을 보여주는 기능 
* 코스트 별 승률을 보여주는 기능
* 유저 정보 검색 기능
* 커뮤니티 기능

---

<h4>이 프로젝트에 사용되는 것들은 무엇인가?</h4>

* Python
* DJango
* MySQL
* HTML
* CSS
* JavaScript

---

<h2>Django 와 MySQL 그리고 프로젝트 연동</h2>

<h4>그 전에...</h4>

```text
지금부터 MySQL 을 이미 설치했다고 가정하고 연동 및 설명을 할 것이다.  
MySQL 을 설치하지 못하였다면 구글링을 통해 설치하고 id, password 를 설정하고 오자.  
```

* 프로젝트에 쓰일 MySQL DATABASE 하나를 만들자. (DATABASE 이름은 자유롭게 설정하자)

* MySQL 과 Django 를 연동한다, 다음의 커맨드라인을 입력한다.

```text
$ pip install mysqlclient
```

* 이 GitHub Repository 에 있는 파일을 다운받자.

* RuneWeb/settings.py 에서 자신의 MySQL 설정에 맞게  
'NAME': '프로젝트에 사용될 데이터베이스 이름'  
'USER': '자신의 MySQL id'  
'PASSWORD': '자신의 MySQL password'  
를 설정해야 한다.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your database name',
        'USER': 'your sql user name',
        'PASSWORD': 'your user password',
        'HOST': '127.0.0.1',
        'POST': '3306',
        'OPTIONS': {
            'init_command':'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}
```

* 다운받은 프로젝트 디렉토리로 이동하여(manag.py 가 있는 디렉토리), 다음의 커맨드라인을 입력한다.

```text
$ python manage.py migrate
```

* 문제없이 잘했다면 자신의 DATABASE 에 다음과 같은 10개의 TABLE 들이 생성되었을 것이다.

```text
auth_group                     django_admin_log
auth_group_permissions         django_content_type
auth_permission                django_migrations
auth_user                      django_session
auth_user_groups
auth_user_user_permissions
```

* 다시한번 manage.py 가 있는 디렉토리에서 다음의 커맨드 라인을 입력하자

```text
$ python manage.py runserver
```

* 그 후 브라우저에 http://127.0.0.1:8000/rune_web/ 으로 접속해 보자.
* 현재까지 진행되고 있는 프로젝트 화면이 나오면 성공적으로 연동이 된것이다.

---

<h4>Django 를 처음 접한다면? </h4>

<a href="https://github.com/truejin/Django-EASY-Manual">Django-EASY-Manual</a>
<br>
<a href="https://docs.djangoproject.com">django official site</a> 

---

<h4>간단한 화면 명세서</h4>
이 프로젝트에서 현재까지 계획된 화면 구조는 다음과 같다.   
<br>

* 메인 화면
* 덱 정보 화면
* 덱 빌딩 화면
* 덱 트렌드 화면
* 커뮤니티 화면
* 로그인 화면

<h4>참조</h4>

자세한 화면 계획서는 메일에 있는 공유 링크를 확인하자  