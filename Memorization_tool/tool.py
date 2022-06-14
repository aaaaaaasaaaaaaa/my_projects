# write your code here
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///<flashcard.db>?check_same_thread=False')
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Flashcards(Base):
    __tablename__ = 'flashcard'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    box_number = Column(Integer)

Base.metadata.create_all(engine)


while True:
    print("""1. Add flashcards
2. Practice flashcards
3. Exit
666. Delete""")
    option = input()
    if option == '1':
        while True:
            print("""\n1. Add a new flashcard
2. Exit""")
            option = input()
            if option == "1":
                print()
                while True:
                    print("Question:")
                    key = input()
                    if key.strip() == '':
                        continue
                    else:
                        break

                while True:
                    print("Answer:")
                    value = input()
                    if value.strip() == '':
                        continue
                    else:
                        session = Session()
                        new_data = Flashcards(question=key, answer=value, box_number=1)
                        session.add(new_data)
                        session.commit()
                        break

            elif option == "2":
                print()
                break

            else:
                print("\n" + option, "is not an option\n")

    elif option == "2":
        session = Session()
        result_list = session.query(Flashcards).all()
        n = 0
        if len(result_list) == 0:
            print("\nThere is no flashcard to practice!\n")
        else:
            print()
            while n < len(result_list):
                print("Question:", result_list[n].question)
                print("press \"y\" to see the answer: \npress \"n\" to skip:\npress \"u\" to update:")
                option = input()
                if option == 'y':
                    print("\nAnswer:", result_list[n].answer, "\n")
                    print("Box number:", result_list[n].box_number, "\n")
                    while True:
                        print('press "y" if your answer is correct:\npress "n" if your answer is wrong:')
                        option = input()
                        if option == 'y':
                            result_list[n].box_number += 1
                            if result_list[n].box_number > 3:
                                session.delete(result_list[n])
                            session.commit()
                            break

                        elif option == 'n':
                            if result_list[n].box_number > 1:
                                result_list[n].box_number -= 1
                                session.commit()
                                break

                        else:
                            print(f'{option} is not an option')

                elif option == 'n':
                    print()
                elif option == 'u':
                    print("press \"d\" to delete the flashcard:\npress \"e\" to edit the flashcard:")
                    option = input()
                    if option == 'd':
                        session.delete(result_list[n])
                        print()
                    elif option == 'e':
                        print("current question:", result_list[n].question)
                        print("please write a new question:")
                        new_question = input()
                        if new_question.strip() != '' and new_question != result_list[n].question:
                            result_list[n].question = new_question
                            session.commit()

                        print("current answer:", result_list[n].answer)
                        print("please write a new answer:")
                        new_answer = input()
                        if new_answer.strip() != '' and new_answer != result_list[n].answer:
                            result_list[n].answer = new_answer
                            print()
                            session.commit()

                    else:
                        print(option, "is not an option")
                        continue
                else:
                    print(option, "is not an option")
                    continue
                n += 1

    elif option == "3":
        print("\nBye!")
        exit()

    #elif option == "666":
    #    Base.metadata.drop_all(engine)
    else:
        print("\n" + option, "is not an option\n")