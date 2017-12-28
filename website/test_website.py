from . import content,create_app
import pytest

@pytest.fixture(scope="module",autouse=True)
def appcontext():
  app=create_app()
  with app.test_client() as c:
    yield

def test_home():
  content.home()
  
def test_about_membership():
  content.about_membership()

def test_about_local():
  content.about_local()

def test_about_committee():
  content.about_committe()
  
def test_projects_previous():
  content.projects_previous()


def test_projects_propose():
  content.projects_propose()

