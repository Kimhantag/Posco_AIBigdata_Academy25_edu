// EXAMPLE 11

import ConditionLight from 'components/ConditionLight'; // ConditionLight 컴포넌트를 가져옴
import ControlGroup from 'components/ControlGroup'; // ControlGroup 컴포넌트를 가져옴
import NumberDisplay from 'components/NumberDisplay'; // NumberDisplay 컴포넌트를 가져옴
import PushButton from 'components/PushButton'; // PushButton 컴포넌트를 가져옴
import ToggleSwitch from 'components/ToggleSwitch'; // ToggleSwitch 컴포넌트를 가져옴
import PageWrapper from 'components/internal/PageWrapper'; // 내부 페이지 래퍼 컴포넌트를 가져옴
import React from 'react'; // React 라이브러리를 가져옴

// 페이지 컴포넌트를 정의
const Page: React.FC = function () {
  return (
    // 페이지의 메인 제목을 "IoT Web Component Example"로 지정
    <PageWrapper title="IoT Web Component Example">

      {/* DHT Sensor를 제어하는 ControlGroup 컴포넌트 */}
      <ControlGroup label="DHT Sensor">

        {/* 온도를 나타내는 NumberDisplay 컴포넌트를 생성 */}
        {/* 컴포넌트에 표시되는 레이블명 : Temperature */}
        {/* 컴포넌트에 온도를 나타내기 위해, 사용하는 데이터 : temperature */}
        {/* 컴포넌트에 표시되는 단위 : ℃ */}
        <NumberDisplay label="Temperature" dataID="temperature" unit="℃" />

        {/* 온도를 나타내는 ToggleSwitch 컴포넌트를 생성 */}
        {/* 컴포넌트에 표시되는 레이블명 : Fan */}
        {/* 컴포넌트에 Fan을 제어하는데, 사용하는 데이터 : config-fan */}
        <ToggleSwitch label="Fan" dataID="config-fan" />
      </ControlGroup>

      {/* Humidity Control을 제어하는 ControlGroup 컴포넌트 */}
      <ControlGroup label="Humidity Control">

        {/* 습도를 나타내는 NumberDisplay 컴포넌트를 생성 */}
        {/* 컴포넌트에 표시되는 레이블명 : Humidity */}
        {/* 컴포넌트에 습도를 나타내기 위해, 사용하는 데이터 : humidity */}
        {/* 컴포넌트에 표시되는 단위 : % */}
        <NumberDisplay label="Humidity" dataID="humidity" unit="%" />

        {/* 습도에 따라 색이 변경되는 ConditionLight 컴포넌트 생성. */}
        {/* 컴포넌트에 표시되는 레이블명 : Air Humidity Light */}
        {/* 컴포넌트에 습도에 따른 색을 나타내기 위해, 사용하는 데이터 : humidity */}
        {/* ConditionLight 컴포넌트에서 ColoringRule 속성 함수(humidity가 85보다 작으면 #00FF00
          , 아니면 #FF0000)에 따라 색상 결정 */}
        <ConditionLight
          label="Air Humidity Light"
          dataID="humidity"
          coloringRule={(humidity:number) => (
            humidity < 85 ? '#00FF00' : '#FF0000'
          )}
        />
        {/* 물을 펌핑하는 PushButtom 컴포넌트 생성. */}
        {/* 컴포넌트에 표시되는 레이블명 : Pump */}
        {/* 컴포넌트에 Pump를 제어하기 위해, 사용하는 데이터 : Pump-water */}
        {/* Button에 표시되는 설명 : Pump Up */}
        {/* Button에 대한 부가 설명 : Push this button to pump water for 5 seconds */}
        <PushButton
          label="Pump"
          dataID="pump-water"
          buttonText="Pump Up"
          description="Push this button to pump water for 5 seconds"
        />
      </ControlGroup>
    </PageWrapper>
  );
};

// 페이지 컴포넌트를 내보내기
export default Page;
