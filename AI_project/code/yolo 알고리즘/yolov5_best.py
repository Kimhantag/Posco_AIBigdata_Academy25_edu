import cv2
from ultralytics import YOLO
import numpy as np
# 모델 학습 시키기
# model = YOLO("yolov5mu.pt") # yolov5m 모델 이용
# model.train(data='./data.yaml', epochs = 100)

car_name = ['carnival', 'ray', 'soul', 'sportage', 'starex', 'tucson']

def filter_boxes(boxes, names, min_confidence=0.5):
    filtered_results = []  # filtered_results 리스트를 여기서 선언
    for box, name in zip(boxes, names):
        if len(box) > 4 and box[4] >= min_confidence:  # Check if box has confidence score
            car_name = ['carnival', 'ray', 'soul', 'sportage', 'starex', 'tucson']
            if name in car_name:  # Example: filtering boxes with 'car' label
                filtered_results.append((name, box[4], box[:4]))  # Append (name, confidence, bbox)
    return filtered_results

model = YOLO('./runs/detect/train28/weights/best.pt') # 학습시키고자 하는 데이터 불러오기
cap = cv2.VideoCapture(0) # 실시간으로 웹캠 연결 받기

while cap.isOpened() : # 웹캠이 열리면서
    ret, frame = cap.read() # 실시간 영상 읽음
    if ret :
        results = model(frame) # s모델로 학습시킨 결과의 frame을 읽어들임
        cv2.imshow("Webcam", results[0].plot()) # 윈도우에 영상 뜨게 함

        if len(results) > 0:
            filtered_results = filter_boxes(results[0].boxes, results[0].names, min_confidence=0.5)
            annotated_frame = frame.copy()
            for name, conf, bbox in filtered_results:
                bbox = [int(coord) for coord in bbox]
                cv2.rectangle(annotated_frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
                cv2.putText(annotated_frame, f'{name} {conf:.2f}', (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        for result in results:
            clist = result.boxes.cls # 영상속 감지된 객체의 class 번호를 나타내는 리스트
            cls = set()
            for cno in clist:
                cls.add(model.names[int(cno)])
            # print(cls)
            # print(clist)
            # 웹캠에 감지된 차량 종류에 따른 volume 값 반환하도록 함
            if 'carnival' in cls:
                print("Detected carnival")
                car = 'carnival'
                # cv2.destroyAllWindows()  # 모든 OpenCV 창을 닫음
                # cap.release()  # 카메라 자원 해제
                break  # 반복문 종료로 프로그램 종료
            elif 'ray' in cls:
                print("Detected ray")
                car = 'ray'
                # cv2.destroyAllWindows()  # 모든 OpenCV 창을 닫음
                # cap.release()  # 카메라 자원 해제
                break  # 반복문 종료로 프로그램 종료
            elif 'soul' in cls:
                print("Detectd soul")
                volume = 2
                # cv2.destroyAllWindows()  # 모든 OpenCV 창을 닫음
                # cap.release()  # 카메라 자원 해제
                break  # 반복문 종료로 프로그램 종료
            elif 'sportage' in cls:
                print("Detected sportage")
                volume = 3
                # cv2.destroyAllWindows()  # 모든 OpenCV 창을 닫음
                # cap.release()  # 카메라 자원 해제
                break  # 반복문 종료로 프로그램 종료
            elif 'starex' in cls:
                print("Detected starex")
                volume =4
                # cv2.destroyAllWindows()  # 모든 OpenCV 창을 닫음
                # cap.release()  # 카메라 자원 해제
                break  # 반복문 종료로 프로그램 종료
            elif 'tucson' in cls:
                print("Detected tucson")
                volume = 5
                # cv2.destroyAllWindows()  # 모든 OpenCV 창을 닫음
                # cap.release()  # 카메라 자원 해제
                break  # 반복문 종료로 프로그램 종료
    if cv2.waitKey(1) & 0xFF == ord('q'): # q를 누르면 영상 종료됨
        break
# 비디오 및 창 해제
cv2.destroyAllWindows()
cap.release()