class Project:
    def __init__(self, name, description, lisence, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.lisence = lisence
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        if len(dependencies) > 0:
            return f"\n- {"\n- ".join(dependencies)}"
        else:
            return ""

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLisence: {self.lisence or '-'}"
            f"\n\nAuthors: {self._stringify_dependencies(self.authors) or '-'}"
            f"\n\nDependencies: {self._stringify_dependencies(self.dependencies) or ""}"
            f"\n\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies) or ""}"
        )
