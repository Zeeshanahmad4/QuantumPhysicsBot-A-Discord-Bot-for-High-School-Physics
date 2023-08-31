class KnowledgeBase:
    def __init__(self):
        self.kb = {}

    def add_qa_pair(self, question, answer):
        self.kb[question] = answer

    def get_answer(self, question):
        return self.kb.get(question, None)

    def update_answer(self, question, new_answer):
        if question in self.kb:
            self.kb[question] = new_answer
 
