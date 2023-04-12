print("WELCOME TO MTN AIRTIME APP")
user_name = str(input("what is your name ?"))
acc_details = 1000
choice = 0
mtn = 1
glo = 2
airtel = 3
nmobile = 4
choice = int(input("PLEASE ENTER NETWORK PROVIDER ___"
                   "ENTER 1 : MTN"
                   "ENTER 2 : GLO"
                   "ENTER 3 : AIRTEL"
                   "ENTER 4 : NMOBILE"
                   "********************"
                   ""))
mb_100 = 1
mb_200 = 2
mb_2gb = 3
mb_20gb = 4
if choice == mtn:
    data_bundle = int(input(""
                            "***************"
                            "ENTER 1 : 100MB FOR 50 NGN"
                            "ENTER 2 : 200MB FOR 100 NGN"
                            "ENTER 3 : 2GB FOR 500 NGN"
                            "ENTER 3 : 20GB FOR 5000 NGN"
                            "******************"
                            ""))
    if acc_details > 0 :
        if data_bundle == mb_100:
            if acc_details >= 50:
                print("CONGRATULATIONS YOU HAVE BEEN CREDITED WITH 100MB FOR 2 NIGHTS" )
            else:
                print(user_name, "INSUFFICIENT FUNDS , PLEASE RECHARGE " )

                # buying 200mb
        elif data_bundle == mb_200:
            if acc_details>= 100:
                print(user_name,"CONGRATULATIONS YOU HAVE 200MB FOR 7 DAYS AND NIGHT")
            else:
                print(user_name,"INSUFFICIENT FUND . PLEASE RECHARGE ")
        elif data_bundle == mb_2gb:
            if acc_details>= 500:
                print(user_name,"CONGRATULATION YOU HAVE 2GB FOR THE MONTH ")
            else:
                print(user_name,"INSUFFICIENT FUND . PLEASE RECHARGE ")
        elif data_bundle == mb_20gb:
            if acc_details>= 5000:
                print(user_name,"CONGRATULATION YOU HAVE 20GB FOR THE MONTH ")
            else:
                print(user_name,"INSUFFICIENT FUND . PLEASE RECHARGE ")

elif choice == glo:
    data_bundle = int(input(""
                            "***************"
                            "ENTER 1 : 100MB FOR 50 NGN"
                            "ENTER 2 : 200MB FOR 100 NGN"
                            "ENTER 3 : 2GB FOR 500 NGN"
                            "ENTER 3 : 20GB FOR 5000 NGN"
                            "******************"
                            ""))
    if acc_details > 0:
        if data_bundle == mb_100:
            if acc_details >= 50:
                print("CONGRATULATIONS YOU HAVE BEEN CREDITED WITH 100MB FOR 2 NIGHTS")
            else:
                print(user_name,
                "INSUFFICIENT FUNDS, PLEASE RECHARGE ")

                # buying 200mb
        elif data_bundle == mb_200:
                if acc_details >= 100:
                    print(user_name, "CONGRATULATIONS YOU HAVE 200MB FOR 7 DAYS AND NIGHT")
                else:
                    print(user_name, "INSUFFICIENT FUND . PLEASE RECHARGE ")
        elif data_bundle == mb_2gb:
            if acc_details >= 500:
                print(user_name, "CONGRATULATION YOU HAVE 2GB FOR THE MONTH ")
            else:
                print(user_name, "INSUFFICIENT FUND . PLEASE RECHARGE ")
        elif data_bundle == mb_20gb:
            if acc_details >= 5000:
                print(user_name, "CONGRATULATION YOU HAVE 20GB FOR THE MONTH ")
            else:
                print(user_name, "INSUFFICIENT FUND . PLEASE RECHARGE ")

elif choice == airtel:
    data_bundle = int(input(""
                            "***************"
                            "ENTER 1 : 100MB FOR 50 NGN"
                            "ENTER 2 : 200MB FOR 100 NGN"
                            "ENTER 3 : 2GB FOR 500 NGN"
                            "ENTER 3 : 20GB FOR 5000 NGN"
                            "******************"
                            ""))
    if acc_details > 0:
        if data_bundle == mb_100:
            if acc_details >= 50:
                print("CONGRATULATIONS YOU HAVE BEEN CREDITED WITH 100MB FOR 2 NIGHTS")
            else:
                print(user_name,
                "INSUFFICIENT FUNDS, PLEASE RECHARGE ")

                # buying 200mb
        elif data_bundle == mb_200:
                if acc_details >= 100:
                    print(user_name, "CONGRATULATIONS YOU HAVE 200MB FOR 7 DAYS AND NIGHT")
                else:
                    print(user_name, "INSUFFICIENT FUND . PLEASE RECHARGE ")
        elif data_bundle == mb_2gb:
            if acc_details >= 500:
                print(user_name, "CONGRATULATION YOU HAVE 2GB FOR THE MONTH ")
            else:
                print(user_name, "INSUFFICIENT FUND . PLEASE RECHARGE ")
        elif data_bundle == mb_20gb:
            if acc_details >= 5000:
                print(user_name, "CONGRATULATION YOU HAVE 20GB FOR THE MONTH ")
            else:
                print(user_name, "INSUFFICIENT FUND . PLEASE RECHARGE ")

elif choice == nmobile:
    data_bundle = int(input(""
                            "***************"
                            "ENTER 1 : 100MB FOR 50 NGN"
                            "ENTER 2 : 200MB FOR 100 NGN"
                            "ENTER 3 : 2GB FOR 500 NGN"
                            "ENTER 3 : 20GB FOR 5000 NGN"
                            "******************"
                            ""))
    if acc_details > 0:
        if data_bundle == mb_100:
           if acc_details >= 50:
                print("CONGRATULATIONS YOU HAVE BEEN CREDITED WITH 100MB FOR 2 NIGHTS")
        else:
                print(user_name,
                "INSUFFICIENT FUNDS, PLEASE RECHARGE ")

                # buying 200mb
    elif data_bundle == mb_200:
        if acc_details >= 100:
                    print(user_name, "CONGRATULATIONS YOU HAVE 200MB FOR 7 DAYS AND NIGHT")
        else:
                    print(user_name, "INSUFFICIENT FUND . PLEASE RECHARGE ")
    elif data_bundle == mb_2gb:
         if acc_details >= 500:
                print(user_name, "CONGRATULATION YOU HAVE 2GB FOR THE MONTH ")
         else:
                print(user_name, "INSUFFICIENT FUND . PLEASE RECHARGE ")
    elif data_bundle == mb_20gb:
         if acc_details >= 5000:
                print(user_name, "CONGRATULATION YOU HAVE 20GB FOR THE MONTH ")
         else:
                print(user_name, "INSUFFICIENT FUND . PLEASE RECHARGE ")


