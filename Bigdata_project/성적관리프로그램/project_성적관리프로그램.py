# 김한탁 email = gksxkrdl@naver.com
# 라이브러리 -------------------------------------------------------------------------------------------------------------- 
import sys


# 자주 사용되는 함수 정의 ----------------------------------------------------------------------------------------------------
def Grade(average):       # 성적 산출 함수
    if average >=90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

def start_form():         # 시작서식 함수
    print()
    print("Student" + "\t\t" + "Name" + "\t\t" + "Midterm" + "\t" + "Final" + "\t" + "Average" + "\t" + "Grade")
    print("-"*60)

def end_form():           # 끝서식 함수
    print("-"*60)
    print()


## 1. show 함수 ----------------------------------------------------------------------------------------------------------
def show_function(stu_list):
    start_form()
    student_avgsort_list = sorted(stu_list, key = lambda x : x[4], reverse = True)   # avg기준으로 학생정보를 정렬한 리스트 출력
    for student in student_avgsort_list:
        print(student[0], "\t", student[1], "\t", student[2], "\t", student[3], "\t", round(student[4],1), "\t", student[5])
    end_form()


## 파일 불러오기, 초기 시작 화면 출력 및 중첩리스트를 이용한 데이터 저장 --------------------------------------------------------------
while (True):
    file_name = sys.argv[-1]
    if (file_name == "students.txt") or (file_name == "project.py"):
        with open("students.txt", "r") as f_student:
            student_list = []   # 학생정보가 담길 리스트

            for line in f_student: 
                sid, name, mid, final = line.split("\t")

                mid = int(mid)
                final = int(final)
                avg = (mid + final) / 2
                grade = Grade(avg)
                student_list.append([sid, name, mid, final, avg, grade])
        
        show_function(student_list)
        break

## 2. search 함수 --------------------------------------------------------------------------------------------------------
def search_function(stu_list):
    stu_id = input("Student ID: ")
    found_success = False
    for student in stu_list:
        if stu_id == student[0]:
            start_form()
            print(student[0], "\t", student[1], "\t", student[2], "\t", student[3], "\t", round(student[4],1), "\t", student[5])
            end_form()
            found_success = True
            break
    if found_success != True:
        print("NO SUCH PERSON.")
        print()
    

## 3. changescore 함수----------------------------------------------------------------------------------------------------
def changescore_function(stu_list):
    stu_id = input("Student ID: ")
    found_success = False
    for student in stu_list:
        
        if stu_id == student[0]:
            m_f = input("Mid/Final? ").lower()
            if (m_f == "mid"):
                mid_score = int(input("Input new score: "))
                if (mid_score < 0) or (mid_score>100):
                    found_success = True
                    print("*"*12 + "1부터 100까지의 값을 입력해주세요..." + "*"*12) 
                    print()

                else:
                    start_form()
                    print(student[0], "\t", student[1], "\t", student[2], "\t", student[3], "\t", round(student[4],1), "\t", student[5])
                    student[2] = mid_score
                    student[4] = (student[2] + student[3]) / 2
                    student[5] = Grade(student[4])
                    print("Score Changed.")
                    print(student[0], "\t", student[1], "\t", student[2], "\t", student[3], "\t", round(student[4],1), "\t", student[5])
                    print()
                    found_success = True

            elif (m_f == "final"):
                final_score = int(input("Input new score: "))
                if (final_score < 0) or (final_score>100):
                    found_sccuess = True
                    print()

                else:
                    start_form()
                    print(student[0], "\t", student[1], "\t", student[2], "\t", student[3], "\t", round(student[4],1), "\t", student[5])
                    student[3] = final_score
                    student[4] = (student[2] + student[3]) / 2
                    student[5] = Grade(student[4])
                    print("Score Changed.")
                    print(student[0], "\t", student[1], "\t", student[2], "\t", student[3], "\t", round(student[4],1), "\t", student[5])
                    print()
                    found_success = True
                
            else:
                found_success = True
                print("*"*20 + "Please Check Again..." + "*"*20) 
                print()

    if found_success != True:
        print("NO SUCH PERSON.")
        print()

    return stu_list


## 4. add함수 ------------------------------------------------------------------------------------------------------------
def add_function(stu_list):
    stu_id = input("Student ID: ")
    found_success = False
    for student in stu_list:
        
       if stu_id == student[0]:
           found_success = True
           print("ALREADY EXISTS.")
           print()
           break
           
       else:
           found_success = False

    if found_success == False:
        name = input("Name: ")
        
        while(True):
            mid_score = int(input("Midterm Score: "))
            
            if (mid_score > 100) or (mid_score < 0):
                print("*"*12 + "1부터 100까지의 값을 입력해주세요..." + "*"*12) 
                print()
                break
            
            final_score = int(input("Final Score: "))
           
            if (final_score < 0 ) or (final_score > 100) :
                print("*"*12 + "1부터 100까지의 값을 입력해주세요..." + "*"*12) 
                print()
                break
         
            avg = (mid_score + final_score) / 2
            grade = Grade(avg)
            print("Student added.")
            print()
            stu_list.append([stu_id, name, mid_score, final_score, avg, grade])
            break
    
    return stu_list


## 5. searchgrade 함수 ---------------------------------------------------------------------------------------------------
def searchgrade_function(stu_list):
    grade = input("Grade to search: ").upper()
    if grade in ["A", "B", "C", "D", "F"]:
        grade_list = []
        for student in stu_list:
            if student[5] == grade:
                grade_list.append(student)  # Append the whole student record

        # Title() 호출을 검색된 결과가 있을 때만 실행
        if len(grade_list) > 0:
            start_form()  # 해당 학점을 받은 학생이 있을 때만 Title 함수 호출
            for student in grade_list:
                print(student[0], "\t", student[1], "\t", student[2], "\t", student[3], "\t", round(student[4],1), "\t", student[5])
                print()
        else:
            print("NO RESULTS.")
            print()
    else:
        print("해당 학점은 존재하지 않습니다.")
        print()
    return stu_list


## 6. remove 함수 --------------------------------------------------------------------------------------------------------
def remove_function(stu_list):
    if len(stu_list)!=0:
        
        stu_id = input("Student ID: ")
        found_success = False
        for student in stu_list:
        
            if stu_id == student[0]:
                found_success = True
                start_form()
                print(student[0], "\t", student[1], "\t", student[2], "\t", student[3], "\t", round(student[4],1), "\t", student[5])
                print()
                print("위의 학생 정보가 삭제됩니다.")
                ans = input("정말 삭제하시겠습니까?(Y/N):").upper()
            
                if ans == "Y" :
                    print()
                    print(student[1], "의 학생 정보가 삭제되었습니다.")
                    stu_list.remove(student)
                    print()
                    break
            
                else:
                    print("취소되었습니다.")
                    print()
                    break            
    
        if found_success == False:
            print("NO SUCH PERSON.")
            print()

    else:
        print("List is empty.")
        print()
    
    return stu_list


## 7. quit함수 -----------------------------------------------------------------------------------------------------------
def quit_function(stu_list):
    while(True):
        answer = input("Save data?[yes/no] ").lower()
        if answer == "yes":
            print("다음의 데이터를 저장합니다.")
            show_function(stu_list)
            file_name = input("File name: ").replace(" ", "")
            with open(file_name, "w") as f:
                # stu_avgsort_list : 학생들을 평균을 기준으로 내림차순 정렬한 리스트
                student_avgsort_list = sorted(stu_list, key = lambda x : x[4], reverse = True)   # avg기준으로 학생정보를 정렬한 리스트 출력
                for student in student_avgsort_list:
                    f.write(str(student[0])+"\t"+str(student[1])+"\t"+str(student[2])+"\t"+str(student[3])+"\t"+str(student[4])+"\t"+str(student[5])+"\n")
            print("저장이 완료되었습니다!")

            break
    
        elif answer == "no":
            print("저장하지 않고 종료합니다.")
            print()
            break

        else:
            print("다시 입력해 주세요.")
            print()


# 반복 질문 실행 -----------------------------------------------------------------------------------------------------------
command_list = ['show', 'search', 'changescore', 'searchgrade', 'add', 'remove', 'quit']
while(True):
    command = input("#").lower()
    if command == 'show':
        show_function(student_list)
    
    elif command == 'search':
        search_function(student_list)
    
    elif command == 'changescore':
        student_list = changescore_function(student_list)
    
    elif command == 'searchgrade':
        studnt_list = searchgrade_function(student_list)
    
    elif command == 'add':
        student_list = add_function(student_list)
    
    elif command == 'remove':
        student_list = remove_function(student_list)

    elif command == 'quit':
        quit_function(student_list)
        break
    else:
        print("*"*30 + "wrong input!" + "*"*30)
        print("*"*27 + "다시 입력해 주세요." + "*"*27)
        print()






        


    
