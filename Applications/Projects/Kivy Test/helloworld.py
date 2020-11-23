from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class girisFormu(App):

    def build(self):
    
        duzen = GridLayout(cols=2)

        #1.Satır
        duzen.add_widget(Label(text='Kullanıcı Adı:')) #1.Sutun
        kullanici_adi = TextInput()
        duzen.add_widget(kullanici_adi) #2.Sutun

        #2.Satır
        duzen.add_widget(Label(text='Parola:')) #1.Sutun
        parola = TextInput()
        duzen.add_widget(parola) #2.Sutun

        #3.Satır
        duzen.add_widget(Widget()) #1.Sutun -- Boş Geçiliyor
        gir_dugme=Button(text='Giriş Yap')
        duzen.add_widget(gir_dugme) #2.Sutun
        
        self.title = "Giriş Formu"  
        return duzen
      
girisFormu().run()