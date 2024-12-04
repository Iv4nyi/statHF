import re

def fix_unicode_in_tex(file_path):

    replacements = {
        "₀": "_0", "₁": "_1", "₂": "_2", "₃": "_3",
        "₄": "_4", "₅": "_5", "₆": "_6", "₇": "_7",
        "₈": "_8", "₉": "_9",
    }

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    for unicode_char, latex_equiv in replacements.items():
        content = content.replace(unicode_char, latex_equiv)

    content = re.sub(r"(?<!\$)(H_[0-9]+|[A-Za-z]\^[0-9]+)(?!\$)", r"$\1$", content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Replacements and math wrapping applied successfully to '{file_path}'.")

fix_unicode_in_tex("1. Feladat.tex")
