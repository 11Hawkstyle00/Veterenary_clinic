from entity.client import Client
from utils.Autogenerator import Autogenerator
from service.Clientservice import ClientService
from service.Petservice import PetService
from service.Appointmentservice import AppointmentService
from service.Doctorservice import DoctorService
from service.Diseaseservice import DiseaseService
Clientservice = ClientService()

def main_menu():
    print('Выберить "класс" с которым хотите работать')
    print('1:Клиенты')
    print('2:Доктора')
    print('3:Прием у врача')
    print('4:Питомцы')
    print("5:Болезни")

def client_menu():
    while True:
        print("Выберите действие для работы с сущностью:")
        print("1:Cоздание новой сущности")
        print("2:Получение сущности по ID")
        print("3:Получение всех сущностей")
        print("4:Редактирование сущности по ID")
        print("5:Удаление сущности по ID")
        command = int(input())
        if command == 0:
            exit()

        if command == 1:
            name = input('Введите имя клиента: ')
            client = Client(name)
            Clientservice.create(client)
            print('Клиент успешно создать и добавлен')


        elif command == 2:
            print('Введите ID клиента, которого хотите посмотреть')
            client_id = int(input())
            Clientservice.get_by_id(client_id).to_str()


        elif command == 3:
            for item in Clientservice.all_get_clients():
                item.to_str()

        elif command == 4:
            client_id = int(input("Введите имя клиента которого хотите отредактировать"))
            name = input("введите имя клиента для редактирования")
            client = Client(name)
            Clientservice.edit(client_id,client)
            print('Клиент успешно отредактирован')

        elif command == 5:
            print('Введите ID клиента, которого хотите посмотреть')
            client_id = int(input())
            Clientservice.del_by_id(client_id)
            print('Клиент успешно удален')
        else:
            print("Такой комнанды не существует!!!")

def doctor_menu():
    pass

def appointment_menu():
    pass

def pet_menu():
    pass

def disease_menu():
    pass

def main():
    while True:
        main_menu()
        command = int(input())
        if command == 0:
            exit()

        if command == 1:
            client_menu()

        if command == 2:
            doctor_menu()

        if command == 3:
            appointment_menu()

        if command == 4:
            pet_menu()
        else:
            print('Такой комнанды не существует!!!')
            

        
    
if __name__ == "__main__":
    main()
    