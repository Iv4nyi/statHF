import re

def fix_unicode_in_tex(file_path):
    """
    Replace Unicode subscript characters in a LaTeX file with LaTeX-compatible equivalents,
    ensuring subscripts (e.g., X_1) are correctly wrapped in $...$ math mode,
    while ignoring filenames, paths, and LaTeX commands.
    """
    # Define replacements for Unicode subscript numbers
    replacements = {
        "₀": "_0", "₁": "_1", "₂": "_2", "₃": "_3",
        "₄": "_4", "₅": "_5", "₆": "_6", "₇": "_7",
        "₈": "_8", "₉": "_9",
    }

    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace Unicode subscripts
    for unicode_char, latex_equiv in replacements.items():
        content = content.replace(unicode_char, latex_equiv)

    # Ensure math mode for subscripts (e.g., X_1), ignoring filenames and LaTeX commands
    def wrap_subscripts(match):
        context, subscript = match.group(1), match.group(2)
        # Skip wrapping for filenames or commands
        if context and (context.startswith("\\includegraphics") or context.startswith("\\input")):
            return match.group(0)  # No changes for commands
        return f"{context}${subscript}$"

    # Match plain text subscripts, excluding filenames and LaTeX commands
    content = re.sub(r"(\\[a-zA-Z]+{[^}]*}|)?([A-Za-z]_[0-9]+)", wrap_subscripts, content)

    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Subscripts wrapped in math mode and Unicode replacements applied to '{file_path}'.")

# Apply fixes to the LaTeX file
fix_unicode_in_tex("2. Feladat.tex")
