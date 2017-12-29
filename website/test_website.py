from . import create_app
import pytest

@pytest.fixture(scope="module")
def client():
  app=create_app()
  with app.test_client() as c:
    yield c


def test_home(client):
  assert client.get('/')[1] == 200
  
def test_about_membership(client):
  assert client.get('/about/membership')[1] == 200

def test_about_local(client):
  assert client.get('/about/local')[1] == 200
  
def test_about_committee(client):
  assert client.get('/about/committee')[1] == 200
  

def test_projects_previous(client):
  assert client.get('/projects/previous')[1] == 200
  
def test_projects_propose(client):
  assert client.get('/projects/propose')[1] == 200
  

