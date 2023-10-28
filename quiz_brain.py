class QuizBrain():
    def __init__(self,questions_list):
        self.question_number = 0    #question we are currently on
        self.questions_list=questions_list
        self.score = 0
        
    def still_has_questions(self):
        if self.question_number < len(self.questions_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        userAnswer = input(f'Q.{self.question_number}: {current_question.text} (True or False): ')
        self.check_answer(userAnswer,current_question.answer)
    
    def check_answer(self,userAnswer,correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            self.score += 1
            print('You got it right!')
        else:
            print('Thats wrong!')
        print(f'The correct answer was: {correctAnswer}')
        print(f'Your current score is: {self.score}/{self.question_number}')
        print('\n')
        
