"""
faster, Avoid repetition, Template-based, flexibility
"""

from abc import ABC, abstractmethod
from copy import deepcopy


class Document(ABC):
    # base class - like blue print
    
    @abstractmethod
    def create(self):
        pass
    
    @abstractmethod
    def save(self):
        pass
    
    @abstractmethod
    def clone(self):
        """
        Clone creates a deep copy of the object so we can modify it independently.
        Create new variations quickly and not affect other docs or prototype
        """
        pass

class ResumeTemplate(Document):
    
    def __init__(self):
        self.title = "Resume Template"

    def create(self):
        print(f"\n📄 {self.title}")
        print("created")
    
    def save(self):
        print(f"Saving {self.title} to file...")
    
    def clone(self):
        return deepcopy(self)


class LegalDocumentTemplate(Document):

    def __init__(self):
        self.title = "Legal Document Template"
    
    def create(self):
        """Display the legal document"""
        print(f"\n  {self.title}")
        print("created")
    
    def save(self):
        print(f"Saving {self.title} to file...")
    
    def clone(self):
        return deepcopy(self)

class DocumentPrototypeRegistry:

    
    def __init__(self):
        self._prototypes = {}
        print("Document Registry initialized (empty)")
    
    def register_prototype(self, name, prototype):
        self._prototypes[name] = prototype
        print(f"Template '{name}' registered successfully!")
    
    def unregister_prototype(self, name):
        if name in self._prototypes:
            del self._prototypes[name]
            print(f"Template '{name}' removed from registry")
        else:
            print(f"Template '{name}' not found")
    
    def get_clone(self, name):
        if name not in self._prototypes:
            raise ValueError(f"Template '{name}' not found in registry!")
        
        # Clone the prototype and return the copy
        cloned = self._prototypes[name].clone()
        print(f"Created a clone of '{name}' template")
        return cloned
    
    def list_templates(self):
        """Show all available templates"""
        print(f"\nAvailable templates: {list(self._prototypes.keys())}")

def main():
    # create document registry
    registry = DocumentPrototypeRegistry()
    
    # STEP 2: Create original templates (prototypes)
    resume_template = ResumeTemplate()
    legal_template = LegalDocumentTemplate()
    
    # STEP 3: Register the templates
    registry.register_prototype("resume", resume_template)
    registry.register_prototype("legal", legal_template)
    registry.list_templates()
    
    print("\n[STEP 4] Cloning templates to create new documents...")
    print("\n--- Creating Resume #1 ---")
    resume_1 = registry.get_clone("resume")
    resume_1.create()  # Display the resume
    resume_1.save()    # Save it
    
    print("\n--- Modifying Resume #1 ---")
    resume_1.title = "John's Resume"
    resume_1.create()  # Show modified version
    
    # STEP 5: Clone another resume (gets fresh copy of original)
    print("\n--- Creating Resume #2 ---")
    resume_2 = registry.get_clone("resume")
    resume_2.title = "Jane's Resume"
    resume_2.create()
    
    # STEP 6: Demonstrate that originals are unchanged
    print("Original template (should still be 'Resume Template'):")
    resume_template.create()
    
    # STEP 7: Clone a legal document
    print("\n--- Creating Legal Document ---")
    legal_doc = registry.get_clone("legal")
    legal_doc.create()
    
    # Prove original legal template is unchanged
    legal_template.create()
    
    # STEP 8: Show that clones are independent
    print("\n[STEP 6] Proving clones are independent from each other...")
    print(f"resume_1 is resume_2: {resume_1 is resume_2}")  # False - different objects
    print(f"resume_1 and resume_2 are separate objects ✅")
    
main()