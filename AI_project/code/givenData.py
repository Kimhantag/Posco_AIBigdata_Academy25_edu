#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import random
from ultralytics import YOLO

def filter_boxes(boxes, names, min_confidence=0.5):
    filtered_results = []
    for box, name in zip(boxes, names):
        if len(box) > 4 and box[4] >= min_confidence:
            car_name = ['carnival', 'ray', 'soul', 'sportage', 'starex', 'tucson']
            if name in car_name:
                filtered_results.append((name, box[4], box[:4]))
    return filtered_results

# YOLO 모델을 불러옴
model = YOLO('/home/piai/다운로드/Online-3D-BPP-pCT-density-code-add/best.pt')
cap = cv2.VideoCapture(0)

# 감지된 자동차에 따른 컨테이너 크기 저장
car_container_sizes = {
    'carnival': [123, 231, 100],
    'ray': [134, 95, 110],
    'soul': [105, 126, 83],
    'sportage': [103, 85, 73],
    'starex': [162, 237, 134],
    'tucson': [103, 159, 77]
}

# 실시간 비디오 스트림 처리
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        results = model(frame)
        cv2.imshow("Webcam", results[0].plot())

        if len(results) > 0:
            filtered_results = filter_boxes(results[0].boxes, results[0].names, min_confidence=0.5)
            annotated_frame = frame.copy()
            for name, conf, bbox in filtered_results:
                bbox = [int(coord) for coord in bbox]
                cv2.rectangle(annotated_frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
                cv2.putText(annotated_frame, f'{name} {conf:.2f}', (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        for result in results:
            clist = result.boxes.cls
            cls = set()
            for cno in clist:
                cls.add(model.names[int(cno)])

            for car in cls:
                if car in car_container_sizes:
                    print(f"Detected {car}")
                    container_size = car_container_sizes[car]
                    print("Container Size for", car, ":", container_size)
                    # cv2.destroyAllWindows()  # 모든 OpenCV 창을 닫음
                    # cap.release()  # 카메라 자원 해제
                    break  # 반복문 종료

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()


item_size_set=[]
for x in range(1000):
    random_numbers = [
    random.randint(20,51),  # 20에서 50 사이의 난수
    random.randint(15,41),  # 15에서 40 사이의 난수
    random.randint(10,36)    # 10에서 35 사이의 난수
    ]
    item_size_set.append(random_numbers)


# In[ ]:
