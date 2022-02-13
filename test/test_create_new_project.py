from model.project import Project
import pytest
import random
import string


def test_add_project(app):
   # old_projects = app.project.get_project_list()
    old_projects = app.soap.projects_get()
    name = app.project.random("name", 10)
    if any([p.name == name for p in old_projects]):
        name = app.project.random("name", 10)
    project = Project(name=name)
    app.project.create_project(project)
    new_projects = app.soap.projects_get()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.name_or_empty) == sorted(new_projects, key=Project.name_or_empty)
