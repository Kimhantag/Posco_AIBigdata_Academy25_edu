# EXAMPLE 11

#include <DHT.h>                     // DHT 센서 라이브러리 불러오기
#include <AsyncTimer.h>              // 비동기 타이머 라이브러리 불러오기
#include <Vegemite.h>                // Vegemite 통신 라이브러리를 불러오기
#include <SoftPWM.h>                 // 소프트웨어 PWM 라이브러리를 불러오기

auto DHT22_PIN = A1;                 // DHT22 센서 핀을 A1에 연결
auto FAN_PIN = A3;                   // 팬 핀을 A3에 연결
auto PUMP_PIN = 16;                  // 펌프 핀을 16에 연결

AsyncTimer t;                        // 비동기 타이머 t 생성
Vegemite v;                          // Vegemite 통신 객체 v생성
SOFTPWM_DEFINE_CHANNEL(FAN_PIN);     // 소프트웨어 PWM 채널을 팬 핀에 정의
DHT dht(DHT22_PIN, DHT22);           // DHT22 센서 객체 dht 생성
bool currentPumpWorking = false;     // 펌프 동작 상태를 나타내는 변수 생성.

void setup() {
  Serial.begin(250000);              // 시리얼 통신을 250000로 초기화
  SoftPWM.begin(490);                // 소프트웨어 PWM을 490Hz 주파수로 초기화
  dht.begin();                       // DHT22 센서를 초기화

  pinMode(PUMP_PIN, OUTPUT);         // 펌프 핀을 출력 모드로 설정

  v.requestSubscription("pump-water");              // Vegemite 통신을 통해 "pump-water" 구독을 요청
  v.requestSubscription("config-fan");              // Vegemite 통신을 통해 "config-fan" 구독을 요청

  //1번 코드블럭: 1초마다 실행되는 코드블럭
  t.setInterval([](){
    float humidity = dht.readHumidity();            // 습도를 읽어옴
    float temperature = dht.readTemperature();      // 온도를 읽어옴
    if(!isnan(humidity) && !isnan(temperature)) {   // 습도와 온도가 nan이 아니면
      v.send("temperature", temperature);           // 온도를 Vegemite 통신을 통해 전송
      v.send("humidity", humidity);                 // 습도를 Vegemite 통신을 통해 전송
    }
  }, 1000);                                         // 1초마다 실행

  //2번 코드블럭: 0.5초마다 실행되는 코드블럭
  t.setInterval([](){
    int pumpWater = int(v.recv("pump-water"));      // "pump-water" 데이터를 통해 펌프 작동 명령 판단
    int fanConfig = int(v.recv("config-fan"));      // "config-fan" 데이터를 통해 팬 작동 명령 판단

    if (pumpWater == 1 && !currentPumpWorking) {    // 펌프 작동 명령이 오고, 펌프가 현재 작동되고 있지 않다면
      currentPumpWorking = true;                    // 펌프가 작동되도록 변경
      v.send("pump-water", 0);                      // "pump-water" 데이터를 전송하여 펌프 작동됨을 알림
      digitalWrite(PUMP_PIN, HIGH);                 // 펌프를 활성화
      t.setTimeout([](){                            // 설정된 시간(5초)가 지난 후에
        digitalWrite(PUMP_PIN, LOW);                // 펌프를 비활성화함
        currentPumpWorking =false;                  // 펌프의 작동을 멈춤
      }, 5000);                                     // 작동 시간을 5초로 설정함
    }
    SoftPWM.set(fanConfig == 1 ? 100:0);            // 팬 설정에 따라 소프트웨어 PWM을 조절하여 팬을 제어.
  }, 500);
}

void loop(){
  v.subscribe();                                     // Vegemite 통신구독
  t.handle();                                        // 비동기 타이머를 처리
}


