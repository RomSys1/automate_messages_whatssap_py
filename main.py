import pywhatkit

try: 
  #enviara el mensaje
  print("Esperando WhatsApp web en el navegador...")
  pywhatkit.sendwhatmsg("+59XXXXXXXXX","Hola",00,22)
  pywhatkit.sendwhatmsg("+59XXXXXXXXX","¿Cómo estas?",00,23)
  print("Mensaje Enviado.")
 
except: 
 
  print("Error al enviar mensaje.")
