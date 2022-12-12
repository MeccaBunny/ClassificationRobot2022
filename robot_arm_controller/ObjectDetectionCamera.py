import cv2
import numpy as np

# Yolo load
net = cv2.dnn.readNet("robot_arm_controller/robot_arm_controller/yolov3.weights",
 "robot_arm_controller/robot_arm_controller/yolov3.cfg")
classes = []
with open("robot_arm_controller/robot_arm_controller/coco.names", "r") as f:
    classes =  [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()

output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

def main():
    u,v = 0,0

    cap = cv2.VideoCapture(2)                       # 2번 카메라 연결

    if cap.isOpened():
        while True:
            ret, frame = cap.read()                 # 카메라 프레임 읽기

            if ret:
                cv2.imwrite('robot_arm_controller/robot_arm_controller/photo.jpg', frame) # 프레임을 'photo.jpg'에 저장
                img = cv2.imread("robot_arm_controller/robot_arm_controller/photo.jpg")

                height, width, channels = img.shape
                blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
                net.setInput(blob)
                outs = net.forward(output_layers)
                confidences = []
                boxes = []

                for out in outs:
                    for detection in out:
                        scores = detection[5:]
                        class_id = np.argmax(scores)
                        confidence = scores[class_id]

                        if class_id == 0 or class_id == 39:  #
                            if confidence > 0.5:
                                center_x = int(detection[0] * width)
                                center_y = int(detection[1] * height)
                                w = int(detection[2] * width)
                                h = int(detection[3] * height)
                                boxes.append([center_x, center_y, w, h])
                                confidences.append(float(confidence))
                                u = center_x
                                v = center_y

                indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
                font = cv2.FONT_HERSHEY_PLAIN
                for i in range(len(boxes)):
                    if i in indexes:
                        x, y, w, h = boxes[i]
                        #color = colors[i]
                        color = [0,0,255]
                        cv2.rectangle(img, (x, y), (x + 50, y + 50), color, 2)
                        cv2.putText(img, str(x)+","+str(y), (x, y+30), font, 3, color, 3)

                cv2.imwrite('robot_arm_controller/robot_arm_controller/photo.jpg', frame)
                cv2.imshow('video',img)


                #with open("/home/meccabunny/.ros/uv.txt", "r") as f:
                #    fu = f.readline()
                #    fv = f.readline()

                f = open("/home/meccabunny/.ros/uv.txt", "w")
                data = str(u) + " " + str(v) + "\n"
                f.write(data)
                f.close()

                if cv2.waitKey(100) == ord('q'): #endkey q
                    break
            else:
                print('no frame!')
                break
    else:
        print('no camera!')
    cap.release()

    cv2.destroyAllWindows()

#if __name__ == "__name__":
#    main()
main()

