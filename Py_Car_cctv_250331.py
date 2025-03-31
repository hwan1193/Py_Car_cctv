import cv2
import numpy as np
import time
import streamlit as st

def main():
    st.title("비식별 자동화 기술")
    st.write("이 데모는 차량 번호판 모자이크 처리 및 속도 계산을 예시로 보여줍니다.")

    # 번호판 검출을 위한 Haar Cascade 로드
    plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

    # 영상 소스 선택 (영상 파일 경로를 raw string으로 입력)
    video_source = r"C:\Users\USER\OneDrive\바탕 화면\opencv-main\opencv-main\dawooni_car01.mp4"
    cap = cv2.VideoCapture(video_source)

    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        fps = 30

    pixels_per_meter = 10.0

    prev_center = None
    prev_time = None

    # 스트림릿에서 이미지를 업데이트할 빈 컨테이너 생성
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 그레이스케일 변환 및 번호판 검출
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 20))

        # 검출된 번호판마다 처리
        for (x, y, w, h) in plates:
            center = (x + w / 2, y + h / 2)
            current_time = time.time()
            speed = 0.0
            if prev_center is not None and prev_time is not None:
                dx = center[0] - prev_center[0]
                dy = center[1] - prev_center[1]
                dist = np.sqrt(dx**2 + dy**2)
                dt = current_time - prev_time if current_time - prev_time > 0 else 1/fps
                speed_pixels_per_sec = dist / dt
                speed_m_per_sec = speed_pixels_per_sec / pixels_per_meter
                speed = speed_m_per_sec * 3.6  # km/h 변환

            prev_center = center
            prev_time = current_time

            # 번호판 영역 모자이크 처리
            plate_region = frame[y:y+h, x:x+w]
            mosaic_factor = 0.1  # 강한 모자이크 효과
            small = cv2.resize(plate_region, (0, 0), fx=mosaic_factor, fy=mosaic_factor, interpolation=cv2.INTER_LINEAR)
            mosaic_plate = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
            frame[y:y+h, x:x+w] = mosaic_plate

            # 번호판 영역에 사각형과 속도 표시
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, f"Speed: {speed:.1f} km/h", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # OpenCV의 BGR 이미지를 RGB로 변환하여 Streamlit에 표시
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame_rgb, channels="RGB")
        
        # 영상 FPS에 맞춰 잠시 대기
        time.sleep(1/fps)

    cap.release()

if __name__ == '__main__':
    main()