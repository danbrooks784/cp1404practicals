"""
CP1404 Prac 6 - Language
Estimated time: 15 minutes
Actual time: 18 minutes
"""

from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

all_languages = [python, ruby, visual_basic]
dynamic_languages = [language for language in all_languages if language.is_dynamic()]
print(f"The dynamically typed languages are:")
for language in dynamic_languages:
    print(language.name)
