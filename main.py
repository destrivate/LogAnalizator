import datetime
import os
from colorama import init, Fore, Style

init(autoreset=True)

session_data = {}

class Utils:
    @staticmethod
    def getTime():
        return datetime.datetime.now(datetime.UTC)

class FormatingData:
    file_name = ""
    def __init__(self, similar):
        self.similar = similar
        self.data = []
        
    def start(self):
        if not os.path.exists(self.file_name):
            print(f"\n{Fore.RED}[Ошибка] Файл не найден!")
            return
            
        print(f"\n{Fore.CYAN}--- Результаты поиска для '{self.similar}': ---")
        
        with open(self.file_name, "r", encoding="utf-8") as file:
            for line in file:
                if self.similar in line or self.similar in line.lower():
                    self.data.append(line)
                    print(f"{Fore.GREEN}{line.strip()}")
                    
        if not self.data:
            print(f"{Fore.YELLOW}Ничего не найдено.")
        print(f"{Fore.CYAN}---------------------------------------")

def show_history():
    if not session_data:
        print(f"\n{Fore.YELLOW}История сессий пуста.")
        return
        
    print(f"\n{Fore.CYAN}=== ИСТОРИЯ СЕССИЙ ===")
    for timestamp, obj in session_data.items():
        time_str = timestamp.strftime("%Y-%m-%d %H:%M:%S UTC")
        print(f"[{Fore.GREEN}{time_str}{Style.RESET_ALL}] Запрос: '{obj.similar}' | Найдено: {len(obj.data)}")
    print(f"{Fore.CYAN}======================")

def main():
    print(f"{Fore.BLUE}Название файла: ")
    FormatingData.file_name = input()
    while True:
        print(f"\n{Fore.MAGENTA}=== ГЛАВНОЕ МЕНЮ ===")
        print(f"{Fore.BLUE}1.{Style.RESET_ALL} Поиск в логах")
        print(f"{Fore.BLUE}2.{Style.RESET_ALL} История сессий")
        print(f"{Fore.BLUE}3.{Style.RESET_ALL} Выход")
        
        choice = input(f"\n{Fore.YELLOW}Выберите действие (1-3): {Style.RESET_ALL}").strip()
        
        if choice == '1':
            keyword = input(f"{Fore.YELLOW}Введите ключевое слово: {Style.RESET_ALL}").strip()
            if keyword:
                s = FormatingData(keyword)
                s.start()
                session_data[Utils.getTime()] = s
            else:
                print(f"{Fore.RED}Ключевое слово не может быть пустым!")
                
        elif choice == '2':
            show_history()  
            
        elif choice == '3':
            print(f"\n{Fore.GREEN}Программа завершена.")
            break
        else:
            print(f"\n{Fore.RED}[Ошибка] Неверный пункт меню.")

if __name__ == '__main__':
    main()
