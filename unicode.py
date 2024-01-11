from unidecode import unidecode

def chuyen_doi_tieu_de(tieu_de):
    return unidecode(tieu_de).lower().replace(" ", "-")

# Ví dụ
tieu_de_input = "tiêu đề"
tieu_de_chuyen_doi = chuyen_doi_tieu_de(tieu_de_input)
print(tieu_de_chuyen_doi)