import pytest

from students.models import Course


@pytest.mark.django_db
def test_one_course(client, course_factory):
    courses = course_factory(_quantity=1)

    res = client.get(f'/api/v1/courses/{courses[0].id}/')

    data = res.json()

    assert res.status_code == 200
    assert data['name'] == courses[0].name


@pytest.mark.django_db
def test_courses(client, course_factory):
    courses = course_factory(_quantity=5)

    res = client.get('/api/v1/courses/')

    data = res.json()

    assert res.status_code == 200
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name


@pytest.mark.django_db
def test_id_filter(client, course_factory):
    courses = course_factory(_quantity=1)

    res = client.get('/api/v1/courses/', {'id': courses[0].id})

    data = res.json()

    assert res.status_code == 200
    assert data[0]['id'] == courses[0].pk


@pytest.mark.django_db
def test_name_filter(client, course_factory):
    courses = course_factory(_quantity=1)

    res = client.get('/api/v1/courses/', {'name': courses[0].name})

    data = res.json()

    assert res.status_code == 200
    assert data[0]['name'] == courses[0].name


@pytest.mark.django_db
def test_create_course(client):
    cnt = Course.objects.count()

    res = client.post('/api/v1/courses/', {'name': 'Python-разработчик'})

    assert res.status_code == 201
    assert Course.objects.count() == cnt + 1


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory(_quantity=1)

    res = client.patch(f'/api/v1/courses/{course[0].id}/', {'name': 'Python-разработчик'})

    data = res.json()

    assert res.status_code == 200
    data_db = Course.objects.get(pk=course[0].id)
    assert data_db.name == data['name']


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory(_quantity=1)
    cnt = Course.objects.count()

    res = client.delete(f'/api/v1/courses/{course[0].id}/')

    assert res.status_code == 204
    assert Course.objects.count() == cnt-1
