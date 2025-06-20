import os
import subprocess
import sys


APPS = {
    "1": {"file": "1num_guesser.py", "name": "Угадай число"},
    "2": {"file": "2magic_ball.py", "name": "Магический шар"},
    "3": {"file": "3pass_gen.py", "name": "Генератор паролей"},
    "4": {"file": "4sh_cesar.py", "name": "Шифр Цезаря"},
    "5": {"file": "5num_sys_calc.py", "name": "Калькулятор систем счисления"},
    "6": {"file": "6word_guesser.py", "name": "Угадай слово"},
    "7": {"file": "7tictac.py", "name": "Крестики-нолики"}
}

def show_menu():
    """Главное меню"""
    print("===== Доступные приложения =====")
    for key, app in APPS.items():
        print(f"{key}. {app['name']}")
    print("0. Выйти")
    print("=" * 31)

def run_app(script_name):
    """Запуск выбранного приложения"""
    script_path = os.path.join("projects", script_name)
    if os.path.exists(script_path):
        print(f"\nЗапуск: {APPS[choice]['name']}...")
        subprocess.run([sys.executable, script_path])
    else:
        print(f"Ошибка: Файл {script_path} не найден!")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Ваш выбор: ").strip()
        
        if choice == "0":
            print("\nДо свидания!")
            break
            
        if choice in APPS:
            run_app(APPS[choice]["file"])
        else:
            print("Неверный ввод! Попробуйте снова.")