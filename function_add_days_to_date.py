

#first vesion with calculation algorithm lib datetime
def date_summ(enter_date,add_days):
    from datetime import date, timedelta

    mydate =enter_date.split(".")

    day=int(mydate[0])
    month=int(mydate[1])
    year=int(mydate[2])

    result_data = date(year, month, day) + timedelta(days=add_days)
    print (result_data)

date_summ("10.01.2008", 10)




#second vesion with calculation algorithm lib datetime
def date_summ2(enter_date,add_days):
    import calendar
    mydate =enter_date.split(".")

    day=int(mydate[0])
    month=int(mydate[1])
    year=int(mydate[2])
    count_days_in_month=calendar.monthrange(year, month)[1]

    day=day+add_days

    if day>count_days_in_month :
        day=day-count_days_in_month
        month=month+1
        print("ok month")


    if month>12:
        year=year+1
        month=month-1
        print("three finish")

    print(day,month, year)

date_summ2("10.04.2022", 10)
