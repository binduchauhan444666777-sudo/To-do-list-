f = open("todolist.txt","w")
f.write("---TO DO LIST--- \n")
tasks = [
    "Revising python concepts",
    "Yoga",
    "Skincare",
    "Reading a book",
    "Diary entry"

]
with open("todolist.txt","a") as f:
    for i, tasks in enumerate(tasks, start=1):
        f.write(f"<{i}> {tasks}\n")

