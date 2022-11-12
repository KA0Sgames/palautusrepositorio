from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        parsed_toml = toml.loads(content)
        #print(parsed_toml)

        dependencies = []
        for dependency in parsed_toml["tool"]["poetry"]["dependencies"].keys():
            dependencies.append(dependency)

        devdeps = []
        for dev_dependency in parsed_toml["tool"]["poetry"]["dev-dependencies"].keys():
            devdeps.append(dev_dependency)

        return Project(parsed_toml["tool"]["poetry"]["name"],
            parsed_toml["tool"]["poetry"]["description"],
            dependencies,
            devdeps)
