import cv2
import threading
import time

class VideoCaptureThread(threading.Thread):
    def __init__(self, Thread_id, cap, fps):
        threading.Thread.__init__(self)
        self.Thread_id = Thread_id
        self.cap = cap
        self.fps = fps
        self.VideoName = f"Video {self.Thread_id}"
        self.frames_processed = 0 #kare sayisi
        self.start_time = time.time() #gecen süre
    def run(self):

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            self.frames_processed += 1
            elapsed_time = time.time() - self.start_time #Başlangıç zamanı çıkartılarak geçen süre hesaplanır.
            fps = self.frames_processed / elapsed_time #kare sayısını geçen süreyle oranlayarak fps bulunur
            cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow(self.VideoName, frame)
            time.sleep(1/self.fps)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cv2.destroyWindow(self.VideoName)

fps_value = [20,5,1]

cap = cv2.VideoCapture(0)
threads = []
for i, fps in enumerate(fps_value):
    thread = VideoCaptureThread(i+1, cap, fps)
    threads.append(thread)
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

cap.release()
cv2.destroyAllWindows()









