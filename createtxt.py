import os
import re

# Base paths
base_path = r"C:\Users\Khozo\Documents\Personal\Mario Kart World\Mario-Kart-World-Randomizer\Images"
characters_path = os.path.join(base_path, "Characters")
karts_path = os.path.join(base_path, "Karts")

# Helper to format name from filename
def format_name(filename):
    name = os.path.splitext(filename)[0]  # Remove file extension
    return re.sub(r'(?<!^)([A-Z])', r' \1', name).strip()  # Add space before caps

# Collect characters
characters = []
for character_folder in os.listdir(characters_path):
    folder_path = os.path.join(characters_path, character_folder)
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif')):
                rel_path = os.path.join("Images", "Characters", character_folder, file).replace("\\", "/")
                characters.append({
                    "picture": rel_path,
                    "name": format_name(file)
                })

# Collect karts
karts = []
for file in os.listdir(karts_path):
    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif')):
        rel_path = os.path.join("Images", "Karts", file).replace("\\", "/")
        karts.append({
            "picture": rel_path,
            "name": format_name(file)
        })

# Write output
output_lines = []
output_lines.append("let characters = [")
for c in characters:
    output_lines.append(f'    {{ picture: "./{c["picture"]}", name: "{c["name"]}" }},')
output_lines.append("];\n")

output_lines.append("let karts = [")
for k in karts:
    output_lines.append(f'    {{ picture: "./{k["picture"]}", name: "{k["name"]}" }},')
output_lines.append("];")

output_text = "\n".join(output_lines)

output_file = os.path.join(base_path, "character_kart_data.txt")
with open(output_file, "w", encoding="utf-8") as f:
    f.write(output_text)

print(f"JavaScript arrays written to: {output_file}")
