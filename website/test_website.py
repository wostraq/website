from . import create_app
import pytest

@pytest.fixture(scope="module")
def client():
  app=create_app()
  with app.test_client() as c:
    yield c


def test_home(client):
  assert '200' in client.get('/').status 
  
def test_about_membership(client):
  assert '200' in client.get('/about/membership').status

def test_about_local(client):
  assert '200' in client.get('/about/local').status
  
def test_about_committee(client):
  assert '200' in client.get('/about/committee').status
  

def test_projects_previous(client):
  assert '200' in client.get('/projects/previous').status
  
def test_projects_propose(client):
  assert '200' in client.get('/projects/propose').status  

