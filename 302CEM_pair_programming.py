def net_chargeable_income(annual_income):
    return annual_income - 132000 - mpf(annual_income)

def mpf(annual_income):
    if annual_income * 0.05 > 18000:
        return 18000
    elif annual_income < 85200:
        return 0
    else:
        return annual_income * 0.05

def standard_tax(net_charge_income):
    if net_charge_income < 0:
        return 0
    else:
        return (net_charge_income + 132000) * 0.15

def progressive_tax(net_charge_income):
    if net_charge_income < 0:
        return 0
    else:
        if net_charge_income <= 50000:
            return net_charge_income * 0.02
        elif net_charge_income <= 100000 and net_charge_income > 50000:
            return (net_charge_income - 50000) * 0.06 + 1000
        elif net_charge_income <= 150000 and net_charge_income > 10000:
            return (net_charge_income - 100000) * 0.1 + 3000 + 1000
        elif net_charge_income <= 200000 and net_charge_income > 150000:
            return (net_charge_income - 150000) * 0.14 + 5000 + 3000 + 1000
        else:
            return (net_charge_income / 50000 - 4) * 8500 + 16000

val = " "


while val != "0":

    martial_status = input("Enter 1 for SINGLE or 2 for MARRIED: ")

    if martial_status == "2":
        annual_income1 = input("Enter Annual Income:")
        annual_income2 = input("Enter Spouse Annual Income:")

        # check if int
        if annual_income1.isdigit() and annual_income2.isdigit():
            annual_income1 = int(annual_income1)
            annual_income2 = int(annual_income2)

            # check if negative
            if annual_income1 < 0 or annual_income2 < 0:
                print("Cannot be negative value")
            else:
                standard_payable_self = standard_tax(net_chargeable_income(annual_income1))
                standard_payable_spouse = standard_tax(net_chargeable_income(annual_income2))
                prog_payable_self = progressive_tax(net_chargeable_income(annual_income1))
                prog_payable_spouse = progressive_tax(net_chargeable_income(annual_income2))
                joint_chargeable_income = net_chargeable_income(annual_income1) + net_chargeable_income((annual_income2))
                standard_payable_joint = standard_tax(joint_chargeable_income + 132000)
                standard_payable_separate = standard_tax(net_chargeable_income(annual_income1)) + standard_tax(net_chargeable_income(annual_income2))
                progressive_payable_joint = progressive_tax(joint_chargeable_income)
                progressive_payable_separate = progressive_tax(net_chargeable_income(annual_income1)) + progressive_tax(net_chargeable_income((annual_income2)))

                total_sep_pay = 0
                total_joint_pay = 0

                if standard_payable_joint > progressive_payable_joint:
                    total_joint_pay += progressive_payable_joint
                else:
                    total_joint_pay += standard_payable_joint

                if standard_payable_self > prog_payable_self:
                    total_sep_pay += prog_payable_self
                else:
                    total_sep_pay += standard_payable_self

                if standard_payable_spouse > prog_payable_spouse:
                    total_sep_pay += prog_payable_spouse
                else:
                    total_sep_pay += standard_payable_spouse

                print("""

    ***MANDATORY PROVIDENT FUND(HK$)***
    Self: {0}
    Spouse: {1}

    ***STANDARD RATE(HK$)***
    Separate: {2}
    Joint: {3}

    ***PROGRESSIVE RATE(HK$)***
    Separate: {4}
    Joint: {5}
    
    ***TOTAL***
    Separate: {6}
    Joint: {7}

                    """.format(mpf(annual_income1), mpf(annual_income2), standard_payable_separate,
                               standard_payable_joint, progressive_payable_separate, progressive_payable_joint, total_sep_pay, total_joint_pay))

                if total_sep_pay > total_joint_pay:
                    print("Joint assessment is recommended")
                elif total_sep_pay == total_joint_pay:
                    print("No recommendation")
                else:
                    print("Joint assessment is NOT recommended")


        else:
            print('Invalid input')

    elif martial_status == "1":
        annual_income1 = input("Enter Annual Income:")
        annual_income2 = "0"

        # check if int
        if annual_income1.isdigit() and annual_income2.isdigit():
            annual_income1 = int(annual_income1)
            annual_income2 = int(annual_income2)

            # check if negative
            if annual_income1 < 0 or annual_income2 < 0:
                print("Cannot be negative value")
            else:
                # calculate for single
                standard_payable = standard_tax(net_chargeable_income(annual_income1))
                progressive_payable = progressive_tax(net_chargeable_income(annual_income1))

                print("""

    ***MANDATORY PROVIDENT FUND(HK$)***
    {0}

    ***STANDARD RATE(HK$)***
    {1}

    ***PROGRESSIVE RATE(HK$)***
    {2}                
                                        """.format(mpf(annual_income1), standard_payable, progressive_payable))
                if standard_payable > progressive_payable:
                    print("Progressive rate recommended")
                else:
                    print("Standard rate recommended")



        else:
            print('Invalid input')
    else:
        print("Invalid input")






    val = input("Press any key to continue or type 0 to leave: ")


