from model.project import Project
import random


def test_del_project(app):
    if app.project.count_project() == 0:
        name = app.project.random("name", 10)
        project = Project(name=name)
        app.project.create_project(project)
    old_projects = app.soap.projects_get()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    new_projects = app.soap.projects_get()
    assert len(old_projects) - 1 == app.project.count_project()
    old_projects.remove(project)
    assert old_projects == new_projects
    assert sorted(old_projects, key=Project.name_or_empty) == sorted(new_projects, key=Project.name_or_empty)
