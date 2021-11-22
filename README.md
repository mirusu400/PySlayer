# ReOpenSlayer
Server emulator of MMORPG game `WindSlayer` also known as `WS1`.

# About csnsocket
* 윈드슬레이어는 기본적으로 `Fireway.dll` 이라는 파일에서 통신을 진행하고, 이때 사용되는 클래스가 `CSNsocket`이라는 겁니다. 클라이언트 입장에서 패킷을 받을 땐 암호화가 진행되지 않지만, 패킷을 보낼 땐 `XOR` 암호화가 진행됩니다. 이를 에뮬레이션한건 `/lib/csnsocket.py`에 있습니다.

# About copyright
제가 작성한 소스코드 중 단 하나라도 윈드슬레이어 클라이언트 혹은 실제 서버 코드를 이용해 작성한 적이 없습니다. `XOR`키 또한 유저가 클라이언트에서 직접 추출하게 하므로, 저작권엔 아무 문제가 없습니다.

# About license
현재 이 프로젝트는 `GNU License`를 따르고 있습니다. 제 소스코드를 수정할 경우 이를 공개할 의무가 있습니다.

# Special Thanks
* Riuga for help reversing `CSNsocket` and build some server-side packets.