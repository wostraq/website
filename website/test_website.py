from . import create_app
import pytest

@pytest.fixture(scope="module")
def client():
  app=create_app()
  with app.test_client() as c:
    yield c


def test_home(client):
  client.get('/')
  
def test_about_membership(client):
  client.get('/about/membership')

def test_about_local(client):
  client.get('/about/local')
  
def test_about_committee(client):
  client.get('/about/committee')
  

def test_projects_previous(client):
  client.get('/projects/previous')
  
def test_projects_propose(client):
  client.get('/projects/propose')
  

