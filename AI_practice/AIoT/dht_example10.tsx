// EXAMPLE 10

import React from 'react'; // React 라이브러리를 가져옴
import PageWrapper from 'components/internal/PageWrapper'; // 내부 페이지 래퍼 컴포넌트를 가져옴
import NumberDisplay from 'components/NumberDisplay'; // NumberDisplay 컴포넌트를 가져옴

// 페이지 컴포넌트를 정의
const Page: React.FC = function () {
  return (
    // 페이지의 메인 제목을 "DHT Status"로 지정
    <PageWrapper title="DHT Status">

      {/* 온도를 나타내는 NumberDisplay 컴포넌트를 생성 */}
      {/* 컴포넌트에 표시되는 레이블명 : Temperature */}
      {/* 컴포넌트에 온도를 나타내기 위해, 사용하는 데이터 : temperature */}
      {/* 컴포넌트에 표시되는 단위 : ℃ */}
      <NumberDisplay label="Temperature" dataID="temperature" unit="℃" />

      {/* 습도를 나타내는 NumberDisplay 컴포넌트를 생성 */}
      {/* 컴포넌트에 표시되는 레이블명 : Humidity */}
      {/* 컴포넌트에 습도를 나타내기 위해, 사용하는 데이터 : humidity */}
      {/* 컴포넌트에 표시되는 단위 : % */}
      <NumberDisplay label="Humidity" dataID="humidity" unit="%" />

      {/* 1분 후 예측된 온도를 나타내는 NumberDisplay 컴포넌트를 생성 */}
      {/* 습도를 나타내는 NumberDisplay 컴포넌트를 생성 */}
      {/* 컴포넌트에 표시되는 레이블명 : Temperature After 1m */}
      {/* 컴포넌트에 온도를 나타내기 위해, 사용하는 데이터 : temperature */}
      {/* 컴포넌트가 추론 수행 */}
      {/* 컴포넌트에 표시되는 단위 : ℃ */}
      <NumberDisplay
        label="Temperature After 1m"
        dataID="temperature"
        dataDispID="temperature-inf"
        action="inference"
        unit="℃"
      />
      {/* 1분 후 예측된 습도를 나타내는 NumberDisplay 컴포넌트를 생성 */}
      {/* 습도를 나타내는 NumberDisplay 컴포넌트를 생성 */}
      {/* 컴포넌트에 표시되는 레이블명 : humidity After 1m */}
      {/* 컴포넌트에 추론된 습도를 나타나기 위해 참조하는 데이터 : humidity */}
      {/* 컴포넌트가 추론 수행 */}
      {/* 컴포넌트에 표시되는 단위 : % */}
      <NumberDisplay
        label="humidity After 1m"
        dataID="humidity"
        dataDispID="humidity-inf"
        action="inference"
        unit="%"
      />
    </PageWrapper>
  );
};

// 페이지 컴포넌트 내보내기
export default Page;
