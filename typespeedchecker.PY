import time

text = "Python is powerful and fast."  
print("Type this:", text)

input("Press Enter to start...")       
start = time.time()                    

typed = input("Start typing: ")        
end = time.time()                      

speed = len(typed.split()) / (end - start) * 60  
print(f"Your speed: {speed:.2f} WPM")           


# import qrcode

# data = input("Enter text or URL: ")
# img = qrcode.make(data)
# img.save("qrcode.png")
# print("QR Code saved as qrcode.png")
