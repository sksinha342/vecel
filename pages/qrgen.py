import qrcode
import io
import cloudinary.uploader

def generate_qr(text):
    qr = qrcode.make(text)
    img_byte_arr = io.BytesIO()
    qr.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    # Cloudinary par upload karne ka logic (optional)
    # response = cloudinary.uploader.upload(img_byte_arr)
    # return response['url']
    
    return "QR Code Generated (Function Triggered)"
