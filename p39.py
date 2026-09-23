from abc import ABC, abstractmethod

class Question(ABC):
    def __init__(self, question_text, correct_answer):
        self.question_text = question_text
        self.correct_answer = correct_answer

    @abstractmethod
    def evaluate_answer(self, user_answer):
        pass

class MCQQuestion(Question):
    def __init__(self, question_text, options, correct_answer):
        super().__init__(question_text, correct_answer)
        self.options = options

    def evaluate_answer(self, user_answer):
        is_correct = str(user_answer).strip().upper() == str(self.correct_answer).strip().upper()
        return f"Result: {'Correct' if is_correct else 'Incorrect'}"

class TrueFalseQuestion(Question):
    def evaluate_answer(self, user_answer):
        is_correct = str(user_answer).strip().capitalize() == str(self.correct_answer).strip().capitalize()
        return f"Result: {'Correct' if is_correct else 'Incorrect'}"

class DescriptiveQuestion(Question):
    def evaluate_answer(self, user_answer):
        user_answer_lower = str(user_answer).lower()
        matched_keywords = [kw for kw in self.correct_answer if kw.lower() in user_answer_lower]
        score = (len(matched_keywords) / len(self.correct_answer)) * 100 if self.correct_answer else 0
        return f"Result: Score {score:.1f}% (Matched {len(matched_keywords)}/{len(self.correct_answer)} key concepts)"

if __name__ == "__main__":
    q1 = MCQQuestion("What is the capital of France?", ["A) London", "B) Paris", "C) Berlin", "D) Madrid"], "B")
    q2 = TrueFalseQuestion("Python is dynamically typed.", True)
    q3 = DescriptiveQuestion("Explain encapsulation in OOP.", ["bundling", "data", "methods", "access"])

    questions = [q1, q2, q3]

    print(q1.question_text)
    print("User Answer: B")
    print(q1.evaluate_answer("B"))
    print("-" * 40)

    print(q2.question_text)
    print("User Answer: True")
    print(q2.evaluate_answer(True))
    print("-" * 40)

    print(q3.question_text)
    user_desc = "Encapsulation is the bundling of data and methods together with controlled access."
    print(f"User Answer: {user_desc}")
    print(q3.evaluate_answer(user_desc))
