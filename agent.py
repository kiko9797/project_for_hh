"""
🎯 AI АГЕНТ ДЛЯ СОБЕСЕДОВАНИЯ
Простая демонстрация управления браузером через код
"""

from playwright.sync_api import sync_playwright
import time
import os

print("=" * 60)
print("🤖 ЗАПУСК AI-АГЕНТА ДЛЯ АВТОМАТИЗАЦИИ БРАУЗЕРА")
print("=" * 60)

def simple_agent_demo():
    """Простая демонстрация возможностей агента"""
    
    print("\n🔧 Инициализация браузера...")
    
    # 1. Запускаем Playwright
    with sync_playwright() as p:
        # Запускаем Chrome (headless=False - видим окно)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        print("✅ Браузер готов к работе\n")
        
        # ========== ДЕМОНСТРАЦИЯ №1: Поиск в Google ==========
        print("🎯 ДЕМО 1: Автоматический поиск в Google")
        print("-" * 40)
        
        page.goto("https://google.com")
        time.sleep(2)
        
        # Ищем поисковую строку и вводим текст
        page.fill("textarea[name='q']", "AI агент на Python Playwright")
        page.press("textarea[name='q']", "Enter")
        
        time.sleep(3)
        page.screenshot(path="demo1_google_search.png")
        print("✅ Поиск выполнен! Скриншот: demo1_google_search.png")
        
        # ========== ДЕМОНСТРАЦИЯ №2: Работа с YouTube ==========
        print("\n🎯 ДЕМО 2: Поиск на YouTube")
        print("-" * 40)
        
        page.goto("https://youtube.com")
        time.sleep(2)
        
        # Вводим в поиск YouTube
        page.fill("input#search", "Python automation tutorial")
        page.press("input#search", "Enter")
        
        time.sleep(3)
        page.screenshot(path="demo2_youtube_search.png")
        print("✅ YouTube поиск выполнен! Скриншот: demo2_youtube_search.png")
        
        # ========== ДЕМОНСТРАЦИЯ №3: Скроллинг и навигация ==========
        print("\n🎯 ДЕМО 3: Навигация по странице")
        print("-" * 40)
        
        page.goto("https://github.com")
        time.sleep(2)
        
        # Скроллим вниз
        page.evaluate("window.scrollTo(0, 1000)")
        time.sleep(1)
        
        # Кликаем по ссылке (пробуем найти кнопку Sign up)
        try:
            page.click("a[href='/signup']")
            time.sleep(2)
        except:
            print("ℹ️ Не нашел кнопку Sign up, продолжаю...")
        
        page.screenshot(path="demo3_github.png")
        print("✅ Навигация выполнена! Скриншот: demo3_github.png")
        
        # ========== ИТОГИ ==========
        print("\n" + "=" * 60)
        print("📊 ОТЧЕТ О РАБОТЕ AI-АГЕНТА")
        print("=" * 60)
        print("✅ Выполнено задач: 3")
        print("✅ Создано скриншотов: 3")
        print("✅ Управление браузером: КЛИК, ВВОД ТЕКСТА, НАВИГАЦИЯ")
        print("✅ Готов к интеграции с OpenAI GPT для анализа")
        print("\n📁 Созданные файлы:")
        print("   - demo1_google_search.png")
        print("   - demo2_youtube_search.png") 
        print("   - demo3_github.png")
        print("=" * 60)
        
        # Закрываем браузер
        input("\nНажми Enter чтобы закрыть браузер...")
        browser.close()
        
        print("\n🎉 AI-агент успешно завершил работу!")
        print("👉 На собеседовании покажу как расширить до полноценного агента с ИИ")

# Запускаем демо
if __name__ == "__main__":
    try:
        simple_agent_demo()
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        print("Проверь установку библиотек: pip install playwright")