# 1983

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    # N = 학생수, K = 학생번호

    # 입력 학생 중간, 기말, 과제 점수
    # 입력받은 중간,기말,과제점수로 총점을 계산한 학생별 총점들
    student_score = []
    # K번째 학생 점수 미리저장 딕셔너리 만들기
    student_k = {}
    # 입력을 n번 받아야 => 반복문
    for i in range(1, N+1): # i의 범위 : 1 ~ N
        # 우리가 찾고 싶은거? K번째 점수 찾아서 저장해야 되니까
        # 그럼? 순서대로 돌다가 K번째가 오면 그걸 딕셔너리에 넣어야겠다.
        mid,final,homework = map(int, input().split())
        # 총점 계산
        grade_result = mid * 0.35 + final * 0.45 + homework * 0.2
        # 일단, 리스트에 넣어야지 총점을
        student_score.append(grade_result)
        # 이때, 지금이 K번째면, 딕셔너리에 저장하자
        if i == K:
            # 딕셔너리명[키] = 값
            # 딕셔너리에 {키:값}으로 저장됨
            # 점수저장 (K번째학생의 총점)
            student_k[K] = grade_result

    # 완성본 보기
    # print(student_score)

    # 높은순대로 학점을 나눠줄때, 높은 순 대로? 정렬이 필요하겠다! 라는 생각 => 내림차순
    # 일단, 정렬 니가 해줘 컴퓨터야 ok?
    # 정렬 : sort() => 리스트를 정렬해줌, 리스트이름.sort() 이런식으로 사용
    student_score.sort(reverse=True) # 내림차순, 오름차순은 그냥 아무것도 안넣어도 기본값이 False
    # print(student_score)
    # 정렬하면? K번째 학생이 누구였는지 어떻게 기억하나?
    # K번째학생의 점수를 기억해놓자
    # 간단하게 K번째학생점수 = 100점 이렇게 저장하려면
    # key와 value로 이루어진 딕셔너리 {K:100} 이런식으로 저장을해놓자
    # 처음에 저장해놓고, 나중에 정렬했을 때, 이 딕셔너리의 K를 키로 가지는 값(점수)과 똑같은
    # 값(점수)의 위치 => 정렬된 리스트에서 K번째 학생 점수가 어디있는지
    # 어디있는지를 왜 알아야 하냐? 순서대로 평점을 줄거니까
    # 20명 중에, 정렬하고 보니 K번째 학생이 정렬하고 20등으로 가버림 => K번째학생의 평점은? D0
    # 우리가 이걸 하려고 지금 하는 거다
    #
    # N/10 명의 학생들에게 동일한 평점을 부여 => 필요가 없을 수도 있다
    # 그냥 계산해서 위치에 아 여기에 이 학점이겠다. 하고 그냥 K번째 학생의 학점만 가져올 수 있음
    # student_score가 학생 총점리스트, 정답!
    grade_score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    for i in range(len(student_score)):
        if student_k[K] == student_score[i]:  # K번 학생의 점수 찾기
            grade = grade_score[i // (N // 10)]  # 등급 계산
            print(f"#{tc} {grade}")  # 해당 tc와 학점 출력
            break  # 찾으면 반복 종료 (불필요한 반복 방지)

    # K 번째 학생 학점 알고싶음
    # 10개의 학점
    #  => 학점 문자열로 따옴표 붙이기