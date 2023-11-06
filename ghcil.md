# Github Cil command

1. gh 설치 : brew install gh
2. github connect : gh auth login 
3. github repo 확인 : gh repo list


#gh cil 사용 후 깃허브 잔디 누락현상
이유 : 깃허브 이메일 계정과 로컬의 이메일 정보가 같아야함, branch는 main or gh-pages 둘 중 하나여야 함, forked repo에서 작업한다면 merge가 되지 않을 경우 반영되지 않음.

##해결방법
1. git config --list/ git config --global --list 로 메일주소 확인 
2. 일치하지 않으면 / git config --global user.email "깃허브 등록 이메일 주소"

## 추가 명령어
    git config --global user.email // 이메일 확인
    git config --global user.name //사용자 이름 확인

    git config user.email // 개별 프로젝트의 이메일 확인
    git config user.name  // 개별 프로젝트의 사용자 이름 확인

###PC의 모든 이메일과 사용자 이름을 바꾸고 싶은 경우
    git config --global user.email "이메일"
    git config --global user.name  "사용자 이름" 


###개별 프로젝트의 이메일과 사용자 이름을 바꾸고 싶은 경우
    git config user.email "이메일"
    git config user.name  "사용자 이름" 