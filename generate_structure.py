import os

# Define folder structure
structure = {
    "dev-blog": {
        "": [  # Files directly inside dev-blog
            "index.html",
            "dsa.html",
            "dev.html",
            "cs.html",
            "reflection.html",
            "contact.html",
            "README.md"
        ],
        "assets": {
            "css": ["style.css"],
            "js": ["script.js"]
        }
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        dir_path = os.path.join(base_path, name)
        os.makedirs(dir_path, exist_ok=True)

        if isinstance(content, dict):
            create_structure(dir_path, content)
        elif isinstance(content, list):
            for file in content:
                file_path = os.path.join(base_path, name, file)
                open(file_path, "w").close()

# Run the function
create_structure("", structure)
print("✅ Dev blog structure created!")
