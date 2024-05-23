import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import qrcode
import io
import cv2
from pyzbar.pyzbar import decode

class BarcodeApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.input = TextInput(hint_text='Enter text or URL', size_hint=(1, 0.1))
        self.layout.add_widget(self.input)

        self.generate_button = Button(text='Generate Barcode', size_hint=(1, 0.1))
        self.generate_button.bind(on_press=self.generate_barcode)
        self.layout.add_widget(self.generate_button)

        self.camera_button = Button(text='Open Camera to Scan Barcode', size_hint=(1, 0.1))
        self.camera_button.bind(on_press=self.open_camera)
        self.layout.add_widget(self.camera_button)

        self.image = Image(size_hint=(1, 0.4))
        self.layout.add_widget(self.image)

        self.camera_image = Image(size_hint=(1, 0.4))
        self.layout.add_widget(self.camera_image)

        return self.layout

    def generate_barcode(self, instance):
        data = self.input.text
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')

        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)
        self.image.texture = Image(io.BytesIO(buffer.getvalue()), ext='png').texture

    def open_camera(self, instance):
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / 30.0)

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            buffer = cv2.flip(frame, 0).tobytes()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
            self.camera_image.texture = texture

            barcodes = decode(frame)
            for barcode in barcodes:
                barcode_data = barcode.data.decode('utf-8')
                self.input.text = barcode_data
                self.capture.release()
                Clock.unschedule(self.update)
                break

if __name__ == '__main__':
    BarcodeApp().run()
