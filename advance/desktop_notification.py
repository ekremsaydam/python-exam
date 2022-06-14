"""Masaüstü bildirimleri."""
import time
import plyer

if __name__ == "__main__":
    while True:
        plyer.notification.notify(
            title="ALARM",
            message="Mesaj",
            app_name="desktop_notif",
            # app_icon="fv.ico",
            timeout=10,
            ticker="Bildirim geldiğinde gösterilecek metin",
            toast="Adroid mesajı"
        )
        time.sleep(3600)
