import cx_Oracle

dsn_tns = cx_Oracle.makedsn('192.168.x.x', 'y', service_name='Test')
conn = cx_Oracle.connect(user='x', password='y', dsn=dsn_tns)

mail = input('Mail Adresi: ')
mesaj = input('Mesajınız: ')
c = conn.cursor()
command = "BEGIN command_sys.mail(subject_ => 'Python test maili!', from_user_name_ => 'IFSAPP', to_user_name_ => '{}',cc_ => 'huseyin.yucel@dener.com',text_ => '{}<br>');COMMIT;END;".format(mail, mesaj)
c.execute(command) 
conn.close()