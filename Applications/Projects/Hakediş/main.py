from hakedis import login_gspn,go_management,read_data_from_txt


login_gspn("https://gspn1.samsungcsportal.com/")
go_management()
read_data_from_txt('hakedisnote.txt')