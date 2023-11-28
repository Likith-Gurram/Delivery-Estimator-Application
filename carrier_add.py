import shippo

shippo.config.api_key = "shippo_test_a65516b46d291a9dce11ed82c9f7cd24acf15c5a"


fedex_account = shippo.CarrierAccount.create(
        carrier= "fedex",
        account_id= "261260377",
        parameters= {
            "first_name": "<Test>",
            "last_name": "Test",
            "phone_number": "<123456789>",
            "from_address_st": "56 crescent place ",
            "from_address_city": "Bridgeport",
            "from_address_state": "CT",
            "from_address_zip": "06608",
            "from_address_country_iso2": "US"
        },
        test= True,
        active= False,
)

ups_account = shippo.CarrierAccount.create(
    carrier = "UPS",
    account_id = "likithgurram",
    parameters= {
        "password":"@09",
        "account_number" : "B24306"
    },
    test = True,
    active = False
)


print("---------------------------------------------------------------")
print(ups_account)