class PromptManager:
    def __init__(self):
        self.prompts = []

    def add_prompt(self, prompt):
        self.prompts.append(prompt)

    def modify_prompt(self, index, new_prompt):
        if 0 <= index < len(self.prompts):
            self.prompts[index] = new_prompt

    def get_prompt(self, index):
        return self.prompts[index] if 0 <= index < len(self.prompts) else None
 
