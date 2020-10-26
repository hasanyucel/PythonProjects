import cx_Oracle

dsn_tns = cx_Oracle.makedsn('x', 'y', service_name='z')
conn = cx_Oracle.connect(user='x', password='y', dsn=dsn_tns)

aday = input('Aday Firma No: ')
actype = input('Aktivite Türü: ')
tanim = input('Başlık : ')

c = conn.cursor()
command = '''DECLARE
	p0_ VARCHAR2(32000) := NULL;
	p1_ VARCHAR2(32000) := NULL;
	p2_ VARCHAR2(32000) := NULL;
	p3_ VARCHAR2(32000) := 'DESCRIPTION' || chr(31) || '{2}' || chr(30) || 'CONNECTION_TYPE' || chr(31) || 'Aday Firma' || chr(30) || 'CONNECTION_ID' ||
						   chr(31) || '{0}' || chr(30) || 'COMPANY' || chr(31) || 'DENER' || chr(30) || 'ACTIVITY_TYPE' || chr(31) || '{1}' || chr(30) ||
						   'LEAD_CONTACT_ID' || chr(31) || '34' || chr(30) || 'MAIN_REPRESENTATIVE_ID' || chr(31) || '11008' || chr(30) ||
						   'CALENDAR_ACTIVITY_TYPE' || chr(31) || 'Randevu' || chr(30) || 'START_DATE' || chr(31) || '2020-10-23-14.30.00' || chr(30) ||
						   'END_DATE' || chr(31) || '2020-10-23-15.01.00' || chr(30);
	p4_ VARCHAR2(32000) := 'DO';

BEGIN
	ifsapp.language_sys.set_language('tr');
	ifsapp.business_activity_api.new__(p0_, p1_, p2_, p3_, p4_);
    COMMIT;
END;'''.format(aday,actype,tanim)
c.execute(command)
conn.close()