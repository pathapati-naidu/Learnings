#replace() ,strip(),lower(),casefold(),center(),count(),encode(),expandtabs(),upper(),capitalize(),isdigit(),isalpha(),startswith(),endswith(),find(),format(),format_map()


#replace()

description="                   This is P Mahesh Kumar iam from andhra pradesh and im currently working as is a software engineer at persistent systems         jai"
replaced_description=description.replace("is","JAI")
print("REPLACE METHOD",replaced_description)

#STRIP()
strip_replace=description.strip()
print("STRIP() METHOD:", strip_replace)

#LOWER() & UPPER() & casefold()
Upper_case_conv=strip_replace.upper()
print("UPPER() METHOD:",Upper_case_conv)

Lower_conv=strip_replace.lower()
print("LOWER() METHOD:",Lower_conv)
case_fold_conv=strip_replace.casefold()
print("CASEFOLD() METHOD:",case_fold_conv)

#COUNT()
name="Mahesh Chowdary mama"
print("COUNT() METHOD:",name.count('a'))

# isdigit()
print("ISDIGIT() METHOD:",name.isdigit())

#isaplha()--->SPACE IN BETWEEN THE CHARACTERS IS ALSO CONSIDERED AS A SPECIAL CHARACTER SO IT WILL RETURN FALSE IF WE HAVE ANY SPACES IN BW THE CHARACTERS

print("ISALPHA() METHOD:",name.isalpha())



