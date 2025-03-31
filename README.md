# Py_Car_cctv
** OpenCV를 활용하여 영상 내 차량 번호판을 검출하고, 검출된 번호판에 모자이크 처리.
** 이 프로젝트는 OpenCV를 활용하여 영상 내 차량 번호판을 검출하고, 검출된 번호판에 모자이크 처리를 하며, 이동 속도를 계산하는 기능을 구현한 예제입니다. 또한, Streamlit을 사용하여 웹 앱 형태로 쉽게 배포할 수 있도록 구성되어 있습니다.

## 주요 기능

- **번호판 검출**: Haar Cascade 분류기를 이용하여 차량 번호판을 검출합니다.
- **모자이크 처리**: 검출된 번호판 영역에 모자이크 효과를 적용하여 개인정보 보호를 강화합니다.
- **속도 계산**: 번호판 중심 좌표의 변화량을 기반으로 차량의 속도를 추정합니다.
- **Streamlit 배포**: 처리된 영상을 웹 앱으로 실시간 스트리밍하여 손쉽게 확인할 수 있습니다.

## 요구 사항

- Python 3.x
- [OpenCV](https://opencv.org/) (`pip install opencv-python`)
- [NumPy](https://numpy.org/) (`pip install numpy`)
- [Streamlit](https://streamlit.io/) (`pip install streamlit`)
