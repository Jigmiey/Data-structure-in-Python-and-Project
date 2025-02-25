from services.task_service import task_service
from services.user_service import user_service

def main():
    task_service1 = task_service()
    task_service1.create_task(1,"teach data structure basic", "teach from scratch")
    task_service1.create_task(2, "teach advance data structure","teach from scratch")
    task_service1.create_task(3,"Do a project","teach from scratch")
    task_service1.create_task(4,"take order from Ak official ", "fix the error")
    
    he_he = True
    while he_he:
        hello = task_service1.complete_task()
        print(hello)
        if hello == None:
            he_he = False

if __name__ == "__main__":
    main()