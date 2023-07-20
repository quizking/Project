class AnimalQuiz:
    def __init__(self):
        self.score = 0

    def check_guess(self, guess, answer):
        attempt = 0
        while attempt < 3:
            if guess.lower() == answer.lower():
                print("Correct Answer")
                self.score += 1
                break
            else:
                if attempt < 2:
                    guess = input("Sorry, Wrong Answer. Try again: ")
                attempt += 1
        else:
            print("The Correct answer is", answer)

    def run_quiz(self):
        print("Guess the Animal")
        guess1 = input("What is a group of cats called?\nA) school \nB) clowder\nC) colony\nAnswer: ")
        self.check_guess(guess1, "B")

        guess2 = input("What is the only mammal capable of true flight?\nA) Cheetah\nB) Bats\nC) penguins\nAnswer: ")
        self.check_guess(guess2, "B")

        guess3 = input("Which is the largest animal?\nA) Blue Whale\nB) Elephant\nC) Giraffe\nAnswer: ")
        self.check_guess(guess3, "A")

        print("Your Score is", self.score)


if __name__ == "__main__":
    quiz = AnimalQuiz()
    quiz.run_quiz()
