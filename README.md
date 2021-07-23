# KNU_SW_HACKATHON
## 팀명 "다한"
 컴퓨터학부 글로벌소프트웨어융합전공 2020110289 이연수
 
 컴퓨터학부 글로벌소프트웨어융합전공 2020111395 김현지


## 서비스명(Service Name)
### "POFO: Portfolio For You"

## 서비스 설명(Service Description)
### <주제>
 대학생들을 위한 개인 포트폴리오 관리 사이트

### <동기>
저희는 2020학년도에 입학하여 대학 생활이 어떤 것인지 파악도 채 하기 전에, 코로나 19로 인해 입학과 동시에 비대면 대학생활을 할 수밖에 없었습니다. 
학교에 입학한 지 1년 반이 지난 현재에도, 내가 하고 있는 것이 맞는 지, 내가 얼마나 배웠고, 앞으로 어떤 부분들을 더 배워야 할 지에 대한 고민들로 혼란스럽기만 합니다.
기약없이 이어지고 있는 코로나19 상황으로 인해, 대학 생활에 대한 깊은 고민들과 학생들의 무력감은 더욱 커져만 가고 있습니다.
이러한 문제점들을 해결하기 위해, 정확히는 나의 대학 생활에 스스로 가이드를 제공하고자, 그리고 같은 고민을 가지고 함께 머리를 싸매고 있는 우리의 학우들에게 직접 만든 가이드를 공유하고자 “포트폴리오 정리 사이트”를 구현하게 되었습니다.


### <목적>
코로나로 인해 학교에 적응하는데 오래 걸렸던 경험을 살려 학교, 학과에 대한 정보가 부족한 대학생들에게 도움을 줄 수 있는 웹 플랫폼을 만들었습니다. 저희 웹에서는 전공, 교양, 대외활동, 교내활동을 기준으로, 자신의 활동을 정리할 수 있는 양식을 제공합니다. 전공과 교양 수업 내용을 작성 및 관리하는 페이지에서는, 단순히 학교 강의를 듣고 학점을 받는 것에 그치지 않고, 정리를 통해 꾸준한 복습이 가능하도록 하는 것을 목표로 하였습니다. 또한, 포트폴리오를 어떻게 작성하고 자기소개서를 어떻게 써야 할지 모르는 학생들을 위해, 대외활동, 교내 활동 공간을 만들어, 정리를 통해 자연스럽게 포트폴리오가 되고 자기소개서 소재 저장소가 될 수 있도록 하였습니다.


### <용도>

### 메인화면
- "시작하기"를 통해 포트폴리오 페이지로 이동할 수있습니다.
- __추천사이트__: 임의로 컴퓨터학부 학생들을 대상으로 하여, 코딩 공부에 유익한 사이트 2개(백준, 프로그래머스)를 기재하여 추가적으로 공부하고 싶은 학생에게 제공하고, 학부 사이트를 넣어 공지사항의 내용을 쉽게 확인 할 수 있도록 만들었습니다.

### 포트폴리오 페이지
- __전공, 교양, 대외활동, 교내활동 공통__: "글쓰기"를 통해 제공되는 양식에 맞추어 내용을 정리하고 요약할 수 있습니다. "삭제","수정"을 통해 게시된 글을 관리할 수 있고, "메모"기능을 통해 양식에 구애 받지 않고 comment를 덧붙일 수 있습니다. 또한 "복습 필요/완료" 기능을 추가하여, 마지막으로 복습한 날짜를 기록하도록 하였습니다. 이를 통해 일회성 페이지가 아닌, 지속적인 복습이 가능할 것을 기대합니다. 

- __전공__:

          <추천 양식>
          제목: 
           전공 이름/교수/주차/차시

          본문:
           1. 소제목 : 강의 계획서에 나와 있는 제목을 써도 되고 PPT에 있는 수업 제목을 써도 됨.
                    : 되도록이면 강의를 한 단어/문장으로 압축할 수 있는 말일 수록 보기가 편함
           2. 수업 내용 : 교수님이 강의하신 내용을 정리해서 적거나 노트 필기한 그대로 적을 것.
                       : PPT를 기준으로 PPT 제목 -> 본문 내용 -> 교수님의 설명 순으로 정리하면 다시 보기 좋음.
           3. 질문 거리 & 궁금한 점 : 이해가 안갔던 부분, 교수님께 추가로 질문하고 싶은 부분을 넣을 것
           4. 요약 정리 : 핵심 키워드를 적어 시험 직전 볼 수 있도록 할 것.
                       : 외워야 하는 중요한 개념들을 적어 놓아도 됨.
                       : 전공에 맞춰서 시험 직전에 보면 좋을 것들을 넣어도 됨.

- __교양__:

        <추천 양식>
        제목: 
         교양 이름/교수/주차/차시

        본문:
         1. 소제목 : 강의 계획서에 나와 있는 제목을 써도 되고 PPT에 있는 수업 제목을 써도 됨.
                  : 되도록이면 강의를 한 단어/문장으로 압축할 수 있는 말일 수록 보기가 편함
         2. 수업 내용 : 교수님이 강의하신 내용을 정리해서 적거나 노트 필기한 그대로 적을 것.
                     : PPT를 기준으로 PPT 제목 -> 본문 내용 -> 교수님의 설명 순으로 정리하면 다시 보기 좋음.
         3. 질문 거리 & 궁금한 점 : 이해가 안갔던 부분, 교수님께 추가로 질문하고 싶은 부분을 넣을 것
         4. 요약 정리 : 핵심 키워드를 적어 시험 직전 볼 수 있도록 할 것.
                     : 외워야 하는 중요한 개념들을 적어 놓아도 됨.
                     : 교양 시험에 맞춰서 시험 직전에 보면 좋을 것들을 넣어도 됨.


- __대외활동__:

        <추천 양식>
        제목:
         대외 활동 이름/시기

        본문:
         * 주요 포인트 : 취업이나 다른 활동을 위한 자기소개서 쓸 때 도움이 되는 내용 쓰는 것이 좋음
                      : 혹시 밑에 양식과 다른 내용이 있으면 개인적으로 추가해도 무방.
         1. 참가하게 된 계기 : 자기소개서 쓸 때 앞에 들어가면 가장 좋은 부분. 
                           : ex) ~것에 대한 나의 실력을 키우고자, ~에 도움이 될 것 같은 경험이여서
                           : 위의 양식과 같이 짧게라도 적어놓으면 자기소개서 쓸 때 편하므로 사소한 것이라도 적어놓는 것을 추천 
         2. 대외 활동의 주요 내용 : 어떤 대외 활동을 했는지 요약해서 적어놓으면 면접에서 어떤 내용을 했는지 말하기가 쉬움.
                                +) 자연스럽게 나의 느낀점까지 이야기하면서 기업에 대한 신뢰도를 줄 수 있음.
                                : 자기소개서를 쓸 때에도 깔끔하게 정리하기 편함. 
         3. 대외활동에서 나의 역할 : 면접과 자기소개서에서 가장 중요한 부분. 꼼꼼히 메모해 놓는 것이 좋음.
                                 : 사소한 것이라도 적어놓으면 자기소개서나 면접의 소재가 되기 때문에 많이 적는 것을 추천
         4. 대외활동을 통해 느낀점 : 나의 역할과 마찬가지로 중요한 부분.
                                 : 참가하게 된 계기과 관련시켜 성장한 부분을 적는 것을 추천. 

- __교내활동__:

          <추천 양식>
          제목:
           교내 활동 이름/시기

          본문:
           * 주요 포인트 : 취업이나 다른 활동을 위한 자기소개서 쓸 때 도움이 되는 내용 쓰는 것이 좋음
                        : 혹시 밑에 양식과 다른 내용이 있으면 개인적으로 추가해도 무방.
           1. 참가하게 된 계기 : 자기소개서 쓸 때 앞에 들어가면 가장 좋은 부분. 
                             : ex) ~것에 대한 나의 실력을 키우고자, ~에 도움이 될 것 같은 경험이여서
                             : 위의 양식과 같이 짧게라도 적어놓으면 자기소개서 쓸 때 편하므로 사소한 것이라도 적어놓는 것을 추천 
           2. 교내 활동의 주요 내용 : 어떤 교내 활동을 했는지 요약해서 적어놓으면 면접에서 어떤 내용을 했는지 말하기가 쉬움.
                                  +) 자연스럽게 나의 느낀점까지 이야기하면서 기업에 대한 신뢰도를 줄 수 있음.
                                  : 자기소개서를 쓸 때에도 깔끔하게 정리하기 편함. 
           3. 교내활동에서 나의 역할 : 면접과 자기소개서에서 가장 중요한 부분. 꼼꼼히 메모해 놓는 것이 좋음.
                                   : 사소한 것이라도 적어놓으면 자기소개서나 면접의 소재가 되기 때문에 많이 적는 것을 추천
           4. 교내활동을 통해 느낀점 : 나의 역할과 마찬가지로 중요한 부분.
                                   : 참가하게 된 계기과 관련시켜 성장한 부분을 적는 것을 추천. 
                                                               

- __참조__: 학교에 대한 정보가 부족한 학생에게 알고있으면 유용한 경북대학교 사이트를 기재해놓은 페이지입니다. 다양한 홈페이지들로부터 SW교육센서, 인재개발원 등 유익한 정보들을 많이 얻을 수 있지만, 대부분의 학생들이 모르는 상태로 효율적으로 이용하지 못하는 경우가 많습니다. 이러한 아쉬움을 해소하고, 적절한 정보들을 통해 대학 생활을 하며 더욱 많은 기회들을 접할 수 있기를 바라는 마음으로 추가한 페이지입니다. 기재된 사이트들 외에도, 추가적으로 개인이 원하는 사이트를 추가하고 삭제할 수 있습니다.

## 환경(Environment)
1. 프로그램 실행을 위한 소스코드 에디터 Visual Studio Code 설치가 필요합니다.
2. vs code 실행 후 ctrl+shift+X 통해 확장 메뉴에서 "live server"를 검색하고, 설치를 진행합니다.
3. python은 버전 3을 사용합니다.
* 아래 실행 방법은 Window 운영체제 기반으로 설명되어 있습니다. (Mac/Linux 운영제체에 익숙하지 못해서.. 죄송합니다ㅠ)

## 실행(Usage)
프로젝트 전체의 메인 페이지와 포트폴리오 페이지의 세부 기능 작동 시 충돌을 막기 위해, 서로 다른 포트를 통해 접속이 가능하도록 하였습니다.
__반드시 두 서버(포트)를 모두 실행시킨 상황에서 작동해주세요!__ 
- __첫 째__: h\ecoverde-master\ecoverde-master\index.html 선택
    - ctrl+p → "> Live Server: Open with Live Server" 검색 후 클릭
    - 프로젝트의 메인 페이지 실행 가능
 
- __둘 째__: 
    - 터미널 실행(Git Bash 기준)
    - cd skeleton_code
    - source myvenv/Scripts/activate
    - (Django가 설지되어 있지 않다면) pip install django
    - cd bp
    - python manage.py runserver
    - 포트폴리오 메인 페이지 실행 가능

## 파일 설명(Files)
### h\ecoverde-master\ecoverde-master\index.html
프로젝트의 메인 페이지

***

### skeleton_code\bp\account\templates\home.html
포트폴리오의 메인 페이지(로그인 페이지)

### skeleton_code\bp\account\templates\signup.html
포트폴리오의 회원가입 페이지

***

### skeleton_code\bp\blog\templates\blog.html
포트폴리오의 '전공' 메인 페이지

### skeleton_code\bp\blog\templates\liberal.html
포트폴리오의 '교양' 메인 페이지

### skeleton_code\bp\blog\templates\exter_act.html
포트폴리오의 '대외활동' 메인 페이지

### skeleton_code\bp\blog\templates\inter_act.html
포트폴리오의 '교내활동' 메인 페이지

### skeleton_code\bp\blog\templates\site.html
포트폴리오의 '참조' 메인 페이지

### skeleton_code\bp\blog\templates\new.html
포트폴리오의 전공 글쓰기 페이지

### skeleton_code\bp\blog\templates\new_liberal.html
포트폴리오의 교양 글쓰기 페이지

### skeleton_code\bp\blog\templates\new_exter_act.html
포트폴리오의 대외활동 글쓰기 페이지

### skeleton_code\bp\blog\templates\new_inter_act.html
포트폴리오의 교내활동 글쓰기 페이지

### skeleton_code\bp\blog\templates\new_site.html
포트폴리오의 참조 추가하기 페이지

### skeleton_code\bp\blog\templates\update.html
포트폴리오의 전공 수정하기 페이지

### skeleton_code\bp\blog\templates\update_liberal.html
포트폴리오의 교양 수정하기 페이지

### skeleton_code\bp\blog\templates\update_exter.html
포트폴리오의 대외활동 수정하기 페이지

### skeleton_code\bp\blog\templates\update_inter.html
포트폴리오의 교내활동 수정하기 페이지

### skeleton_code\bp\blog\templates\detail.html
포트폴리오의 작성글 상세 페이지

***

### skeleton_code\bp\templates\basic.html
포트폴리오의 메뉴바 전체 적용 페이지

## 시연영상
[KNU_SW해커톤_"다한"](https://youtu.be/tt7R-oqkt2U)
