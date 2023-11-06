# Git 명령어

- git status : 현재 상태 확인
- git add [파일명] : 파일을 추가
- git add . : 모든 파일 추가
- git commit -m "메세지" : 커밋
- git push origin master : 원격 저장소에 올리기
- git pull origin master : 원격 저장소에서 가져오기
- git clone [url] : 원격 저장소에서 복제
- git log --all --online : 커밋 내역 조회
- git log --all --graph : 커밋 그래프로 보기


## 브랜치
- git branch : 브랜치 목록 확인
- git branch [브랜치명] : 브랜치 생성
- git checkout [브랜치명] : 브랜치 변경
- git merge [브랜치명] : 브랜치 병합
- git branch -d [브랜치명] : 브랜치 삭제 (merge완료된 브랜치 삭제)
- git branch -D [브랜치명] : 브랜치 삭제 (merge안한 브랜치 삭제)
- git rebase [브랜치명] : 브랜치의 신규 시작점을 최신으로 옮길 수 있다.
- git squash [브랜치명] : 깔끔한 merge

* 서브 브랜치에서 개발한 것은 서브 브랜치에서만 가능
* 메인 브랜치로 스위치하면, 그 파일들은 없어짐
* 보통 브랜치를 만들어서 작업하고, 작업이 완료되면 메인 브랜치로 합치는 방식으로 진행
* 각 다른 브랜치에서 같은 파일, 같은 줄을 수정하면 merge로 합칠 때 충돌이 발생함
/n 
* 3-way-merge는 복잡하다. 간단하게 하려면 rebase를 쓰는 것을 추천
* rebase의 단점 : conflict엔딩이 많이 남


## 원격 저장소
- git remote add [저장소명] [url] : 원격 저장소 추가
- git remote -v : 원격 저장소 목록 확인
- git remote remove [저장소명] : 원격 저장소 삭제
- git clone 주소 - 깃허브에 있는 프로젝트를 내려받는 명령어
- git pull - 깃허브에 있는 프로젝트를 업데이트 하는 명령어
- git push - 깃허브에 있는 프로젝트를 업로드 하는 명령어
- git remote add origin 주소 - 깃허브에 있는 프로젝트를 연결하는 명령어

## 기타
- git  restore [파일명] : 파일복구
- git restore --source [커밋해시] [파일명] : 특정 commit 시점으로 파일 복구하는법 
- git restore --staged [파일명] : 스테이징된 파일을 unstaged로 변경(파일단위 복구)
- git log : 커밋 로그 확인
- git reset --hard [커밋ID] : 과거 커밋으로 되돌아가기 (모든걸 되돌리기)
- git reset --soft [커밋ID] : 과거 커밋으로 되돌아가기 (변동사항 지우지 말고 staging 해놓기)
- git reset --mixed [커밋ID] : 변동사항 지우지 말고 unstaged 해놓기

- git reset HEAD [파일명] : 파일의 변경 내용 되돌리기
- git checkout -- [파일명] : 파일의 변경 내용 되돌리기
- git reset --hard HEAD^ : 마지막 커밋으로 되돌아가기
- git reset --hard HEAD^^ : 마지막 커밋으로 되돌아가기
- git reset --hard HEAD~2 : 마지막 커밋으로 되돌아가기
- git reset --hard [커밋ID] : 해당 커밋으로 되돌아가기 
- git reset --hard origin/master : 원격 저장

- git stash - 현재 작업중인 내용을 임시저장하는 명령어
- git stash list - 임시저장한 내용을 확인하는 명령어
- git stash pop - 가장 최근에 임시저장한 내용을 불러오는 명령어


