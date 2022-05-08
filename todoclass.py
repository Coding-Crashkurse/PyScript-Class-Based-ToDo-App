class TodoHandler:
    def __init__(self):
        self.todos = []
        self.alle_todos = []
        self.offene_todos = []

    def todos_helper(self):
        self.alle_todos = [item["content"] for item in self.todos]
        self.offene_todos = [item["content"] for item in self.todos if not item["done"]]

    def add_todo(self, todo):
        if todo in self.alle_todos or todo == "":
            return
        new_todo = {"content": todo, "done": False}
        self.todos.append(new_todo)
        self.todos_helper()

    def get_index(self, content):
        idx = self.alle_todos.index(content)
        return idx

    def delete_todo(self, content):
        idx = self.get_index(content)
        self.todos.pop(idx)
        self.todos_helper()

    def check_todo(self, content):
        idx = self.get_index(content)
        self.todos[idx]["done"] = not self.todos[idx]["done"]
        self.todos_helper()