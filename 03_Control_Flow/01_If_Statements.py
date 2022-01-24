# age = 19
# film_showing = True
#
# if age >= 18 and film_showing:
#     print("You can buy a ticket for this film")
# elif age == 17:
#     print("Come back next year")
# else:
#     print("No dice")
#
# print("This will always print")

certificate = "18"


if certificate.upper() == "U":
    print("Suitable for all ages")
elif certificate.upper() == "PG":
    print("Certificate is PG")
elif certificate.upper() in ("12", "12A"):
    print("Certificate is 12 ages and Above")
elif certificate == "15":
    print("Certificate is 15")
elif certificate == "18":
    print("Certificate is 18")
else:
    print("Certificate not recognised")
