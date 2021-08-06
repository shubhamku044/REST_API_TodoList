# https://www.instagram.com/thelegitprogrammer/
from flask import Flask
from werkzeug.datastructures import RequestCacheControl
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

todos = {
    1: {
        "Todo": "Learn to create api using Flask",
        "Description": "Creating a todo list api using flask"
    },
    2: {
        "Todo": "Learn to create api using Django",
        "Description": "Creating a todo list api using Django"
    },
    3: {
        "Todo": "Learn to create api using express",
        "Description": "Creating a todo list api using express"
    }
}

todo_post_args = reqparse.RequestParser()
todo_post_args.add_argument(
    "Todo", type=str, help="Todo is required", required=True
)
todo_post_args.add_argument(
    "Description", type=str, help="Description is required", required=True
)

todo_put_args = reqparse.RequestParser()
todo_put_args.add_argument(
    "Todo", type=str
)
todo_put_args.add_argument(
    "Description", type=str
)

# I haven't integrated this api into database but if you want me to do that then DM on insta.

class ToDo(Resource):
    def get(self, todo_id):
        return todos[todo_id]

    def post(self, todo_id):
        args = todo_post_args.parse_args()

        if todo_id in todos:
            abort(409, "Task id already exists")
        
        todos[todo_id] = {
            "Todo": args["Todo"],
            "Description": args["Description"]
        }

        return todos[todo_id]
    
    def put(self, todo_id):
        args = todo_put_args.parse_args()
        
        if todo_id not in todos:
            abort(404, message="Todo Item not found, Cannot update")
        
        if args["Todo"]:
            todos[todo_id]['Todo'] = args["Todo"]

        if args["Description"]:
            todos[todo_id]['Description'] = args["Description"]


    def delete(self, todo_id):
        del todos[todo_id]
        return todos


class ToDoList(Resource):
    def get(self):
        return todos

api.add_resource(ToDo, '/todo/<int:todo_id>')
api.add_resource(ToDoList, '/todo')


if __name__ == '__main__':
    app.run(debug=True)