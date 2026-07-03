from copy import deepcopy

class Document:
    def __init__(self, title):
        self.title = title
    
    def clone(self):
        return deepcopy(self)
    
    def __str__(self):
        return f"Document: {self.title}"

# Create original template
resume_template = Document("Resume Template")

# Clone to create new documents
resume_1 = resume_template.clone()
resume_1.title = "John's Resume"

resume_2 = resume_template.clone()
resume_2.title = "Jane's Resume"

print(resume_template)  # Document: Resume Template
print(resume_1)         # Document: John's Resume
print(resume_2)         # Document: Jane's Resume

print(f"\nAre they same object? {resume_1 is resume_2}")  # False