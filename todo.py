class TodoHandler:
    def __init__(self):
        self.todo_template = Element("todo-template").select("#task", from_content=True)
        self.todo_list = Element("todo-list-container")
        self.new_todo_dom = Element("new-todo")

        self.todos = []
        self.alle_todos = []
        self.offene_todos = []

    def set_length(self):
        document.getElementById("length-todo").innerText = f"{len(self.alle_todos)} Todos - {len(self.offene_todos)} offen"

    def todos_helper(self):
        self.alle_todos = [item["content"] for item in self.todos]
        self.offene_todos = [item["content"] for item in self.todos if not item["done"]]

    def get_index(self, content):
        idx = self.alle_todos.index(content)
        return idx

    def add_todo(self, *args, **kwargs):
        todo = self.new_todo_dom.element.value
        if todo in self.alle_todos or todo == "":
            return
        new_todo = {"content": todo, "done": False}
        self.todos.append(new_todo)
        self.todos_helper()

        todo_html = self.todo_template.clone(todo, to=self.todo_list)
        todo_html_content = todo_html.select("p")
        trash_button = todo_html.select(".fa-trash")
        todo_html_content.element.innerText = new_todo["content"]
        self.todo_list.element.appendChild(todo_html.element)
        self.new_todo_dom.clear()

        def check_todo(evt=None):
            idx = self.get_index(new_todo["content"])
            self.todos[idx]["done"] = not self.todos[idx]["done"]
            self.todos_helper()
            if new_todo["done"]:
                todo_html_content.element.classList.add("line-through")
            else:
                todo_html_content.element.classList.remove("line-through")
            self.set_length()

        def delete_todo(self):
            idx = self.get_index(new_todo["content"])
            self.todos.pop(idx)
            self.todos_helper()
            elem = document.getElementById(new_todo["content"])
            elem.parentNode.removeChild(elem)
            self.set_length()

        todo_html_content.element.onclick = check_todo
        trash_button.element.onclick = delete_todo
        self.set_length()

handler = TodoHandler()