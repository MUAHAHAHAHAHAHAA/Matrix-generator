import generator
import file_handler as fh
import os

def print_m(A):
    for row in A:
        res = []
        for entry in row:
            res.append(str(int(entry)))
        txt = " ".join(res)
        print(txt)
    print("")

def save(p, A, A_inv, B, M):
    tasks = sorted(get_ids())
    id = 0
    for vel in tasks:
        if id == vel:
            id += 1
    tasks.append(id)
    set_ids(tasks)
    data = {
        "char": p,
        "A": A.tolist(),
        "A_inv": A_inv.tolist(),
        "B": B.tolist(),
        "M": M.tolist()
    }
    fh.set("data/" + str(id), data)
    return id

def get_task(id):
    return fh.get("data/" + id)

def del_task(id):
    os.remove("data/" + id)
    id = int(id)
    tasks = get_ids()
    tasks.remove(id)
    set_ids(tasks)

def set_ids(tasks):
    fh.set("data/info.json", {"tasks": tasks})

def get_ids():
    info = fh.get("data/info.json")
    return info["tasks"]

if __name__ == "__main__":
    while True:
        txt = input(">> ")
        data = txt.split(" ")

        if data[0] == "end":
            break
        elif data[0] == "generate":
            try:
                p = int(data[1])
                if not p in [2, 3, 5, 7]:
                    print("Bad input")
                    continue
                A, A_inv, B, M = generator.generate(p, int(data[2]))
                id = save(p, A, A_inv, B, M)
                print("Saved in: " + str(id))
            except:
                print("Invalid input")
        elif data[0] == "sol":
            try:
                tsk = get_task(data[1])
                print("characteristic: " + str(tsk["char"]))
                print("A:")
                print_m(tsk["A"])
                print("A^-1:")
                print_m(tsk["A_inv"])
                print("B = A^-1 * M * A:")
                print_m(tsk["B"])
                print("M:")
                print_m(tsk["M"])
            except:
                print("Task not found")
        elif data[0] == "get":
            try:
                tsk = get_task(data[1])
                print("characteristic: " + str(tsk["char"]))
                print("M:")
                print_m(tsk["M"])
            except:
                print("Task not found")
        elif data[0] == "ids":
            print(get_ids())
        elif data[0] == "del":
            try:
                del_task(data[1])
            except:
                print("Task not found")
        else:
            print("Command does not exist")