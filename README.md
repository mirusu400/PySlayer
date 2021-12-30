# PySlayer
An single python server emulator of MMORPG game `WindSlayer` also known as `WS1`.

# Requirements
* Python >= 3.7
* Old windslayer client (Korea Yahoo! ver.)

# Installation
1. 윈드슬레이어 야후 버전(MD5:`209dfadadbd83badaab2f85d075accae`)을 구해서 `/patch/WS1Yahoo.xdelta` 패치를 적용합니다. 서버를 로컬호스트로 돌리고, 야후로 리다이렉션 되는것을 막아줍니다. 

2. `/utils/get_xorkey.py`를 실행하면 검은색창이 나오는데, 윈드슬레이어 야후 버전의 `Fireway.dll`파일을 검은색 창 위로 드래그 한 후 엔터를 누릅니다. 자동으로 `_key.py` 파일이 생성되면 이를 `server.py`가 있는 폴더와 동일한 경로에 놔둡니다.

3. `server.py` 파일을 실행하면 자동으로 서버가 실행됩니다. 이후 패치된 야후 윈드슬레이어 클라이언트를 실행하면 됩니다.

# What can we do for now?
지금 현재는 인게임밖에 안됩니다.

# TODO
- [ ] 패킷 분석 및 문서화
- [ ] 로컬 데이터베이스 구축
- [ ] UDP 패킷 통신 분석 및 에뮬레이션
- [ ] 멀티플레이어 활성화

# Why we cannot play on multi?
제가 파이썬이란 언어를 선택한 이유는 가장 익숙하기도 하지만 빠르게 오고가는 통신을 쉽게 확인하고 조작하기 쉽게 하기 때문이었습니다. 다만 파이썬은 멀티쓰레드를 구현하기 복잡하고, 패킷 분석을 집중적으로 하고있기 때문에 현재는 멀티를 지원하지 않습니다.

# About CSNsoceket
윈드슬레이어는 기본적으로 `Fireway.dll` 이라는 파일에서 통신을 진행하고, 이때 사용되는 클래스가 `CSNsocket`이라는 겁니다. 클라이언트 입장에서 패킷을 받을 땐 암호화가 진행되지 않지만, 패킷을 보낼 땐 `XOR` 암호화가 진행됩니다. 이를 에뮬레이션한건 `/lib/csnsocket.py`에 있습니다.

# About Copyright
제가 작성한 소스코드 중 단 하나라도 윈드슬레이어 클라이언트 혹은 실제 서버 코드를 이용해 작성한 적이 없습니다. `XOR`키 또한 유저가 클라이언트에서 직접 추출하게 하므로, 저작권엔 아무 문제가 없습니다. 다만 이를 통해 상용 서버를 열고, 변조된 클라이언트를 배포하게 된다면 저작권에 저촉될 가능성이 존재합니다. 이에 대한 불이익 및 처벌에 대하여 저는 아무런 책임을 지지 않습니다.

# About License
현재 이 프로젝트는 `GPL License`를 따르고 있습니다. 제 소스코드를 수정할 경우 이를 공개할 의무가 있습니다. 제 프로젝트에 대한 Contribute는 언제나 환영합니다.

# Special Thanks
* Riuga for help reversing `CSNsocket` and build some server-side packets.