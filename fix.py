import re

def fix_unicode_in_tex(file_path):
    """
    Replace Unicode characters in a LaTeX file with LaTeX-compatible equivalents
    and ensure math expressions are correctly wrapped in $...$.
    """
    replacements = {
        # Subscript numbers
        "₀": "_0", "₁": "_1", "₂": "_2", "₃": "_3",
        "₄": "_4", "₅": "_5", "₆": "_6", "₇": "_7",
        "₈": "_8", "₉": "_9",
    }

    # Read file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace Unicode characters
    for unicode_char, latex_equiv in replacements.items():
        content = content.replace(unicode_char, latex_equiv)

    # Wrap subscripts and superscripts in math mode if needed
    # Matches H_0 and wraps it in $...$ if not already wrapped
    content = re.sub(r"(?<!\$)(H_[0-9]+|[A-Za-z]\^[0-9]+)(?!\$)", r"$\1$", content)

    # Write back the updated content
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Replacements and math wrapping applied successfully to '{file_path}'.")

# Replace in your LaTeX file
fix_unicode_in_tex("3. Feladat.tex")
