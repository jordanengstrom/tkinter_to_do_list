class Task:
    def __init__(self, title, details, due_date, priority):
        self.title = title
        self.details = details
        self.due_date = due_date
        self.priority = priority

    @property
    def title(self):
        return self.title()

    @title.setter
    def title(self, title):
        self.title = title

    def __str__(self):
        return self.title + ": " + self.details

    def __repr__(self):
        return self.title + ": " + self.details