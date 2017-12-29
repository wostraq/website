from . import create_app
import pytest

@pytest.fixture(scope="module")
def client():
  app=create_app()
  with app.test_client() as c:
    yield c


def test_home(client):
  assert client.get('/').status == 200
  
def test_about_membership(client):
  assert client.get('/about/membership').status == 200

def test_about_local(client):
  assert client.get('/about/local').status == 200
  
def test_about_committee(client):
  assert client.get('/about/committee').status == 200
  

def test_projects_previous(client):
  assert client.get('/projects/previous').status == 200
  
def test_projects_propose(client):
  assert client.get('/projects/propose').status == 200
  

